# Main program and game loop
from Round import *
from random import choices

COLORS = (
    "000000",   # White
    "ffffff",   # Black
    "ff0000",   # Red
    "00ff00",   # Green
    "0000ff",   # Blue
    "ffdd00"    # Yellow (slightly more "banana"-y for better visibility)
    )

def makeTarget() -> list:
    return choices(range(6), k = 4)

if __name__ == "__main__":
    print("Yay, the Main")