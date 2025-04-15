import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
max_health = 100
health = 20
ratio = health / max_health

pygame.display.set_caption('Health bar')


class HealthBar:
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surf):
        """calculate health ratio"""
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, 'red', (self.x, self.y, self.w, self.h))
        pygame.draw.rect(screen, 'green', (self.x, self.y, self.w * ratio, self.h))

    # def health_player(self, damage):
    #     self.hp -= damage
