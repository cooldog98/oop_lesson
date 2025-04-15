import pygame
from os.path import isfile, join


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, _screen, offset_x):
        _screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = self.get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def get_block(self, size, folder='graphic', picture='walland green.jpg'):
        path = join(folder, picture)
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(0, 0, size, size)
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale(surface, (size, size))


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
