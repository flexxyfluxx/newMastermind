# GUI class:
# Manages the GUI that the User interfaces with.
# Based on TKInter.

from tkinter import *
from Round import *
from Game import *
from handydandies import *




class MainWindow(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        # Define window dimensions and grid:
        self.master.geometry("720x720")
        self.master.resizable(width = 0, height = 0)

        self._selected_data = [None, None, None, None]

        # make button functions
        """
        self._btn_funcs = [ [], [], [], [] ]
        for c in range(4):
            for z in range(6):
                self._btn_funcs[c] += [self._make_button_func(c, z)]
        """

        #self.colorselect_pressed = None
        #self.submit_pressed = None

        self._create_widgets()
        self._place_widgets()
        print("Game window created.")
    
    """
    def _make_button_func(self, c, z):
        return lambda: self.colorselect_pressed(clid = c, new = z)
    """


    def _create_left(self):
        self.left_side = Frame(
            self.master
        )

        self.hiddentarget = Frame(
            self.left_side,
            bg = "#000000"
        )
        self.hiddentarget_cells = []
        for c in range(4):
            self.hiddentarget_cells += [
                Frame(
                    self.hiddentarget,
                    bg = "#000000",
                    relief = SUNKEN,
                    bd = 12
                )
            ]
        

        self.hiddentarget_colors = []
        self.hiddentarget_labels = []
        for c in range(4):
            self.hiddentarget_colors += [
                Frame(
                    self.hiddentarget,
                    bg = COLORS[3] #placeholder
                )
            ]
            self.hiddentarget_labels += [
                Label(
                    self.hiddentarget,
                    text = "?",
                    font = ("Helvetica", 48, "bold"),
                    height = 1,
                    width = 1,
                    bg = "#000000",
                    fg = "#ffffff"
                )
            ]

        self.history = Frame(
            self.left_side,
        )
        self.history_cells = [ [],[],[],[],[],[],[],[],[],[] ]
        self.history_colors = [ [],[],[],[],[],[],[],[],[],[] ]
        self.history_feedback_cells = []
        self.history_feedback_labels = [ [],[],[],[],[],[],[],[],[],[] ]
        for c in range(10):
            for z in range(4):
                self.history_cells[c] += [
                    Frame(
                        self.history,
                        relief = SUNKEN,
                        bg = "#000000",
                        bd = 8
                    )
                ]
                self.history_colors[c] += [
                    Frame(
                        self.history,
                        bg = "#444444"
                    )
                ]

            self.history_feedback_cells += [
                Frame(
                    self.history,
                    relief = RIDGE,
                    bg = "#000000",
                    bd = 8,
                )
            ]
            self.history_feedback_labels[c] += [
                Label(
                    self.history,
                    text = "!",
                    font = ("Helvetica", 28),
                    fg = "#00ff00",
                    bg = "#555555",
                    width = 1,
                    height = 1
                ),
                Label(
                    self.history,
                    text = "!",
                    font = ("Helvetica", 28),
                    fg = "#ff0000",
                    bg = "#555555",
                    width = 1,
                    height = 1
                )
            ]

    def _create_right(self):
        self.right_side = Frame(
            self.master,
            bg = "#000000"
        )

        self.staged_guess = Frame(
            self.right_side,
            bg = "#000000",
            bd = 12,
            relief = SUNKEN
        )
        self.staged_guess_cells = []
        self.staged_guess_colors = []
        for c in range(4):

            
            self.staged_guess_cells += [
                Frame(
                    self.right_side,
                    bg = "#000000",
                    bd = 8,
                    relief = RIDGE,
                )
            ]
            
            self.staged_guess_colors += [
                Frame(
                    self.right_side,
                    bg = DEFAULTCOLOR
                )
            ]
        
        self.button_panels = []
        for c in range(4):
            self.button_panels += [
                Frame(
                    self.right_side,
                    bg = "#000000",
                    bd = 8,
                    relief = SUNKEN,
                    command = None
                )
            ]
        

        self.color_buttons = [ [],[],[],[] ]
        for c in range(4):
            for z in range(6):
                self.color_buttons[c] += [
                    Button(
                        self.right_side,
                        bg = COLORS[z],
                        height = 2,
                        width = 5,
                        bd = 8,
                        command = None
                    )
                ]
        
        self.submit_button_frame = Frame(
            self.right_side,
            bg = "#000000",
            bd = 8,
            relief = SUNKEN
        )
        self.submit_button = Button(
            self.right_side,
            bg = "#00ffff",
            bd = 8,
            relief = RAISED,
            height = 1,
            width = 10,
            text = "SUBMIT",
            font = ("Helvetica", 12, "bold"),
            command = lambda: self.submit_pressed()
        )

        self.credits = Label(
            self.right_side,
            relief = FLAT,
            bg = "#000000",
            fg = "#ff0000",
            font = ("Times New Roman", 32, "bold"),
            text = "by flÿˣˣ",
            height = 1
        )
        self.logo = Label(
            self.right_side,
            relief = SUNKEN,
            bg = "#000000",
            fg = "#ffffff",
            bd = 8,
            text = "MASTERmind",
            font = ("Bauhaus", 38, "bold"),
            height = 1
        )

    def _place_left(self):
        self.left_side.grid(row = 0, column = 0, sticky = NSEW)
        
        # set up left side grid
        self.left_side.rowconfigure(0, weight = 1)
        self.left_side.rowconfigure(1, weight = 5)
        self.left_side.columnconfigure(0, weight = 1)


        # set up hiddentarget area
        self.hiddentarget.grid(row = 0, column = 0, sticky = NSEW)
        self.hiddentarget.rowconfigure(0, weight = 1)
        for c in range(4):
            self.hiddentarget.columnconfigure(c, weight = 1)

        # spawn hiddentarget cells
        self.hiddentarget.grid_propagate(0) # To prevent the Label from abnormally resizing the grid structure.
        for c in range(4):
            self.hiddentarget_cells[c].grid(row = 0, column = c, sticky = NSEW)
            self.hiddentarget_cells[c].rowconfigure(0, weight = 1)
            self.hiddentarget_cells[c].columnconfigure(0, weight = 1)
            self.hiddentarget_colors[c].grid(in_ = self.hiddentarget_cells[c], row = 0, column = 0, sticky = NSEW)
            self.hiddentarget_labels[c].grid(in_ = self.hiddentarget_cells[c], row = 0, column = 0, sticky = NSEW)


        # set up history area
        self.history.grid(row = 1, column = 0, sticky = NSEW)
        for c in range(10):
            self.history.rowconfigure(c, weight = 1)
        for c in range(5):
            self.history.columnconfigure(c, weight = 1)
        
        # spawn history sequence cells
        for c in range(10):
            for z in range(4):
                t_row = 9 - c # First round is at the bottom, thus it makes sense to go bottom-up
                self.history_cells[c][z].grid(row = t_row, column = z, sticky = NSEW)
                self.history_cells[c][z].rowconfigure(0, weight = 1)
                self.history_cells[c][z].columnconfigure(0, weight = 1)
                self.history_colors[c][z].grid(in_ = self.history_cells[c][z], row = 0, column = 0, sticky = NSEW)
        
        # spawn and setup feedback cells
        for c in range(10):
            t_row = 9 - c
            self.history_feedback_cells[c].grid(row = t_row, column = 4, sticky = NSEW)
            self.history_feedback_cells[c].rowconfigure(0, weight = 1)
            self.history_feedback_cells[c].columnconfigure(0, weight = 1)
            self.history_feedback_cells[c].columnconfigure(1, weight = 1)
            self.history.grid_propagate(0)

        # spawn feedback labels
        for c in range(10):
            t_row = 9 - c
            for z in range(2):
                self.history_feedback_labels[c][z].grid(in_ = self.history_feedback_cells[c], row = 0, column = z, sticky = NSEW)

    def _place_right(self):
        self.right_side.grid(row = 0, column = 1, sticky = NSEW)

        # set up right side grid
        for c in range(9):
            self.right_side.rowconfigure(c, weight = 1)
        for c in range(4):
            self.right_side.columnconfigure(c, weight = 1)
        
        # spawn staged guess outside border, set up staged guess grid
        self.staged_guess.grid(row = 0, column = 0, columnspan = 4, sticky = NSEW)
        self.staged_guess.rowconfigure(0, weight = 1)
        for c in range(4):
            self.staged_guess.columnconfigure(c, weight = 1)
        
        self.staged_guess.grid_propagate(0)

        # spawn staged guess cells and colors
        for c in range(4):
            self.staged_guess_cells[c].grid(in_ = self.staged_guess, row = 0, column = c, sticky = NSEW, padx = 12)
            self.staged_guess_cells[c].rowconfigure(0, weight = 1)
            self.staged_guess_cells[c].columnconfigure(0, weight = 1)
            self.staged_guess_colors[c].grid(in_ = self.staged_guess_cells[c], row = 0, column = 0, sticky = NSEW)

        self.right_side.grid_propagate(0)
        
        # spawn and setup button panels
        for c in range(4):
            self.button_panels[c].grid(row = 1, column = c, rowspan = 6, sticky = NSEW)
            for z in range(6):
                self.button_panels[c].rowconfigure(z, weight = 1)
            self.button_panels[c].columnconfigure(0, weight = 1)

            self.button_panels[c].grid_propagate(0)

        # spawn buttons in panels
        for c in range(4):
            for z in range(6):
                self.color_buttons[c][z].grid(in_ = self.button_panels[c], row = z, column = 0)

        self.right_side.grid_propagate(0)
        # spawn submit button and frame
        self.submit_button_frame.grid(row = 7, column = 0, columnspan = 2, sticky = NSEW)
        self.submit_button_frame.rowconfigure(0, weight = 1)
        self.submit_button_frame.columnconfigure(0, weight = 1)
        self.submit_button_frame.grid_propagate(0)

        self.submit_button.grid(in_ = self.submit_button_frame, row = 0, column = 0)

        self.credits.grid(row = 7, column = 2, columnspan = 2, sticky = SE, pady = 16, padx = 24)
        #self.credits.pack()

        self.logo.grid(row = 8, column = 0, columnspan = 4, sticky = NSEW)
        #self.logo.pack()
        

    def _create_widgets(self):
        self._create_left()
        self._create_right()

        # Set up left side:
        
    def _place_widgets(self):
        # set up left/right half as 2 columns:
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight = 1)

        self._place_left()
        self._place_right()


    def reveal_target(self):
        for c in range(4):
            self.hiddentarget_labels[c].grid_remove()
    
    def get_selected(self):
        return self._selected_data
    
    #def colorselect_pressed(self, clid, new):
    #    pass

    #def submit_pressed(self):
    #    pass

    def set_guess_cell(self, clid, new):
        if new in range(6) or new is None:
            self.staged_guess_colors[clid]['bg'] = DEFAULTCOLOR if new is None else COLORS[new]
            self._selected_data[clid] = new
        else:
            raise ValueError("Invalid color ID given!")
    
    def push_round(self, round):
        for c in range(4):
            self.history_colors[round.getID()][c]['bg'] = DEFAULTCOLOR if (x := round.getGuess()[c]) is None else COLORS[x]
        self.history_feedback_labels[round.getID()][0]['text'] = round.getFeedback()[0]
        self.history_feedback_labels[round.getID()][1]['text'] = round.getFeedback()[1]

    def do_victory_things(self, game_final_length):
        self.reveal_target()
        victory_msg_window = Toplevel(
            width = 256,
            height = 256
        )
        victory_label1 = Label(
            victory_msg_window,
            text = "Congrations, you guessed the sequence :D"
        )
        if game_final_length >= 9:
            celebration_str = f"Just in the nick of time, too! You took a whole {game_final_length} rounds!"
        
        elif game_final_length == 1:
            celebration_str = "You must've gotten lucky! You got it first-try!"

        elif game_final_length <= 3:
            celebration_str = f"And with time to spare! You only took an astonishing {game_final_length} rounds!"

        else:
            celebration_str = f"You accomplished this feat in some {game_final_length} rounds."
        
        victory_label2 = Label(
            victory_msg_window,
            text = celebration_str
        )
        victory_msg_window.resizable(width = 0, height = 0)
        victory_label1.pack()
        victory_label2.pack()
        self._nuke_buttons()
        victory_msg_window.mainloop()
    
    def do_defeat_things(self, target):
        self.reveal_target()
        defeat_msg_window = Toplevel(
            width = 256,
            height = 256
        )
        defeat_label1 = Label(
            defeat_msg_window,
            text = "You utter disappointment. You disgust me."
        )
        defeat_label1 = Label(
            defeat_msg_window,
            text = f"Ten entire rounds, and you can't even guess that the sequence was actually {target_to_words(target)}? Pathetic!"
        )
        defeat_msg_window.resizable(width = 0, height = 0)
        defeat_label1.pack()
        defeat_label2.pack()
        self._nuke_buttons()
        defeat_msg_window("Defeat!")


        defeat_msg_window.mainloop()
    
    def _nuke_buttons(self):
        for c in range(4):
            for z in range(6):
                self.color_buttons[c][z].config(state = DISABLED)
        self.submit_button.config(state = DISABLED)
        



