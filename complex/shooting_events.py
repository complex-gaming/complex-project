import csv

from shooting_event import ShootingEvent

TIMESTAMP = 4
VICTIM_POS_X = 5
VICTIM_POS_Y = 6
ATTACKER_POS_X = 11
ATTACKER_POS_Y = 12

SHOOTING_EVENT_WINDOW = 5000

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900


class ShootingEvents:
    def __init__(self, shootings_file, screen, map_corners):
        self.shootings_file = shootings_file
        self.shooting_data = dict()
        self.screen = screen
        self.map_corners = map_corners

        self.read_shooting_data()
        self.calculate_map_limits()

    def read_shooting_data(self):
        with open(self.shootings_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            next(reader)
            for row in reader:
                timestamp = int(row[TIMESTAMP])
                if not timestamp in self.shooting_data:
                    self.shooting_data[timestamp] = []
                shooting_data = ((float(row[ATTACKER_POS_X]), float(row[ATTACKER_POS_Y])),
                                 (float((row[VICTIM_POS_X])), float(row[VICTIM_POS_Y])))
                self.shooting_data[timestamp].append(shooting_data)
                print("Attacker {} Victim {}".format(shooting_data[0], shooting_data[1]))

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
        for key in self.shooting_data:
            if key in range(timestamp, timestamp + SHOOTING_EVENT_WINDOW):
                for shooting in self.shooting_data[key]:
                    attacker_pos = self.scale_position(shooting[0])
                    victim_pos = self.scale_position(shooting[1])

                    events.append(ShootingEvent(self.screen, attacker_pos, victim_pos))
        return events



