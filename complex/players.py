import pygame
from random import randint

from player import Player

from utils import load_images


class Players:
    def __init__(self, game_map):
        self.players = dict()
        self.next_id = 0
        player_images = load_images("misc/player_blue.gif", "misc/player_green.gif",
                                    "misc/player_gray.gif")
        self.player_images = [pygame.transform.scale(img, (30, 30))
                              for img in player_images]
        player_images_shoot = load_images("misc/player_blue_shoot.gif",
                                          "misc/player_green_shoot.gif",
                                          "misc/player_gray_shoot.gif")
        self.player_images_shoot = [pygame.transform.scale(img, (30, 30))
                                    for img in player_images_shoot]
        self.game_map = game_map

    def add_player(self, id):
        position = (randint(0, 900), randint(0, 900))
        rotation = randint(0, 360)
        player = Player(id, position, rotation, self.player_images[0], self.player_images_shoot[0],
                        self.game_map.map_corners)
        self.players[id] = player

    def move_player(self, id, data):
        player = self.players[id]
        player.set_position_and_orientation(data)
        if randint(0, 9) == 5:
            player.shooting = True
        else:
            player.shooting = False

    def update_data(self, tick_data):
        for key in tick_data:
            if key not in self.players:
                self.add_player(key)
            self.move_player(key, tick_data[key])

    def _get_id(self):
        yield self.next_id
        self.next_id += 1
