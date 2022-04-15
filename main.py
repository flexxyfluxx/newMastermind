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
def makeTarget() -> list:

    return choices(range(6), k = 4)

@verbose_wrapper
def playGame() -> None:

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
            print(f"""Just in the nick of time, too!\
                You took a whole {game_final_length} rounds!""")
        
        elif game_final_length == 1:
            print("You must've gotten lucky! You got it first-try!")

        elif game_final_length <= 3:
            print(f"""And with time to spare! You only took an astonishing {game_final_length} rounds!""")

        else:
            print(f"""You accomplished this feat in some {game_final_length} rounds.""")
    
    else:
        print("You utter disappointment. You disgust me.")
        print(f"""Ten entire rounds, and you can't even guess that the sequence was actually {current_game.getTarget()}? Pathetic!""")
        

if __name__ == "__main__":
    playGame()