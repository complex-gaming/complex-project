import csv
import os
import pygame

from utils import load_image


MINIMAPS = dict(Fools_Road="Fools_Road_v1_Minimap.gif",
                Chora="Chora1_Minimap.gif",
                Gorodok="gorodok_minimap.gif")


class GameMap:
    def __init__(self):
        self.all_map_corners = dict()

        self.original_map_image = None
        self.scaled_map_image = None


        with open("resources/csv/all_corners.csv", 'r') as f:
            reader = csv.DictReader(f, delimiter=',')

            for row in reader:
                self.all_map_corners[row["names"]] = ((row["Corner0_x"], row["Corner0_y"]),
                                                      (row["Corner1_x"], row["Corner1_y"]))

    def load_map(self, map_name):
        for key in MINIMAPS:
            if map_name.startswith(key):
                self.original_map_image = load_image(os.path.join("minimaps", MINIMAPS[key]))
                self.scaled_map_image = pygame.transform.scale(self.original_map_image, (900, 900))




