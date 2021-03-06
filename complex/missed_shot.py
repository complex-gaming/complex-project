import pygame
import math

SHOT_LENGTH = 50
ADJUSTMENT = 180


class MissedShot:
    def __init__(self, surface, start, rotation):
        rotation = - rotation + ADJUSTMENT
        x = start[0] + math.cos(math.radians(rotation)) * SHOT_LENGTH
        y = start[1] + math.sin(math.radians(rotation)) * SHOT_LENGTH
        pygame.draw.line(surface, pygame.Color(0, 255, 0), start, (x, y))
