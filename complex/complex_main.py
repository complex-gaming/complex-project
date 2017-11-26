from random import randint
import csv

import pygame

from game_map import GameMap
from game_ticks import GameTicks
from player import Player
from flag import Flag
from players import Players
from flags import Flags
from shooting_events import ShootingEvents

# Define some colors
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
FPS = 60


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# This sets the name of the window
pygame.display.set_caption('Complex GUI')

clock = pygame.time.Clock()

# Set positions of graphics
background_position = [0, 0]

player_group = pygame.sprite.Group()
all_group = pygame.sprite.RenderUpdates()
Player.containers = all_group
Flag.containers = all_group

game_map = GameMap()
game_map.load_map("Fools_Road_AAS_V1")
background_image = game_map.scaled_map_image

game_ticks = GameTicks("../junction-gaming/matches/37549105/sorted_ticks.csv")
game_ticks.set_index(0)

players = Players(game_map)
flags = Flags(game_map)

with open("resources/csv/flags.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['x'], row['y'], row['team_id'])
        flags.add_flag(float(row['x']), float(row['y']), int(row['team_id']))

# load flags
#for i in range(10):
#    players.add_player()

shooting_events = ShootingEvents("../junction-gaming/matches/37549105/sorted_damage_dealt.csv", screen, game_map.map_corners)

done = False
players_init = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # clear screen
    all_group.clear(screen, background_image)

#    if not players_init:
#        for i in range(10):
#            players.add_player()
#        players_init = True

    try:
        data, timestamp = game_ticks.get_next_tick_data()
    except:
        done = True

    # move players
    players.update_data(data, timestamp)

    # update all
    all_group.update()

    # Copy image to screen:
    screen.blit(background_image, background_position)

    # update shooting events
    screen.lock()
    shootings = shooting_events.create_shooting_events(timestamp)
    screen.unlock()

    dirty = all_group.draw(screen)
    pygame.display.update(dirty)

    clock.tick(FPS)

pygame.quit()
