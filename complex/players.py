import pygame
from random import randint

from player import Player

from utils import load_images


class Players:
    def __init__(self):
        self.players = []
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

    def add_player(self):
        position = (randint(0, 900), randint(0, 900))
        rotation = randint(0, 360)
        player = Player(self._get_id(), position, rotation, self.player_images[0], self.player_images_shoot[0])
        self.players.append(player)

    def move_players(self):
        for player in self.players:
            player.position = (player.position[0] + randint(-1, 1), player.position[1] + randint(-1, 1))
            player.orientation += randint(-30, 30)
            if randint(0, 9) == 5:
                player.shooting = True
            else:
                player.shooting = False


    def _get_id(self):
        yield self.next_id
        self.next_id += 1
