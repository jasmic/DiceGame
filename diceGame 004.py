#Dice game - Stage 4
#code for a score less than 0

#throw two six sided dice
#print the result

#Declare variables and import modules
import random

Player1score = 0

#Dice throw code
throw1 = random.randint(1,6)
throw2 = random.randint(1,6)
print("You threw a",throw1,"and a",throw2)

#code to decide scoring
#code for a draw
if throw1 == throw2:
    print("You threw a double!")
    Player1score = (throw1 + throw2) + 10
    extraThrow = random.randint(1,6)
    print("You threw an extra ",extraThrow)
    Player1score = Player1score + extraThrow

#code for two different numbers
else:
    print("That isn't a double...")
    Player1score = (throw1 + throw2) - 5

#code for if the score ends up being less than 0

if Player1score < 0:
    Player1score = 0
else:
    Player1score = Player1score

#print the score for the turn
print("Player 1, you scored",Player1score)

#code tested and working as expected
