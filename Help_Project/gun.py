import pygame
# from player import Player

class Bullet(pygame.sprite.Sprite):
    block_size = 50
    width = 1000
    player_pos_x = block_size * (-19)
    player_pos_y = 790
    def __init__(self, x, y, speed=10):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))  # red bullet
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.player = Player(self.player_pos_x, self.player_pos_y, 60, 60)
        self.offset_x = -(-self.player.rect.x + self.width // 2 - self.player.rect.width // 2)
        self.true_x = x
        self.true_y = y

    def update(self):
        self.rect.y -= self.speed  # move up
        self.rect.center = (self.true_x - self.offset_x, self.true_y)

        self.rect.x -= self.offset_x
        if self.rect.bottom < 0:
            self.kill()
