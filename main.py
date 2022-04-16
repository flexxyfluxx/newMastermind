# Main program and game loop
from Game import *
from random import choices
from handydandies import *
from GUI import *

COLORS = (
    "000000",   # White
    "ffffff",   # Black
    "ff0000",   # Red
    "00ff00",   # Green
    "0000ff",   # Blue
    "ffdd00"    # Yellow (slightly more "banana"-y for better visibility)
)

@verbose_wrapper
def makeTarget():

    return choices(range(6), k = 4)

@verbose_wrapper
def play_in_console():

    print("Game started.")

    target = makeTarget()
    current_game = Game(target)
    won = False

    while not won and current_game.getLength() < 10:
        guess = []
        while len(guess) != 4:
            guess = list(str(input("Input guess:")))
        for c in range(len(guess)):
            guess[c] = int(guess[c])

        print(f"Guess: {guess}")

        #print(f"{target = }")          # For debugging only!!! (no cheating!)

        current_game.nextRound(guess)
        current_round = current_game.rounds[-1]
        
        accurates = current_round.getFeedback()[0]
        inaccurates = current_round.getFeedback()[1]
        print(f"Accurates: {accurates};\nInaccurates: {inaccurates}")

        if current_round.checkVictory():
            won = True

    game_final_length = current_game.getLength()

    if won:
        print("Congrations, you guessed the sequence :D")
        
        if game_final_length >= 9:
            print(f"Just in the nick of time, too! You took a whole {game_final_length} rounds!")
        
        elif game_final_length == 1:
            print("You must've gotten lucky! You got it first-try!")

        elif game_final_length <= 3:
            print(f"And with time to spare! You only took an astonishing {game_final_length} rounds!")

        else:
            print(f"You accomplished this feat in some {game_final_length} rounds.")
    
    else:
        print("You utter disappointment. You disgust me.")
        print(f"Ten entire rounds, and you can't even guess that the sequence was actually {current_game.getTarget()}? Pathetic!")

def submit_guess(game, window, guess):
    if None in guess:
        return
    
    game.nextRound(guess)
    window.push_round(game.getRounds()[-1])

    if game.getRounds()[-1].checkVictory():
        window.do_victory_things()
        window.quit()
    elif game.getLength() >= 10:
        window.do_defeat_things()
        window.quit()


def submit_color(window, clid, new):
    if new is None:
        return
    
    window.set_guess_cell(clid, new)


if __name__ == "__main__":
    window = MainWindow()
    game = Game(makeTarget())

    window.colorselect_pressed = lambda: submit_color(window=window, clid=None, new=None)
    window.submit_pressed = lambda: submit_guess(game, window, window.get_selected())

    window.master.title("MASTERmind")
    window.mainloop()

    #play_in_console()