# Game class:
# Manages the game.

from Round import *
from handydandies import *

class Game():

    # Attributes: rounds, target
    # Methods: getTarget, getRounds, getRoundCount, nextRound, getLength

    def __init__(self, target):
        self.target = target
        self.rounds = []
        print("Game created.")
    
    @verbose_wrapper
    def nextRound(self, guess):
        self.rounds += [Round(guess, self.target)]
    
    def getTarget(self):
        return self.target
    
    def getRounds(self):
        return self.rounds

    def getLength(self):
        return len(self.rounds)