import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed=15):
        super().__init__()
        # Make bullet more visible
        self.image = pygame.Surface((20, 5))  # Wider bullet
        self.image.fill(((0, 255, 255)))  # Bright yellow color
        pygame.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), 1)  # Red border
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.direction = direction
        self.lifetime = 90  # Longer lifetime
        self.true_x = x  # Store absolute position for scrolling
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt, offset_x=0):
        move_distance = self.speed * dt * 60

        if self.direction == 'right':
            self.true_x += move_distance
        else:
            self.true_x -= move_distance

        self.rect.x = self.true_x - offset_x

        # Remove old bullets
        # self.lifetime -= 1
        # if self.lifetime <= 0:
        #     self.kill()