import pygame


class GameTimer():
    def __init__(self, surface, start):
        self.surface = surface
        self.start = start
        pygame.font.init()
        self.font = pygame.font.Font("resources/fonts/meslo.ttf", 30)

    def update(self, current):
        text_surface = self.font.render(self.get_time_string(current), False, (200, 200, 200))
        self.surface.blit(text_surface, (0, 0))

    def get_time_string(self, current):
        millis = current - self.start
        seconds = (millis / 1000) % 60
        seconds = int(seconds)
        minutes = (millis / (1000 * 60)) % 60
        minutes = int(minutes)
        hours = (millis / (1000 * 60 * 60)) % 24
        hours = int(hours)
        return "{:02d}h:{:02d}m:{:02d}s".format(hours, minutes, seconds)
