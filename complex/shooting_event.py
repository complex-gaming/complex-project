import pygame


class ShootingEvent:
    def __init__(self, surface, start, end):
        pygame.draw.line(surface, pygame.Color(255, 0, 0), start, end)
