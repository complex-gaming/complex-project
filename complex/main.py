from random import randint

import tkinter as tk

from complex.application import Application
import os
from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900


def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
    root.title("Complex GUI")
    app = Application(master=root)

    app.load_map("resources/minimaps/albasrah_minimap.gif")

    # Move to foreground
    running_app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
    running_app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)
    positions = get_player_positions()
    app.create_players(positions)
    app.move_players()

    app.mainloop()


def get_player_positions():
    return [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for a in range(50)]


if __name__ == "__main__":
    main()