import pygame

from random import randint
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900


class Player(pygame.sprite.Sprite):
    containers = None

    def __init__(self, id, position, orientation, image_normal, image_shoot, map_corners, team_number):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.id = id
        self.position = position
        self.orientation = orientation
        self.image = pygame.transform.rotate(image_normal, orientation)
        self.image_normal_clean = image_normal.copy()
        self.image_shoot_clean = image_shoot.copy()
        self.rect = self.image.get_rect()
        self.orientation = orientation
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.shooting = False
        self.map_corners = map_corners
        self.calculate_map_limits()
        self.team_number = team_number

    def update(self):
        if not self.shooting:
            self.image = self.rot_center(self.image_normal_clean, self.orientation)
        else:
            self.image = self.rot_center(self.image_shoot_clean, self.orientation)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.scale_position(self.position)

    def scale_position(self, pos):
        x = (pos[0] - self.min_x)/(self.max_x - self.min_x) * WINDOW_WIDTH
        y = (pos[1] - self.min_y)/(self.max_y - self.min_y) * WINDOW_HEIGHT
        return x, y

    def calculate_map_limits(self):
        c = self.map_corners
        self.min_x = min(c[0][0], c[1][0])
        self.max_x = max(c[0][0], c[1][0])
        self.min_y = min(c[0][1], c[1][1])
        self.max_y = max(c[0][1], c[1][1])


    def set_position_and_orientation(self, data):
        self.position = data[0:2]
        self.orientation = data[2]

    def set_shoot_status(self, status):
        self.shooting = status

    @staticmethod
    def rot_center(image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image


