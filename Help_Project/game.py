import sys
import pygame


from player import Player
from game_platform import Platform
from health import HealthBar
from block import Block
from enemy import Enemy_1


"""start pygame"""
pygame.init()

"""change name in windows pygame"""
pygame.display.set_caption('PLATFORMER GAME: HELP')

"""set the screen size (w, h)"""
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))


# """set fonts and colors"""
# font = pygame.font.SysFont('Arial', 40)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
#
#
# class Player(pygame.sprite.Sprite):
#     color = (255, 0, 0)
#     gravity = 0.4
#     # SPRITES = load_sprite_sheets('graphic', 'animation', 210, 266, True)
#     '''dir1 , dir2 is dir that picture stay with width and height is size of picture thant
#     use to cut if fix incorrect size the picture will have another picture than beside wit, then ture is
#     make right and left direction'''
#     animation_delay = 5
#
#     def __init__(self, x, y, width, height):
#         super().__init__()
#         """The top-left corner of the screen is (0, 0)."""
#         """The x-axis increases from left to right."""
#         """The y-axis increases from top to bottom."""
#         self.rect = pygame.Rect(x, y, width, height)
#         self.x_vel = 0
#         self.y_vel = 0
#         self.make = None
#         self.direction = 'left'
#         # self.ani_count = 0
#         self.fall_count = 0
#         self.jump_count = 0
#         self.count = 0
#         # self.animation_timer = 0
#
#         self.load_image()
#         self.state, self.frames_index = 'player', 0
#         self.image = self.frames[self.state][0]
#
#         self.bullets = pygame.sprite.Group()
#         self.shoot_cooldown = 0
#
#         self.hp = 100
#
#
#     def jump(self):
#         # self.y_vel = -self.gravity * 8
#         self.ani_count = 0
#         self.jump_count += 1
#         if self.jump_count == 1:
#             self.y_vel = -self.gravity * 8
#             self.fall_count = 0
#         elif self.jump_count == 2:
#             self.y_vel = -self.gravity * 10
#             self.fall_count = 0
#
#     def move(self, dx, dy):
#         """move dx(left right) dy(up down)"""
#         self.rect.x += dx
#         self.rect.y += dy
#
#     def move_left(self, vel):
#         """because The top-left corner of the screen is (0, 0).
#         if, want to go left vel need to be negative."""
#         self.x_vel = -vel
#         """check def work or not"""
#         if self.direction != 'left':
#             self.direction = 'left'
#             current_index = self.frames_index
#             self.frames = self.reload_frames(flipped=True)
#             self.frames_index = current_index
#             self.ani_count = 0
#
#     def move_right(self, vel):
#         self.x_vel = vel
#         if self.direction != 'right':
#             self.direction = 'right'
#             current_index = self.frames_index
#             self.frames = self.reload_frames(flipped=False)
#             self.frames_index = current_index
#             self.ani_count = 0
#
#     # def _gravity(self, fps):
#     #     self.y_vel += min(2, (self.fall_count / fps) * self.gravity)
#     #     self.fall_count += 1
#
#     def loop(self, fps, dt):
#         self.y_vel += min(2, (self.fall_count / fps) * self.gravity)
#         self.fall_count += 1
#         # self.y_vel += min(2, (self.fall_count / fps) * self.gravity)
#         # self.fall_count += 1
#         #
#         # # Apply dt to movement
#         # x_move = self.x_vel * dt * 60
#         # y_move = self.y_vel * dt * 60
#         #
#         # self.move(x_move, y_move)
#
#         # self.fall_count += 1
#         # self.update_sprite()
#         # if self.animation_timer >= self.animation_delay:
#         #     self.update_sprite()
#         #     self.animation_timer = 0
#         # self.animation_timer += 1
#
#     def draw_player(self, screen, offset_x):
#         screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))
#         # self.sprite = self.SPRITES['run_use_' + self.direction][0]
#         # if self.sprite:
#         #     screen.blit(self.sprite, (self.rect.x, self.rect.y))
#         # pygame.draw.rect(screen, self.color, self.rect)
#
#     def stop(self):
#         self.x_vel = 0
#
#     def reload_frames(self, flipped=False):
#         frames = {state: [] for state in self.frame_paths.keys()}
#         # new_size = (self.rect.width * 2, self.rect.height* 2)
#         new_size = (self.rect.width, self.rect.height)
#
#         for state, paths in self.frame_paths.items():
#             for path in paths:
#                 surf = pygame.image.load(path).convert_alpha()
#                 surf = pygame.transform.scale(surf, new_size)
#                 if flipped:
#                     surf = pygame.transform.flip(surf, True, False)
#                     """pygame.transform.flip(surf, True, False) mean flip picture from left to right"""
#                 frames[state].append(surf)
#
#         return frames
#
#     def load_image(self):
#         self.frames = {'dying': [], 'hit': [], 'jump': [], 'jump_2': [], 'player': [], 'run': [], 'shoot': []}
#         self.frame_paths = {state: [] for state in self.frames.keys()}
#         # new_size = (self.rect.width * 2, self.rect.height * 2)
#         new_size = (self.rect.width, self.rect.height)
#         for state in self.frames.keys():
#             for folder_path, sub_folder, file_names in walk(join('graphic', 'animation', state)):
#                 if file_names:
#                     """skip .DS_Store or another file that nor be .png"""
#                     file_names = [f for f in file_names if f.endswith('.png')]
#                     """sort file"""
#                     file_names.sort(key=lambda x: int(x.split('.')[0]))
#                     for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
#                         full_path = join(folder_path, file_name)
#                         self.frame_paths[state].append(full_path)
#                         original_surf = pygame.image.load(full_path).convert_alpha()
#                         surf = pygame.transform.scale(original_surf, new_size)
#                         self.frames[state].append(surf)
#         print(self.frames)
#
#     def animate(self, dt):
#         # Get state
#         if self.x_vel != 0:
#             self.state = 'run'
#         elif self.y_vel != 0:
#             if self.jump_count == 1 or self.jump_count == 2:
#                 self.state = 'jump'
#         elif self.y_vel > self.gravity * 2:
#             if self.x_vel != 0:
#                 self.state = 'run'
#             elif self.x_vel == 0:
#                 self.state = 'player'
#         elif self.x_vel == 0:
#             self.state = 'player'
#
#         # Animate
#         # print(self.x_vel)
#         self.frames_index += 7 * dt
#         self.image = self.frames[self.state][int(self.frames_index) % len(self.frames[self.state])]
#
#     def landed(self):
#         self.fall_count = 0
#         self.y_vel = 0
#         self.jump_count = 0
#
#     def hit_head(self):
#         self.count = 0
#         self.y_vel *= -1
#
#     # def die(self):
#     #     self.rect.y = 100
#     #     self.y_vel = 0
#     #     self.x_vel = 0
#
#     def shoot(self):
#         if self.shoot_cooldown == 0:
#             # Better bullet spawn position (from player's gun)
#             if self.direction == 'right':
#                 bullet_x = self.rect.right + 10
#             else:
#                 bullet_x = self.rect.left - 10
#             bullet_y = self.rect.centery  # Adjust to gun position
#
#             bullet = Bullet(bullet_x, bullet_y, self.direction)
#             self.bullets.add(bullet)
#             self.shoot_cooldown = 15  # Cooldown frames
#
#     def update(self):
#         if self.shoot_cooldown > 0:
#             self.shoot_cooldown -= 1
#
#     def health_player(self, damage):
#         self.hp -= damage
#
#
# # StartScreen class to show the start screen
# class StartScreen:
#     def __init__(self):
#         self.running = True
#         self.player_name = ""
#         self.bg_image = pygame.image.load("assets/login_bg.jpg")  #  path to background image
#         self.bg_image = pygame.transform.scale(self.bg_image,
#                                                (screen_width, screen_height))  #  scale to screen size
#
#     def prompt_for_name(self):
#         text = ''
#         font = pygame.font.SysFont('Arial', 40)
#         # screen.blit(self.bg_image, (0, 0)) # draw background
#         # txt_surface = font.render(text, True, BLACK) #make a tzt box and label
#         input_box = pygame.Rect(400, 400, 300, 50)
#         color_inactive = pygame.Color('lightskyblue')
#         color_active = pygame.Color('dodgerblue')
#         color = color_inactive
#         active = False
#         clock = pygame.time.Clock()
#
#         # screen.blit(self.bg_image, (0, 0)) # draw background
#         # txt_surface = font.render(text, True, BLACK) #make a tzt box and label
#
#         while True:
#             # screen.blit(self.bg_image, (0, 0))
#             # txt_surface = font.render(text, True, BLACK)  # make a tzt box and label
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if input_box.collidepoint(event.pos):
#                         active = not active
#                         color = color_active if active else color_inactive
#                     else:
#                         active = False
#                         color = color_inactive
#
#                 if event.type == pygame.KEYDOWN:
#                     if active:
#                         if event.key == pygame.K_RETURN:
#                             self.player_name = text  # Save player name when hitting Enter
#                             return self.player_name
#                         elif event.key == pygame.K_BACKSPACE:
#                             text = text[:-1]
#                         else:
#                             text += event.unicode
#
#             # Draw everything
#             screen.blit(self.bg_image, (0, 0))  # draw background
#             txt_surface = font.render(text, True, WHITE)  # make a tzt box and label
#             width = max(200, txt_surface.get_width()+10)
#             input_box.w = width
#             screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
#             pygame.draw.rect(screen, color, input_box, 2)
#
#             start_button = pygame.Rect(330, 315, 350, 70)
#             pygame.draw.rect(screen, BLACK, start_button)
#             start_text = font.render("Enter your name:", True, WHITE)
#             screen.blit(start_text, (350, 330))
#             # pygame.draw.rect(screen, BLACK, start_text)
#
#             pygame.display.update()
#             clock.tick(30)
#
#     def display(self):
#         # input_box = pygame.Rect((screen_width - 400) // 2, 350, 400, 60)
#         # color_inactive = pygame.Color('lightskyblue')
#         # color_active = pygame.Color('dodgerblue')
#         # color = color_inactive
#         # text = ''
#         # font = pygame.font.SysFont('Arial', 40)
#         while self.running:
#             """make background"""
#             screen.blit(self.bg_image, (0, 0))
#
#             # Title
#             start_button = pygame.Rect(340, 170, 320, 70)
#             pygame.draw.rect(screen, BLACK, start_button)
#             title_text = font.render('Enjoy the game', True, WHITE)
#             title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
#             screen.blit(title_text, title_rect)
#
#             # # Input prompt
#             # prompt_text = font.render("Enter your name:", True, BLACK)
#             # screen.blit(prompt_text, (input_box.x, input_box.y - 50))
#             #
#             # # Input box
#             # txt_surface = font.render(text, True, BLACK)
#             # input_box.w = max(300, txt_surface.get_width() + 20)
#             # pygame.draw.rect(screen, color, input_box, 2)
#             # screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))
#
#             # Start Button
#             # pygame.Rect()
#             start_button = pygame.Rect((screen_width - 300) // 2, 600, 300, 50)
#             pygame.draw.rect(screen, GREEN, start_button)
#             start_text = font.render('Start Game', True, BLACK)
#             start_text_rect = start_text.get_rect(center=start_button.center)
#             screen.blit(start_text, start_text_rect)
#
#             # Exit Button
#             exit_button = pygame.Rect((screen_width - 300) // 2, 670, 300, 50)
#             pygame.draw.rect(screen, GREEN, exit_button)
#             exit_text = font.render('Exit Game', True, BLACK)
#             exit_text_rect = exit_text.get_rect(center=exit_button.center)
#             screen.blit(exit_text, exit_text_rect)
#
#             # Handle events
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     mouse_pos = pygame.mouse.get_pos()
#                     if start_button.collidepoint(mouse_pos):
#                         player_name = self.prompt_for_name()
#                         print(f"Starting game with player: {player_name}")
#                         return player_name  # Pass player name to the game loop
#                     elif exit_button.collidepoint(mouse_pos):
#                         print("Exiting game")
#                         pygame.quit()
#                         sys.exit()
#
#                 pygame.display.update()
#
#
# class HealthBar:
#     def __init__(self, x, y, w, h, max_hp):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         self.hp = max_hp
#         self.max_hp = max_hp
#
#     def draw(self, surf):
#         """calculate health ratio"""
#         ratio = self.hp / self.max_hp
#         pygame.draw.rect(screen, 'red', (self.x, self.y, self.w, self.h))
#         pygame.draw.rect(screen, 'green', (self.x, self.y, self.w * ratio, self.h))
#
#     # def health_player(self, damage):
#     #     self.hp -= damage
#
#
# class Platform:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_background(self, name):
#         path = os.path.join('graphic', name)  # Join the file path correctly
#         """os.path.join('assets', 'Background', 'back_G_help.jpg') assets โฟร์เ้อใหญ่สุดที่ ไฟล์รูปภาพเก็บไว้
#         Background โฟเด้อรองลงมา back_G_help.jpg ไฟล์รูปภาพ or 'graphic', name: graphic is bigger folder that
#          keep file picture, name is file picture """
#         image = pygame.image.load(path)
#         __, __, width_image, height_image = image.get_rect()
#         tiles = []
#
#         for i in range(self.width // width_image + 1):
#             for j in range(self.height//height_image + 1):
#                 pos = [i * width_image, j * height_image]
#                 tiles.append(pos)
#
#         return tiles, image
#
#     def draw(self, screen_, background, bg_image, player, objects, offset_x):
#         for tile in background:
#             screen_.blit(bg_image, tuple(tile))
#
#         for obj in objects:
#             obj.draw(screen_, offset_x)
#
#         player.draw_player(screen_, offset_x)
#
#
# class Object(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height, name=None):
#         super().__init__()
#         self.rect = pygame.Rect(x, y, width, height)
#         self.image = pygame.Surface((width, height), pygame.SRCALPHA)
#         self.width = width
#         self.height = height
#         self.name = name
#
#     def draw(self, _screen, offset_x):
#         _screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))
#
#
# class Block(Object):
#     def __init__(self, x, y, size):
#         super().__init__(x, y, size, size)
#         block = self.get_block(size)
#         self.image.blit(block, (0, 0))
#         self.mask = pygame.mask.from_surface(self.image)
#
#     def get_block(self, size, folder='graphic', picture='walland green.jpg'):
#         path = join(folder, picture)
#         image = pygame.image.load(path).convert_alpha()
#         surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
#         rect = pygame.Rect(0, 0, size, size)
#         surface.blit(image, (0, 0), rect)
#         return pygame.transform.scale(surface, (size, size))
#
#
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y, direction, speed=15):
#         super().__init__()
#         # Make bullet more visible
#         self.image = pygame.Surface((20, 5))  # Wider bullet
#         self.image.fill(((0, 255, 255)))  # Bright yellow color
#         pygame.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), 1)  # Red border
#         self.rect = self.image.get_rect(center=(x, y))
#         self.speed = speed
#         self.direction = direction
#         self.lifetime = 90  # Longer lifetime
#         self.true_x = x  # Store absolute position for scrolling
#         self.mask = pygame.mask.from_surface(self.image)
#
#     def update(self, dt, offset_x=0):
#         move_distance = self.speed * dt * 60
#
#         if self.direction == 'right':
#             self.true_x += move_distance
#         else:
#             self.true_x -= move_distance
#
#         self.rect.x = self.true_x - offset_x
#
#         # Remove old bullets
#         # self.lifetime -= 1
#         # if self.lifetime <= 0:
#         #     self.kill()
#
#
# class Enemy_1(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height):
#         super().__init__()
#         self.rect = pygame.Rect(x, y, width, height)
#         # self.x = x
#         self.x_vel = x
#         self.y_vel = y
#         self.load_image()
#         self.state, self.frames_index = 'ghost', 0
#         self.image = self.frames[self.state][0]
#         self.speed = 6
#         self.attack_range = 300  # Distance at which enemy will start chasing
#         self.direction = 'right'  # Start facing right
#         # self.animation_timer = 0
#         self.hp = 50
#
#         self.attack_cooldown = 60 #cooldown when attack player
#         self.is_attacking = False
#         self.retreat_distance = 100 #dis affert attack
#         self.target_x = x #ตำแหน่งเป้าหมายในการถอยหลัง
#         self.get_attack = False
#
#         self.hurt_duration = 20
#         self.hurt_timer = 0
#
#     def reload_frames(self, flipped=False):
#         frames = {state: [] for state in self.frame_paths.keys()}
#         new_size = (self.rect.width, self.rect.height)
#
#         for state, paths in self.frame_paths.items():
#             for path in paths:
#                 surf = pygame.image.load(path).convert_alpha()
#                 surf = pygame.transform.scale(surf, new_size)
#                 if flipped:
#                     surf = pygame.transform.flip(surf, True, False)
#                 frames[state].append(surf)
#
#         return frames
#
#     def load_image(self):
#         self.frames = {'attake': [], 'ghost': [], 'hurt': []}
#         self.frame_paths = {state: [] for state in self.frames.keys()}
#         new_size = (self.rect.width, self.rect.height)
#
#         for state in self.frames.keys():
#             for folder_path, sub_folder, file_names in walk(join('enemy', 'ghost_1', state)):
#                 if file_names:
#                     file_names = [f for f in file_names if f.endswith('.png')]
#                     file_names.sort(key=lambda x: int(x.split('.')[0]))
#                     for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
#                         full_path = join(folder_path, file_name)
#                         self.frame_paths[state].append(full_path)
#                         original_surf = pygame.image.load(full_path).convert_alpha()
#                         surf = pygame.transform.scale(original_surf, new_size)
#                         self.frames[state].append(surf)
#
#     def update_enemy(self, player: Player, offset_x):
#         # calculate between player and enemy
#         player_true_x = player.rect.x
#         player_true_y = player.rect.y
#         dist_x = player_true_x - self.x_vel
#         dist_y = player_true_y - self.y_vel
#
#         if self.attack_cooldown > 0:
#             self.attack_cooldown -= 2
#
#         if self.hurt_timer > 0:
#             self.hurt_timer -= 1
#             self.state = 'hurt'
#             if self.hurt_timer == 0:
#                 self.get_attack = False
#
#         if self.is_attacking:
#             # go back after attack
#             if self.direction == 'right':
#                 self.x_vel -= self.speed
#                 if self.get_attack:
#                     self.state = 'hurt'
#                 if self.x_vel < self.target_x - self.retreat_distance:
#                     self.is_attacking = False
#             else:
#                 self.x_vel += self.speed
#                 if self.get_attack:
#                     self.state = 'hurt'
#                 if self.x_vel > self.target_x + self.retreat_distance:
#                     self.is_attacking = False
#
#         elif abs(dist_x) < self.attack_range and abs(dist_y) <= 50:
#             # if  self.get_attack == False:
#             self.state = 'ghost'
#             if abs(dist_x) > 20:
#                 if dist_x > 0:  # player on right
#                     if self.direction != 'right':
#                         if self.get_attack:
#                             self.state = 'hurt'
#                         self.direction = 'right'
#                         self.frames = self.reload_frames(flipped=False)
#                     self.x_vel += self.speed
#                 else:  # # player in left
#                     if self.direction != 'left':
#                         if self.get_attack:
#                             self.state = 'hurt'
#                         self.direction = 'left'
#                         self.frames = self.reload_frames(flipped=True)
#                     self.x_vel -= self.speed
#
#             # elif self.get_attack == True:
#             #     self.state = 'hurt'
#             if abs(dist_x) > 20:
#                 if dist_x > 0:  # player on right
#                     if self.direction != 'right':
#                         if self.get_attack:
#                             self.state = 'hurt'
#                         self.direction = 'right'
#                         self.frames = self.reload_frames(flipped=False)
#                     self.x_vel += self.speed
#                 else:  # player in left
#                     if self.direction != 'left':
#                         if self.get_attack:
#                             self.state = 'hurt'
#                         self.direction = 'left'
#                         self.frames = self.reload_frames(flipped=True)
#                     self.x_vel -= self.speed
#
#             elif abs(dist_y) <= 50 and abs(dist_x) != 0:
#                 # if abs(dist_y) <= 50 and abs(dist_x) != 0:
#                 print(f'attack {abs(dist_y)} , {player_true_y}')
#                 if self.attack_cooldown == 0:
#                     if self.get_attack:
#                         self.state = 'hurt'
#                     self.state = 'attake'
#                     self.attack_cooldown = 60
#                     self.is_attacking = True
#                     self.target_x = self.x_vel - 10
#                     print("enemy attack!")  # ตรงนี้คุณจะเชื่อมไปลด HP ผู้เล่นได้
#                     player.health_player(3)
#             # else:
#             #     print('run')
#             #     print(abs(dist_y), player_true_y)
#             #     if self.attack_cooldown == 0:
#             #         self.state = 'ghost'
#             #         self.target_x = self.x_vel
#
#         else:
#             print('ghost')
#             if self.get_attack:
#                 self.state = 'hurt'
#             else:
#                 self.state = 'ghost'
#
#
#         # update animation
#         self.animate(dt=1 / 60)
#         self.rect.x = self.x_vel - offset_x
#
#     # def update_enemy(self, player: Player, offset_x):
#     #     # Calculate distance to player in world coordinates
#     #     player_true_x = player.rect.x
#     #     player_true_y = player.rect.y
#     #     dist_x = player_true_x - self.x_vel
#     #     dist_y = player_true_y - self.y_vel
#     #
#     #     if self.attack_cooldown > 0:
#     #         self.attack_cooldown -= 1
#     #
#     #     # if self.is_attacking:
#     #
#     #     #Only move if player is within attack range
#     #     if abs(dist_x) < self.attack_range and abs(dist_y) <= player_true_y:
#     #         self.state = 'ghost'
#     #
#     #         # Calculate desired distance (maintain 10px space)
#     #         if dist_x > 15:  # Player is to the right
#     #             if self.direction != 'right':
#     #                 self.direction = 'right'
#     #                 self.frames = self.reload_frames(flipped=False)
#     #                 # if self.x_vel <= self.target_x - self.retreat_distance:
#     #             # Move right but stop 10px before player
#     #             if dist_x - 4 > self.speed:
#     #                 self.x_vel += self.speed
#     #             else:
#     #                 self.x_vel = player_true_x - 20
#     #
#     #         elif dist_x < -15:  # Player is to the left
#     #             if self.direction != 'left':
#     #                 self.direction = 'left'
#     #                 self.frames = self.reload_frames(flipped=True)
#     #             # Move left but stop 10px before player
#     #             if abs(dist_x) - 4 > self.speed:
#     #                 self.x_vel -= self.speed
#     #             else:
#     #                 self.x_vel = player_true_x + 20
#     #
#     #         else:
#     #             # Within 10px range - don't move
#     #             self.state = 'ghost'
#     #     else:
#     #         self.state = 'ghost'
#     #
#     #     #Update animation
#     #     self.animate(dt=1 / 60)
#     #     # Update screen position
#     #     self.rect.x = self.x_vel - offset_x
#
#     def animate(self, dt):
#         self.frames_index += 7 * dt
#         if self.frames_index >= len(self.frames[self.state]):
#             self.frames_index = 0
#         self.image = self.frames[self.state][int(self.frames_index)]
#
#     def enemy_move_left(self, dx):
#         self.x_vel -= dx
#
#     def draw_enemy(self, screen, offset_x):
#         """ - offset_x make enemy not move follow screen."""
#         # screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))
#         screen.blit(self.image, (self.x_vel - offset_x, self.rect.y))
#
#     def health(self, bullet):
#         # self.state = 'hurt'
#         self.hp -= bullet
#         self.get_attack = True
#         self.hurt_timer = self.hurt_duration
#         # if self.hp <= 0:
#         #     self.alive = False
#
#
# class Enemy_2(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height):
#         super().__init__()
#         self.rect = pygame.Rect(x, y, width, height)
#         self.load_image()
#         self.state, self.frames_index = 'enemy_2', 0
#         self.image = self.frames[self.state][0]
#
#     def reload_frames(self, flipped=False):
#         frames = {state: [] for state in self.frame_paths.keys()}
#         # new_size = (self.rect.width * 2, self.rect.height* 2)
#         # new_size = (self.rect.width, self.rect.height)
#         new_size = (self.rect.width * 3, self.rect.height * 3)
#
#         for state, paths in self.frame_paths.items():
#             for path in paths:
#                 surf = pygame.image.load(path).convert_alpha()
#                 surf = pygame.transform.scale(surf, new_size)
#                 if flipped:
#                     surf = pygame.transform.flip(surf, True, False)
#                     """pygame.transform.flip(surf, True, False) mean flip picture from left to right"""
#                 frames[state].append(surf)
#
#         return frames
#
#     def load_image(self):
#         self.frames = {'attake': [], 'ghost': []}
#         self.frame_paths = {state: [] for state in self.frames.keys()}
#         # new_size = (self.rect.width * 2, self.rect.height * 2)
#         new_size = (self.rect.width * 3, self.rect.height * 3)
#         # new_size = (self.rect.width, self.rect.height)
#         for state in self.frames.keys():
#             for folder_path, sub_folder, file_names in walk(join('enemy', 'ghost_1', state)):
#                 if file_names:
#                     """skip .DS_Store or another file that nor be .png"""
#                     file_names = [f for f in file_names if f.endswith('.png')]
#                     """sort file"""
#                     file_names.sort(key=lambda x: int(x.split('.')[0]))
#                     for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
#                         full_path = join(folder_path, file_name)
#                         self.frame_paths[state].append(full_path)
#                         original_surf = pygame.image.load(full_path).convert_alpha()
#                         surf = pygame.transform.scale(original_surf, new_size)
#                         self.frames[state].append(surf)
#         print(self.frames)
#
#     def draw_enemy(self, screen):
#         screen.blit(self.image, (self.rect.x, self.rect.y))
#
#

