import tkinter as tk

from PIL import ImageTk, Image
from random import randint

CANVAS_WIDTH = 1400
CANVAS_HEIGHT = 900

PLAYER_SIZE = 30


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.draw_area = None
        self.original_background_image = None
        self.scaled_background_image = None  # Need a reference to prevent garbage collection
        self.background_image = None

        self.player_images = None

        self.create_widgets()

    def create_widgets(self):
        self.draw_area = tk.Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.draw_area.pack()

        self.load_player_images()

    def load_player_images(self):
        self.player_images = dict()
        gray = Image.open("resources/misc/player_gray.gif")
        blue = Image.open("resources/misc/player_blue.gif")
        green = Image.open("resources/misc/player_green.gif")

        [img.thumbnail((PLAYER_SIZE, PLAYER_SIZE), Image.ANTIALIAS) for img in [gray, blue, green]]

        self.player_images["gray"] = ImageTk.PhotoImage(gray)
        self.player_images["blue"] = ImageTk.PhotoImage(blue)
        self.player_images["green"] = ImageTk.PhotoImage(green)

    def create_players(self, player_positions):
        player_num = 0
        for position in player_positions:
            self.draw_area.create_image(position[0], position[1], image=self.player_images["gray"],
                                        anchor=tk.NW, tags=str(player_num))
            player_num += 1

    def move_players(self, event=None):
        for i in range(50):
            self.draw_area.move(str(i), randint(-5, 5), randint(-5, 5))
        self.draw_area.after(100, self.move_players)

    def load_map(self, map_file):
        self.original_background_image = Image.open(map_file)
        self.scaled_background_image = self.original_background_image.copy()
        self.scaled_background_image.thumbnail((CANVAS_WIDTH, CANVAS_HEIGHT), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(self.scaled_background_image)
        self.draw_area.create_image(0, 0, image=self.background_image, anchor=tk.NW)
