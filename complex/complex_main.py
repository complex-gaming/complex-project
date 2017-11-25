import os
from random import randint

import pygame

from game_map import GameMap
from player import Player
from players import Players
from shooting_event import ShootingEvent
from utils import load_images, load_image

# Define some colors
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
FPS = 10


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# This sets the name of the window
pygame.display.set_caption('CMSC 150 is cool')

clock = pygame.time.Clock()

# Before the loop, load the sounds:

# Set positions of graphics
background_position = [0, 0]

player_group = pygame.sprite.Group()
all_group = pygame.sprite.RenderUpdates()
Player.containers = all_group

players = Players()
for i in range(10):
    players.add_player()

done = False

game_map = GameMap()
game_map.load_map("Fools_Road")
background_image = game_map.scaled_map_image

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # clear screen
    all_group.clear(screen, background_image)

    # move players
    players.move_players()


    # update all
    all_group.update()

    # Copy image to screen:
    screen.blit(background_image, background_position)

    # update shooting events
    screen.lock()
    shooting_events = [ShootingEvent(screen, (randint(0, 900), randint(0, 900)), (randint(0, 900), randint(0, 900)))]
    screen.unlock()

    dirty = all_group.draw(screen)
    pygame.display.update(dirty)

    clock.tick(FPS)

pygame.quit()