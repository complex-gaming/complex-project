import pygame

from random import randint
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900


class Flag(pygame.sprite.Sprite):
    containers = None

    def __init__(self, position, image, map_corners):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.position = position
        self.image = image
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.map_corners = map_corners
        self.calculate_map_limits()

        self.rect.x, self.rect.y = self.scale_position()


    def scale_position(self):
        pos = self.position
        x = (pos[0] - self.min_x)/(self.max_x - self.min_x) * WINDOW_WIDTH
        y = (pos[1] - self.min_y)/(self.max_y - self.min_y) * WINDOW_HEIGHT
        return x, y

    def calculate_map_limits(self):
        c = self.map_corners
        self.min_x = min(c[0][0], c[1][0])
        self.max_x = max(c[0][0], c[1][0])
        self.min_y = min(c[0][1], c[1][1])
        self.max_y = max(c[0][1], c[1][1])

