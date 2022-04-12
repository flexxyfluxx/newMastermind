# Game class

# Manages the game

class Game():

    # Attributes: rounds, target
    # Methods: getTarget, getRounds, getRoundCount, reset, nextRound, getLength

    def __init__(self, target):
        self.target = target
        self.rounds = []
        self.length = 0
    
    def nextRound(self, guess):
        self.rounds += [Round(guess, self.target)]
        self.length += 1
    
    def reset(self, newTarget):
        self.target = newTarget
        self.rounds = []
    
    def getTarget(self):
        return self.target
    
    def getRounds(self):
        return self.rounds

    def getLength(self):
        return self.length