import csv
import math

from missed_shot import MissedShot

TIMESTAMP = 3
POS_X = 5
POS_Y = 6
ROT_X = 8
ROT_Y = 9

SHOOTING_EVENT_WINDOW = 5000
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900


class MissedShots:
    def __init__(self, shots_file, screen, map_corners):
        self.shots_file = shots_file
        self.missed_shots = dict()
        self.current_index = 0
        self._read_shooting_data()
        self.screen = screen
        self.map_corners = map_corners
        self.calculate_map_limits()

    def _read_shooting_data(self):
        with open(self.shots_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                timestamp = int(row[TIMESTAMP])
                if not timestamp in self.missed_shots:
                    self.missed_shots[timestamp] = []
                shooting_data = (float(row[POS_X]), float(row[POS_Y]),
                                 math.degrees(math.atan2(float(row[ROT_Y]), float(row[ROT_X]))))
                self.missed_shots[timestamp].append(shooting_data)
                print("{}".format(shooting_data))

    def calculate_map_limits(self):
        c = self.map_corners
        self.min_x = min(c[0][0], c[1][0])
        self.max_x = max(c[0][0], c[1][0])
        self.min_y = min(c[0][1], c[1][1])
        self.max_y = max(c[0][1], c[1][1])

    def scale_position(self, pos):
        x = (pos[0] - self.min_x)/(self.max_x - self.min_x) * WINDOW_WIDTH
        y = (pos[1] - self.min_y)/(self.max_y - self.min_y) * WINDOW_HEIGHT
        return x, y

    def create_shooting_events(self, timestamp):
        events = []
        for key in self.missed_shots:
            if key in range(timestamp, timestamp + SHOOTING_EVENT_WINDOW):
                for missed_shot in self.missed_shots[key]:
                    pos = self.scale_position((missed_shot[0], missed_shot[1]))
                    rot = missed_shot[1]

                    events.append(MissedShot(self.screen, pos, rot))
        return events
