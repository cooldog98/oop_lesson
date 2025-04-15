
import os
import pygame


class Platform:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_background(self, name):
        path = os.path.join('graphic', name)  # Join the file path correctly
        """os.path.join('assets', 'Background', 'back_G_help.jpg') assets โฟร์เ้อใหญ่สุดที่ ไฟล์รูปภาพเก็บไว้
        Background โฟเด้อรองลงมา back_G_help.jpg ไฟล์รูปภาพ or 'graphic', name: graphic is bigger folder that
         keep file picture, name is file picture """
        image = pygame.image.load(path)
        __, __, width_image, height_image = image.get_rect()
        tiles = []

        for i in range(self.width // width_image + 1):
            for j in range(self.height//height_image + 1):
                pos = [i * width_image, j * height_image]
                tiles.append(pos)

        return tiles, image

    def draw(self, screen_, background, bg_image, player, objects, offset_x):
        for tile in background:
            screen_.blit(bg_image, tuple(tile))

        for obj in objects:
            obj.draw(screen_, offset_x)

        player.draw_player(screen_, offset_x)