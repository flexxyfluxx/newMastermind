# GUI class:
# Manages the GUI that the User interfaces with.
# Based on TKInter.

from tkinter import *

COLORS = (
    "#000000",   # Black
    "#ffffff",   # White
    "#ff0000",   # Red
    "#00ff00",   # Green
    "#0000ff",   # Blue
    "#ffdd00"    # Yellow (slightly more "banana"-y for better visibility)
    )

class MainWindow(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        # Define window dimensions:
        self.height = 720
        self.width = 720

        # Create widgets:

        # --- LEFT SIDE ---

        self.history_frame = Frame(
            self,
            height = 600,
            width = 360,
            bd = 1
            ).place(x = 0, y = 120)

        # --- END OF LEFT SIDE


        # --- RIGHT SIDE ---

        # Staged sequence:
        self.staged_sequence = Frame(
            self,
            height = 80,
            width = 360,
            bd = 8
        ).place(x = 360, y = 0)

        # Create staged sequence segments
        self.staged_sequence_cells = []
        for c in range(4):
            self.staged_sequence_cells += [
                Frame(
                    self.staged_sequence,
                    height = 80,
                    width = 90,
                    bg = COLORS[3],
                    bd = 8,
                    relief = RIDGE
                ).place(x = 90 * c + 360, y = 0)
            ]
        
        # Button panel:
        
        self.color_selector_panel = Frame(
            self,
            height = 480,
            width = 360
            ).place(x = 360, y = 80)

        # Create buttons in grid
        self.color_selector_panel_frame_grid = [[],[],[],[]]
        self.color_selector_panel_button_grid = [[],[],[],[]]
        for c in range(4):
            for z in range(6):
                self.color_selector_panel_frame_grid[c] += [
                    Frame(
                        self.color_selector_panel,
                        height = 80,
                        width = 90,
                        bg = COLORS[z],         # placeholder
                        bd = 4,
                        cursor = "hand1",
                        relief = GROOVE
                    ).place(x = 90 * c + 360, y = 80 * z + 80)
                ]
                self.color_selector_panel_button_grid += [
                    Button()
                ]
        
        # Submit button:
        self.submit_button = Frame(
            self.color_selector_panel,
            height = 80,
            width = 180,
            relief = GROOVE,
            bd = 8,
            cursor = "hand1",
            bg = "Black",
        ).place(x = 360, y = 560)

        # --- END OF RIGHT SIDE ---

# some tests lol
if __name__ == "__main__":
    window = MainWindow()
    window.master.title("Testing 123")
    window.mainloop()
