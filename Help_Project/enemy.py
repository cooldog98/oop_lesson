import pygame
from player import Player
from os import walk
from os.path import join


class Enemy_1(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = x
        self.y_vel = y
        self.load_image()
        self.state, self.frames_index = 'ghost', 0
        self.image = self.frames[self.state][0]
        self.speed = 6
        self.attack_range = 300  # Distance at which enemy will start chasing
        self.direction = 'right'  # Start facing right
        # self.animation_timer = 0
        self.hp = 50

        self.attack_cooldown = 60 #cooldown when attack player
        self.is_attacking = False
        self.retreat_distance = 100 #dis affert attack
        self.target_x = x #ตำแหน่งเป้าหมายในการถอยหลัง
        self.get_attack = False

        self.hurt_duration = 20
        self.hurt_timer = 0

    def reload_frames(self, flipped=False):
        frames = {state: [] for state in self.frame_paths.keys()}
        new_size = (self.rect.width, self.rect.height)

        for state, paths in self.frame_paths.items():
            for path in paths:
                surf = pygame.image.load(path).convert_alpha()
                surf = pygame.transform.scale(surf, new_size)
                if flipped:
                    surf = pygame.transform.flip(surf, True, False)
                frames[state].append(surf)

        return frames

    def load_image(self):
        self.frames = {'attake': [], 'ghost': [], 'hurt': []}
        self.frame_paths = {state: [] for state in self.frames.keys()}
        new_size = (self.rect.width, self.rect.height)

        for state in self.frames.keys():
            for folder_path, sub_folder, file_names in walk(join('enemy', 'ghost_1', state)):
                if file_names:
                    file_names = [f for f in file_names if f.endswith('.png')]
                    file_names.sort(key=lambda x: int(x.split('.')[0]))
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        self.frame_paths[state].append(full_path)
                        original_surf = pygame.image.load(full_path).convert_alpha()
                        surf = pygame.transform.scale(original_surf, new_size)
                        self.frames[state].append(surf)

    def update_enemy(self, player: Player, offset_x):
        # calculate between player and enemy
        player_true_x = player.rect.x
        player_true_y = player.rect.y
        dist_x = player_true_x - self.x_vel
        dist_y = player_true_y - self.y_vel

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 2

        if self.hurt_timer > 0:
            self.hurt_timer -= 1
            self.state = 'hurt'
            if self.hurt_timer == 0:
                self.get_attack = False

        if self.is_attacking:
            # go back after attack
            if self.direction == 'right':
                self.x_vel -= self.speed
                if self.get_attack:
                    self.state = 'hurt'
                if self.x_vel < self.target_x - self.retreat_distance:
                    self.is_attacking = False
            else:
                self.x_vel += self.speed
                if self.get_attack:
                    self.state = 'hurt'
                if self.x_vel > self.target_x + self.retreat_distance:
                    self.is_attacking = False

        elif abs(dist_x) < self.attack_range and abs(dist_y) <= 50:
            # if  self.get_attack == False:
            self.state = 'ghost'
            if abs(dist_x) > 20:
                if dist_x > 0:  # player on right
                    if self.direction != 'right':
                        if self.get_attack:
                            self.state = 'hurt'
                        self.direction = 'right'
                        self.frames = self.reload_frames(flipped=False)
                    self.x_vel += self.speed
                else:  # # player in left
                    if self.direction != 'left':
                        if self.get_attack:
                            self.state = 'hurt'
                        self.direction = 'left'
                        self.frames = self.reload_frames(flipped=True)
                    self.x_vel -= self.speed

            # elif self.get_attack == True:
            #     self.state = 'hurt'
            if abs(dist_x) > 20:
                if dist_x > 0:  # player on right
                    if self.direction != 'right':
                        if self.get_attack:
                            self.state = 'hurt'
                        self.direction = 'right'
                        self.frames = self.reload_frames(flipped=False)
                    self.x_vel += self.speed
                else:  # player in left
                    if self.direction != 'left':
                        if self.get_attack:
                            self.state = 'hurt'
                        self.direction = 'left'
                        self.frames = self.reload_frames(flipped=True)
                    self.x_vel -= self.speed

            elif abs(dist_y) <= 50 and abs(dist_x) != 0:
                # if abs(dist_y) <= 50 and abs(dist_x) != 0:
                print(f'attack {abs(dist_y)} , {player_true_y}')
                if self.attack_cooldown == 0:
                    if self.get_attack:
                        self.state = 'hurt'
                    self.state = 'attake'
                    self.attack_cooldown = 60
                    self.is_attacking = True
                    self.target_x = self.x_vel - 10
                    print("enemy attack!")  # ตรงนี้คุณจะเชื่อมไปลด HP ผู้เล่นได้
                    player.health_player(3)
            # else:
            #     print('run')
            #     print(abs(dist_y), player_true_y)
            #     if self.attack_cooldown == 0:
            #         self.state = 'ghost'
            #         self.target_x = self.x_vel

        else:
            print('ghost')
            if self.get_attack:
                self.state = 'hurt'
            else:
                self.state = 'ghost'


        # update animation
        self.animate(dt=1 / 60)
        self.rect.x = self.x_vel - offset_x

    # def update_enemy(self, player: Player, offset_x):
    #     # Calculate distance to player in world coordinates
    #     player_true_x = player.rect.x
    #     player_true_y = player.rect.y
    #     dist_x = player_true_x - self.x_vel
    #     dist_y = player_true_y - self.y_vel
    #
    #     if self.attack_cooldown > 0:
    #         self.attack_cooldown -= 1
    #
    #     # if self.is_attacking:
    #
    #     #Only move if player is within attack range
    #     if abs(dist_x) < self.attack_range and abs(dist_y) <= player_true_y:
    #         self.state = 'ghost'
    #
    #         # Calculate desired distance (maintain 10px space)
    #         if dist_x > 15:  # Player is to the right
    #             if self.direction != 'right':
    #                 self.direction = 'right'
    #                 self.frames = self.reload_frames(flipped=False)
    #                 # if self.x_vel <= self.target_x - self.retreat_distance:
    #             # Move right but stop 10px before player
    #             if dist_x - 4 > self.speed:
    #                 self.x_vel += self.speed
    #             else:
    #                 self.x_vel = player_true_x - 20
    #
    #         elif dist_x < -15:  # Player is to the left
    #             if self.direction != 'left':
    #                 self.direction = 'left'
    #                 self.frames = self.reload_frames(flipped=True)
    #             # Move left but stop 10px before player
    #             if abs(dist_x) - 4 > self.speed:
    #                 self.x_vel -= self.speed
    #             else:
    #                 self.x_vel = player_true_x + 20
    #
    #         else:
    #             # Within 10px range - don't move
    #             self.state = 'ghost'
    #     else:
    #         self.state = 'ghost'
    #
    #     #Update animation
    #     self.animate(dt=1 / 60)
    #     # Update screen position
    #     self.rect.x = self.x_vel - offset_x

    def animate(self, dt):
        self.frames_index += 7 * dt
        if self.frames_index >= len(self.frames[self.state]):
            self.frames_index = 0
        self.image = self.frames[self.state][int(self.frames_index)]

    def enemy_move_left(self, dx):
        self.x_vel -= dx

    def draw_enemy(self, screen, offset_x):
        """ - offset_x make enemy not move follow screen."""
        # screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        screen.blit(self.image, (self.x_vel - offset_x, self.rect.y))

    def health(self, bullet):
        # self.state = 'hurt'
        self.hp -= bullet
        self.get_attack = True
        self.hurt_timer = self.hurt_duration
        # if self.hp <= 0:
        #     self.alive = False