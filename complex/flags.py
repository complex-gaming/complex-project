import pygame
from random import randint

from flag import Flag

from utils import load_images


class Flags:
    def __init__(self, game_map):
        self.flags = []
        flag_images = load_images("misc/flag_grey.gif", "misc/flag_blue.gif",
                "misc/flag_red.gif")
        self.images = [pygame.transform.scale(img, (40, 40))
                for img in flag_images]
        self.game_map = game_map

    def add_flag(self, x, y, owner):
        image = self.images[owner]
        position = (x, y)
        flag = Flag(position, image, self.game_map.map_corners)
        flag.scale_position()
        self.flags.append(flag)
