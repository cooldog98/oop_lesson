import pygame
from os import walk
from os.path import isfile, join
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    color = (255, 0, 0)
    gravity = 0.4
    # SPRITES = load_sprite_sheets('graphic', 'animation', 210, 266, True)
    '''dir1 , dir2 is dir that picture stay with width and height is size of picture thant
    use to cut if fix incorrect size the picture will have another picture than beside wit, then ture is
    make right and left direction'''
    animation_delay = 5

    def __init__(self, x, y, width, height):
        super().__init__()
        """The top-left corner of the screen is (0, 0)."""
        """The x-axis increases from left to right."""
        """The y-axis increases from top to bottom."""
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.make = None
        self.direction = 'left'
        # self.ani_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.count = 0
        # self.animation_timer = 0

        self.load_image()
        self.state, self.frames_index = 'player', 0
        self.image = self.frames[self.state][0]

        self.bullets = pygame.sprite.Group()
        self.shoot_cooldown = 0

        self.hp = 100


    def jump(self):
        # self.y_vel = -self.gravity * 8
        self.ani_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.y_vel = -self.gravity * 8
            self.fall_count = 0
        elif self.jump_count == 2:
            self.y_vel = -self.gravity * 10
            self.fall_count = 0

    def move(self, dx, dy):
        """move dx(left right) dy(up down)"""
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        """because The top-left corner of the screen is (0, 0).
        if, want to go left vel need to be negative."""
        self.x_vel = -vel
        """check def work or not"""
        if self.direction != 'left':
            self.direction = 'left'
            current_index = self.frames_index
            self.frames = self.reload_frames(flipped=True)
            self.frames_index = current_index
            self.ani_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != 'right':
            self.direction = 'right'
            current_index = self.frames_index
            self.frames = self.reload_frames(flipped=False)
            self.frames_index = current_index
            self.ani_count = 0

    # def _gravity(self, fps):
    #     self.y_vel += min(2, (self.fall_count / fps) * self.gravity)
    #     self.fall_count += 1

    def loop(self, fps, dt):
        self.y_vel += min(2, (self.fall_count / fps) * self.gravity)
        self.fall_count += 1
        # self.y_vel += min(2, (self.fall_count / fps) * self.gravity)
        # self.fall_count += 1
        #
        # # Apply dt to movement
        # x_move = self.x_vel * dt * 60
        # y_move = self.y_vel * dt * 60
        #
        # self.move(x_move, y_move)

        # self.fall_count += 1
        # self.update_sprite()
        # if self.animation_timer >= self.animation_delay:
        #     self.update_sprite()
        #     self.animation_timer = 0
        # self.animation_timer += 1

    def draw_player(self, screen, offset_x):
        screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        # self.sprite = self.SPRITES['run_use_' + self.direction][0]
        # if self.sprite:
        #     screen.blit(self.sprite, (self.rect.x, self.rect.y))
        # pygame.draw.rect(screen, self.color, self.rect)

    def stop(self):
        self.x_vel = 0

    def reload_frames(self, flipped=False):
        frames = {state: [] for state in self.frame_paths.keys()}
        # new_size = (self.rect.width * 2, self.rect.height* 2)
        new_size = (self.rect.width, self.rect.height)

        for state, paths in self.frame_paths.items():
            for path in paths:
                surf = pygame.image.load(path).convert_alpha()
                surf = pygame.transform.scale(surf, new_size)
                if flipped:
                    surf = pygame.transform.flip(surf, True, False)
                    """pygame.transform.flip(surf, True, False) mean flip picture from left to right"""
                frames[state].append(surf)

        return frames

    def load_image(self):
        self.frames = {'dying': [], 'hit': [], 'jump': [], 'jump_2': [], 'player': [], 'run': [], 'shoot': []}
        self.frame_paths = {state: [] for state in self.frames.keys()}
        # new_size = (self.rect.width * 2, self.rect.height * 2)
        new_size = (self.rect.width, self.rect.height)
        for state in self.frames.keys():
            for folder_path, sub_folder, file_names in walk(join('graphic', 'animation', state)):
                if file_names:
                    """skip .DS_Store or another file that nor be .png"""
                    file_names = [f for f in file_names if f.endswith('.png')]
                    """sort file"""
                    file_names.sort(key=lambda x: int(x.split('.')[0]))
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        self.frame_paths[state].append(full_path)
                        original_surf = pygame.image.load(full_path).convert_alpha()
                        surf = pygame.transform.scale(original_surf, new_size)
                        self.frames[state].append(surf)
        print(self.frames)

    def animate(self, dt):
        # Get state
        if self.x_vel != 0:
            self.state = 'run'
        elif self.y_vel != 0:
            if self.jump_count == 1 or self.jump_count == 2:
                self.state = 'jump'
        elif self.y_vel > self.gravity * 2:
            if self.x_vel != 0:
                self.state = 'run'
            elif self.x_vel == 0:
                self.state = 'player'
        elif self.x_vel == 0:
            self.state = 'player'

        # Animate
        # print(self.x_vel)
        self.frames_index += 7 * dt
        self.image = self.frames[self.state][int(self.frames_index) % len(self.frames[self.state])]

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    # def die(self):
    #     self.rect.y = 100
    #     self.y_vel = 0
    #     self.x_vel = 0

    def shoot(self):
        if self.shoot_cooldown == 0:
            # Better bullet spawn position (from player's gun)
            if self.direction == 'right':
                bullet_x = self.rect.right + 10
            else:
                bullet_x = self.rect.left - 10
            bullet_y = self.rect.centery  # Adjust to gun position

            bullet = Bullet(bullet_x, bullet_y, self.direction)
            self.bullets.add(bullet)
            self.shoot_cooldown = 15  # Cooldown frames

    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def health_player(self, damage):
        self.hp -= damage