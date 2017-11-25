import csv
import math

# PLAYER DATA MODEL
# pos_x, pos_y, rotation
TIMESTAMP = 3
PLAYER_ID = 4
POS_X = 5
POS_Y = 6
ROT_X = 8
ROT_Y = 9


class GameTicks:
    def __init__(self, ticks_file):
        self.ticks_file = ticks_file

    def next_tick_data(self):
        with open(self.ticks_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            current_timestamp = 0

            player_data = dict()
            for row in reader:
                timestamp = row[TIMESTAMP]
                if current_timestamp == 0:
                    current_timestamp = timestamp
                if timestamp > current_timestamp:
                    yield player_data
                current_timestamp = timestamp
                player_data[int(row[PLAYER_ID])] = (float(row[POS_X]), float(row[POS_Y]),
                                                    math.atan2(float(row[ROT_Y]), float(row[ROT_X])))

