import pygame
from random import randint

from player import Player

from utils import load_images

TIMESTAMP_THRESHOLD = 5000


class Players:
    def __init__(self, game_map):
        self.players = dict()
        self.player_updated = dict()
        self.next_id = 0
        player_images = load_images("misc/team_blue.gif", "misc/team_red.gif",
                                    "misc/player_gray.gif")
        self.player_images = [pygame.transform.scale(img, (20, 20))
                              for img in player_images]
        player_images_shoot = load_images("misc/player_blue_shoot.gif",
                                          "misc/player_green_shoot.gif",
                                          "misc/player_gray_shoot.gif")
        self.player_images_shoot = [pygame.transform.scale(img, (20, 20))
                                    for img in player_images_shoot]
        self.game_map = game_map

    def add_player(self, id, data, timestamp):
        position = data[0:2]
        rotation = data[2]

        if position[0] < 20000:
            team_number = 2
        else:
            team_number = 1

        player = Player(id, position, rotation, self.player_images[team_number - 1], self.player_images_shoot[0],
                        self.game_map.map_corners, team_number)
        if id in self.players and self.players[id] is not None:
            self.players[id].kill()
        self.players[id] = player
        self.player_updated[id] = timestamp

    def move_player(self, id, data, timestamp):
        player = self.players[id]
        player.set_position_and_orientation(data)
        self.player_updated[id] = timestamp
#        if randint(0, 100) == 5:
#            player.shooting = True
#        else:
#            player.shooting = False

    def update_data(self, tick_data, timestamp):
        for key in tick_data:
            if key not in self.players:
                self.add_player(key, tick_data[key], timestamp)
            self.move_player(key, tick_data[key], timestamp)

        for key in self.player_updated:
            if self.player_updated[key] and timestamp - self.player_updated[key] > TIMESTAMP_THRESHOLD:
                if self.players[key] is not None:
                    self.players[key].kill()
                self.players[key] = None
                self.player_updated[key] = None

    def _get_id(self):
        yield self.next_id
        self.next_id += 1
