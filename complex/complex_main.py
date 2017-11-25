import os
from random import randint

import pygame

from player import Player
from players import Players
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

# Load and set up graphics.
background_image_orig = load_image("minimaps/albasrah_minimap.gif")
background_image = pygame.transform.scale(background_image_orig, (WINDOW_WIDTH, WINDOW_HEIGHT))
player_images = load_images("misc/player_blue.gif", "misc/player_green.gif", "misc/player_gray.gif")
player_images = [pygame.transform.scale(img, (30, 30))
                 for img in player_images]
player_images_shoot = load_images("misc/player_blue_shoot.gif", "misc/player_green_shoot.gif", "misc/player_gray_shoot.gif")
player_images_shoot = [pygame.transform.scale(img, (30, 30))
                       for img in player_images_shoot]

player_group = pygame.sprite.Group()
all_group = pygame.sprite.RenderUpdates()
Player.containers = all_group

players = Players()
for i in range(10):
    players.add_player()

done = False

orientation = 0
position = (500, 500)
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

    dirty = all_group.draw(screen)
    pygame.display.update(dirty)

    clock.tick(FPS)

pygame.quit()