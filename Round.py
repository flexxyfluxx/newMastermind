# Round class

# Manages a single round.

class Round():

    # Attributes: guess, accurates, inaccurates
    # Methods: checkVictory, getGuess, getFeedback

    def __init__(self, guess, target):
        self.guess = guess
        
        
        self.accurates = 0
        self.inaccurates = 0
        
        t_guess = list(guess)       # in case Tuple was given (is immutable and thus unsuitable)
        t_target = list(target)

        for c in range(4):              # Catch the Accurates first, since these take priority. Don't want an Accurate denied because it was pre-emptively None'd!
            if t_guess[c] == t_target[c]:
                self.accurates += 1
                t_guess[c] = t_target[c] = None
        
        for c in range(4):
            for z in range(4):
                if None in (t_guess[z], t_target[c]):
                    pass
                elif t_guess[z] == t_target[c]:
                    self.inaccurates += 1
                    t_guess[z] = None
                    t_target[c] = None
    
    def checkVictory(self):
        if self.accurates == 4 and self.inaccurates == 0:
            return True
        else:
            return False

    def getGuess(self):
        return self.guess

    def getFeedback(self):
        return (self.accurates, self.inaccurates)
        







# If this class definition is run by itself, some tests will be run.
if __name__ == "__main__":
    test_round = Round((1,2,3,4), (1,2,4,3))
    print(test_round.accurates)
    print(test_round.inaccurates)
    print()
    test_round = Round((1,2,3,4), (4,3,2,1))
    print(test_round.accurates)
    print(test_round.inaccurates)
    print()
    test_round = Round((1,2,3,4), (1,2,3,4))
    print(test_round.accurates)
    print(test_round.inaccurates)
    print()
    test_round = Round((1,2,3,4), (2,2,2,2))
    print(test_round.accurates)
    print(test_round.inaccurates)