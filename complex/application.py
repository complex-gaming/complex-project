import tkinter as tk

from PIL import ImageTk, Image

CANVAS_WIDTH = 1400
CANVAS_HEIGHT = 900


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.draw_area = None

        self.create_widgets()

    def create_widgets(self):
        self.draw_area = tk.Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.draw_area.pack()

    def load_map(self, map_file):
        self.original_background_image = (Image.open(map_file))
        self.scaled_background_image = self.original_background_image.copy()
        self.scaled_background_image.thumbnail((CANVAS_WIDTH, CANVAS_HEIGHT), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(self.scaled_background_image)
        self.draw_area.create_image(0, 0, image=self.background_image, anchor=tk.NW)
