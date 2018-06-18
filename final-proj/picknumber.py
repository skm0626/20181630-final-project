import random

class Number:

    def __init__(self):
        self.secret = 0
        self.digit = 0
        self.trials = 0

    def newGame(self, amount):
        self.secret = random.randint(1, amount)
	self.digit = amount
	self.trials = 0

    def guess(self, userGuess):
        self.trials += 1
        if 0 < userGuess < self.secret:
            return "You have to type bigger number."
        elif userGuess > self.secret:
            return "You have to type smaller number."
        elif userGuess == 0:
            return"0 is out of range"
        elif userGuess == self.secret:
            return "FINISH"

    def getGuessCount(self):
        return self.trials

if __name__== '__main__':
    s = Number()
    count = int(input("Set Range : "))
    s.newGame(count)
    x = 0
    while x != "FINISH":
        inputStr = int(input("Your Guess : "))
	x=s.guess(inputStr)
	print(x)        
    guessCount = s.getGuessCount()
    print("SUCCESS in %d trials" %guessCount)
