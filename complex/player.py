import pygame

from random import randint


class Player(pygame.sprite.Sprite):
    containers = None

    def __init__(self, id, position, orientation, image_normal, image_shoot):
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

    def update(self):
        if not self.shooting:
            self.image = self.rot_center(self.image_normal_clean, self.orientation)
        else:
            self.image = self.rot_center(self.image_shoot_clean, self.orientation)
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def set_position_and_orientation(self, position, orientation):
        self.position = position
        self.orientation = orientation

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