# some tests lol
if __name__ == "__main__":
    window = MainWindow()
    window.master.title("Did someone say sus 😱😱😱 HOLY FUCKING SHIT‼️‼️‼️‼️ IS THAT A MOTHERFUCKING AMONG US REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1! 😱😱😱😱😱😱😱 AMONG US IS THE BEST FUCKING GAME 🔥🔥🔥🔥💯💯💯💯 RED IS SO SUSSSSS 🕵️🕵️🕵️🕵️🕵️🕵️🕵️🟥🟥🟥🟥🟥 COME TO MEDBAY AND WATCH ME SCAN 🏥🏥🏥🏥🏥🏥🏥🏥 🏥🏥🏥🏥 WHY IS NO ONE FIXING O2 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡 OH YOUR CREWMATE? NAME EVERY TASK 🔫😠🔫😠🔫😠🔫😠🔫😠 Where Any sus!❓ ❓ Where!❓ ❓ Where! Any sus!❓ Where! ❓ Any sus!❓ ❓ Any sus! ❓ ❓ ❓ ❓ Where!Where!Where! Any sus!Where!Any sus Where!❓ Where! ❓ Where!Any sus❓ ❓ Any sus! ❓ ❓ ❓ ❓ ❓ ❓ Where! ❓ Where! ❓ Any sus!❓ ❓ ❓ ❓ Any sus! ❓ ❓ Where!❓ Any sus! ❓ ❓ Where!❓ ❓ Where! ❓ Where!Where! ❓ ❓ ❓ ❓ ❓ ❓ ❓ Any sus!❓ ❓ ❓ Any sus!❓ ❓ ❓ ❓ Where! ❓ Where! Where!Any sus!Where! Where! ❓ ❓ ❓ ❓ ❓ ❓ I think it was purple!👀👀👀👀👀👀👀👀👀👀It wasnt me I was in vents!!!!!!!!!!!!!!😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂😂 r/amongusmemes r/unexpectedamongus r/expectedamongus perfectly balanced as all things should be r/unexpectedthanos r/expectedthanos for balance")
    window.mainloop()