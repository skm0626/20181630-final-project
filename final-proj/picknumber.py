import random

class Number:

    def __init__(self):
        self.secret = 0
        self.digit = 0
        self.trials = 0

    def newGame(self, amount):
        self.secret = random.randint(1, amount+1)
	self.digit = amount
	self.trials = 0

    def guess(self, userGuess):
        self.trials += 1
        if 0 < userGuess < self.secret:
            print "You have to type bigger number."
        elif userGuess > self.secret:
            print "You have to type smaller number."
        elif userGuess == 0:
            print"0 is out of range"
        elif userGuess == self.secret:
            print "FINISH"

    def getGuessCount(self):
        return self.trials
##TEST
if __name__== '__main__':
    s = Number()
    count = int(input("Set Range : "))
    s.newGame(count)
    x = 0
    while x != s.secret:
        inputStr = int(input("Your Guess : "))
        while inputStr > count:
            print("input %d digits!" %count)
            inputStr = int(input("Your Guess : "))
        x = s.guess(inputStr)
        print( )
    guessCount = s.getGuessCount()
    print("SUCCESS in %d trials" %guessCount)