class Game:
    block_size = 50
    width = 1000
    height = 800
    player_pos_x = block_size * (-17)
    player_pos_y = 790

    def __init__(self, player_name):
        self.player_name = player_name
        # self.clock = pygame.time.Clock()
        # self.all_sprites = pygame.sprite.Group()
        self.player = Player(self.player_pos_x, self.player_pos_y, 60, 60)

        self.enemies = pygame.sprite.Group()
        # enemy_1 = Enemy_1(700, self.height - self.block_size * 2, 50, 50)
        self.enemies.add(Enemy_1(700, self.height - self.block_size * 2, 50, 50),
                         Enemy_1(-400, self.height - self.block_size * 2, 50, 50),
                         Enemy_1(-900, self.height - (self.block_size * 12), 50, 50),
                         Enemy_1(100, self.height - (self.block_size * 9), 50, 50),
                         Enemy_1(800, self.height - (self.block_size * 12), 50, 50),
                         Enemy_1(1800, self.height - (self.block_size * 10), 50, 50))

        # self.enemy_1 = Enemy_1(700, self.height - self.block_size * 2, 50, 50)
        self.platform = Platform(self.width, self.height)
        # self.block = [Block(0, self.height - self.block_size, self.block_size)]
        self.floor = [Block(i * self.block_size, self.height - self.block_size, self.block_size)
                      for i in range(-self.width // self.block_size, (self.width * 2) // self.block_size)]
        self.wall_left = [Block(- self.width, i * self.block_size, self.block_size)
                     for i in range(-self.height // self.block_size, (self.height * 2) // self.block_size)]
        self.wall_right = [Block(self.width * 2, i * self.block_size, self.block_size)
                          for i in range(-self.height // self.block_size, (self.height * 2) // self.block_size)]

        self.offset_x = -(-self.player.rect.x + self.width // 2 - self.player.rect.width // 2)

        self.scroll_area_width = 200
        self.scroll_speed = 10
        # self.all_sprites = pygame.sprite.Group(self.player, self.enemy_1)
        # self.all_sprites = pygame.sprite.Group(self.player, self.enemies)
        # self.gun = Gun(self.player, self.all_sprites)
        # self.enemy = [Enemy_1(700, self.height - self.block_size * 3, 50, 50)]
        self.objs = pygame.sprite.Group([*self.floor,
                     *self.wall_left,
                     *self.wall_right,
                     Block(0, self.height - self.block_size * 2, self.block_size),
                     Block(self.block_size, self.height - self.block_size * 2, self.block_size),
                     Block(self.block_size * (-1), self.height - self.block_size * 2, self.block_size),

                     Block(self.block_size * 3, self.height - self.block_size * 4, self.block_size),
                     Block(self.block_size * 4, self.height - self.block_size * 4, self.block_size),
                     Block(self.block_size * 5, self.height - self.block_size * 4, self.block_size),
                     Block(self.block_size * 6, self.height - self.block_size * 5, self.block_size),
                     Block(self.block_size * 7, self.height - self.block_size * 5, self.block_size),

                     Block(self.block_size * 8, self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * 9, self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * 10, self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * 11, self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * 12, self.height - self.block_size * 9, self.block_size),

                     Block(self.block_size * 18, self.height - self.block_size * 5, self.block_size),
                     Block(self.block_size * 19, self.height - self.block_size * 5, self.block_size),
                     Block(self.block_size * 20, self.height - self.block_size * 5, self.block_size),
                     Block(self.block_size * 21, self.height - self.block_size * 5, self.block_size),
                     Block(self.block_size * 22, self.height - self.block_size * 5, self.block_size),

                     Block(self.block_size * 23, self.height - self.block_size * 7, self.block_size),
                     Block(self.block_size * 24, self.height - self.block_size * 7, self.block_size),
                     Block(self.block_size * 25, self.height - self.block_size * 7, self.block_size),
                     Block(self.block_size * 26, self.height - self.block_size * 7, self.block_size),
                     Block(self.block_size * 27, self.height - self.block_size * 7, self.block_size),
                     Block(self.block_size * 28, self.height - self.block_size * 7, self.block_size),

                     Block(self.block_size * 32, self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * 33, self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * 34, self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * 35, self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * 36, self.height - self.block_size * 9, self.block_size),

                     Block(self.block_size * 38, self.height - self.block_size * 7, self.block_size),
                     Block(self.block_size * 39, self.height - self.block_size * 7, self.block_size),

                     Block(self.block_size * (-4), self.height - self.block_size * 5, self.block_size),
                     Block(self.block_size * (-5), self.height - self.block_size * 5, self.block_size),
                     Block(self.block_size * (-6), self.height - self.block_size * 5, self.block_size),

                     Block(self.block_size * (-17), self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * (-18), self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * (-19), self.height - self.block_size * 11, self.block_size),

                     Block(self.block_size * (-7), self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * (-6), self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * (-5), self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * (-4), self.height - self.block_size * 11, self.block_size),

                     Block(self.block_size * 15, self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * 16, self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * 17, self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * 18, self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * 19, self.height - self.block_size * 11, self.block_size),
                     Block(self.block_size * 20, self.height - self.block_size * 11, self.block_size),

                     Block(self.block_size * (-8), self.height - self.block_size * 7, self.block_size),
                     Block(self.block_size * (-9), self.height - self.block_size * 7, self.block_size),
                     Block(self.block_size * (-10), self.height - self.block_size * 7, self.block_size),

                     Block(self.block_size * (-16), self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * (-15), self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * (-14), self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * (-13), self.height - self.block_size * 9, self.block_size),
                     Block(self.block_size * (-12), self.height - self.block_size * 9, self.block_size),

                     Block(0, self.height - self.block_size * 8, self.block_size),
                     Block(self.block_size, self.height - self.block_size * 8, self.block_size),
                     Block(self.block_size * 2, self.height - self.block_size * 8, self.block_size),
                     Block(self.block_size * 3, self.height - self.block_size * 8, self.block_size),])
        # self.block_size * (-19) before end map left

        self.all_sprites = pygame.sprite.Group(self.player, self.enemies, self.objs)

        self.health_bar = HealthBar(5, 40, 300, 15, 100)
        self.damage = 5

        self.name_font = pygame.font.SysFont('Arial', 24)

    def draw_player_name(self):
        """show name of player"""
        name_surface = self.name_font.render(f"Player: {self.player_name}", True, (255, 255, 255))
        screen.blit(name_surface, (5, 5))

    # def handle_check_collision(self, player, objects, dy):
    #     collided_object = []
    #     for obj in objects:
    #         if pygame.sprite.collide_mask(player, obj):
    #             if player.y_vel > 0:
    #                 player.rect.bottom = obj.rect.top
    #                 player.landed()
    #             if player.y_vel < 0:
    #                 player.rect.top = obj.rect.bottom
    #                 player.hit_head()
    #
    #             # if player.x_vel > 0:
    #             #     player.rect.right = obj.rect.left
    #             # elif player.x_vel < 0:
    #             #     player.rect.left = obj.rect.right
    #         collided_object.append(obj)
    #     return collided_object

    def move_and_check_collision(self, player, objects,dt):
        # Move and check X axis
        move_x = player.x_vel * dt * 60
        player.rect.x += move_x
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if player.x_vel > 1:
                    player.rect.right = obj.rect.left
                    player.x_vel = 0
                elif player.x_vel < 0:
                    player.rect.left = obj.rect.right
                    player.x_vel = 0
                player.x_vel = 0

        # Move and check Y axis
        move_y = player.y_vel * dt * 60
        player.rect.y += move_y
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if player.y_vel > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif player.y_vel < 0:
                    player.rect.top = obj.rect.bottom
                    player.hit_head()
                player.y_vel = 0
        self.player.update()

    def handle_check_collision_x(self, player, objects):
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if player.x_vel > 0:  # Moving right
                    player.rect.right = obj.rect.left
                elif player.x_vel < 0:  # Moving left
                    player.rect.left = obj.rect.right
                player.x_vel = 0
        self.player.update()

    def handle_check_collision_y(self, player, objects):
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if player.y_vel > 0:  # Falling
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif player.y_vel < 0:  # Jumping
                    player.rect.top = obj.rect.bottom
                    player.hit_head()
                player.y_vel = 0
        self.player.update()

    def collide(self, player, objects, dx):
        player.move(dx, 0)
        player.update()
        collided_obj = None
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                collided_obj = obj
                break

        player.move(-dx, 0)
        player.update()
        return collided_obj

    def start_game(self):
        # platform = Platform()
        """set the frame rate"""
        self.clock = pygame.time.Clock()
        self.background, self.bg_image = self.platform.get_background('black_imresizer.jpg')
        self.update()

    def check_bullet_collisions(self):
        # Check bullet collisions with blocks
        for bullet in self.player.bullets:
            for block in self.objs:
                if pygame.sprite.collide_mask(bullet, block):
                    print(f"Bullet hit block at {block.rect}")
                    bullet.kill()
                    break # Stop checking other blocks for this bullet

            for enemy in self.enemies:
                if pygame.sprite.collide_rect(bullet, enemy):
                    enemy.get_attack = True
                    # enemy.state = 'hurt'
                    print(f"Bullet hit enemy at {enemy.rect}")
                    bullet.kill()
                    enemy.health(self.damage)
                    # enemy.get_attack = False
                    if enemy.hp <= 0:
                        enemy.kill()
                    print(enemy.hp)


    def update(self):
        """Main game loop"""
        while True:
            """Convert to seconds"""
            dt = self.clock.tick(60) / 1000
            """pygame.event.get() เรียกใช้ในทุก frames ป้องการการค้าง"""
            """1. When the player presses a key, clicks the mouse, or closes the window → Pygame creates an event.
            2. These events are stored in the event queue (a list).
            3. pygame.event.get() takes all the events from the queue and allows you to handle them one by one."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.player.jump_count < 2:
                        self.player.jump()

                    if event.key == pygame.K_RETURN:
                        self.player.shoot()

            # Check keys every frame
            keys = pygame.key.get_pressed()
            player_speed = 10

            if keys[pygame.K_a]:
                self.player.move_left(player_speed)
            elif keys[pygame.K_d]:
                self.player.move_right(player_speed)
            else:
                self.player.stop()

            self.player.loop(60, dt)
            self.player.update()
            for enemy in self.enemies:
                enemy.offset_x = self.offset_x
                enemy.update_enemy(self.player, self.offset_x)

            self.player.bullets.update(dt, self.offset_x)
            # self.check_bullet_collisions()
            self.move_and_check_collision(self.player, self.objs, dt)

            self.player.animate(dt)
            self.check_bullet_collisions()
            self.platform.draw(screen, self.background, self.bg_image, self.player, self.objs, self.offset_x)
            self.player.bullets.draw(screen)

            for enemy in self.enemies:
                enemy.draw_enemy(screen, self.offset_x)

            """health bar"""
            self.health_bar.hp = self.player.hp
            self.health_bar.draw(screen)
            """draw name of player"""
            self.draw_player_name()

            if self.health_bar.hp <= 0:
                print('Player Dying')
                pygame.quit()

            if (self.player.rect.right - self.offset_x >= self.width - self.scroll_area_width
                and self.player.x_vel > 0) or (self.player.rect.left - self.offset_x <= self.scroll_area_width
                                               and self.player.x_vel < 0):
                self.offset_x += self.player.x_vel * dt * 60
                """dt * 60 beacues เพราะ dt = 1/60 ใน fps 60
                จะได้ความเร็วปกติเท่ากับค่าเดิม (x_vel = 10)"""

            if self.player.rect.top > self.height:
                self.player.die()
                print('game over')
                exit()

            pygame.display.update()
            """setup frames per second be 60"""
            self.clock.tick(60)


# if __name__ == "__main__":
#     game = Game()
#     game.start_game()

# if __name__ == "__main__":
#     # สร้างหน้าเริ่มเกมและรับชื่อผู้เล่น
#     start_screen = StartScreen()
#     player_name = start_screen.display()  # รับชื่อผู้เล่นจากหน้าเริ่มเกม
#
#     # เริ่มเกมด้วยชื่อผู้เล่น
#     game = Game(player_name)
#     game.start_game()
