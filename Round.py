# Round class:
# Manages a single round.

from handydandies import *

class Round():

    # Attributes: guess, accurates, inaccurates
    # Methods: checkVictory, getGuess, getFeedback

    def __init__(self, guess, target, rid):
        self.round_id = rid
        self.guess = guess
        
        
        self.accurates = 0
        self.inaccurates = 0
        
        t_guess = list(guess)       # in case Tuple was given (is immutable and thus unsuitable)
        t_target = list(target)

        for c in range(4):              # Catch all the Accurates first, since these take priority. Don't want an Accurate match denied because it was pre-emptively None'd!
            if t_guess[c] == t_target[c]:
                self.accurates += 1
                t_guess[c] = t_target[c] = None
        
        for c in range(4):
            for z in range(4):
                if None in (t_guess[z], t_target[c]) or c == z:
                    continue
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

    def getID(self):
        return self.round_id
   
# If this class definition is run by itself, some test values will be run:
if __name__ == "__main__":
    test_round = Round((1,2,3,4), (1,2,4,3))
    print(f"{test_round.accurates}, {test_round.inaccurates}")
    print()
    test_round = Round((1,2,3,4), (4,3,2,1))
    print(f"{test_round.accurates}, {test_round.inaccurates}")
    print()
    test_round = Round((1,2,3,4), (1,2,3,4))
    print(f"{test_round.accurates}, {test_round.inaccurates}")
    print()
    test_round = Round((1,2,3,4), (2,2,2,2))
    print(f"{test_round.accurates}, {test_round.inaccurates}")