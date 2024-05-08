#Dice game - Stage 7
#Adding the code for a running total

#throw two six sided dice
#print the result

#Declare variables and import modules
import random

#players
Player1score = 0
Player2score = 0
#variables needed for a running total
Player1total = 0
Player2total = 0

#rounds
rounds = 0

#code to allow 5 rounds

while rounds != 5:

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

    #Code duplicated for player 2

    #Dice throw code
    throw1 = random.randint(1,6)
    throw2 = random.randint(1,6)
    print("You threw a",throw1,"and a",throw2)

    #code to decide scoring
    #code for a draw
    if throw1 == throw2:
        print("You threw a double!")
        Player2score = (throw1 + throw2) + 10
        extraThrow = random.randint(1,6)
        print("You threw an extra ",extraThrow)
        Player2score = Player2score + extraThrow

    #code for two different numbers
    else:
        print("That isn't a double...")
        Player2score = (throw1 + throw2) - 5

    #code for if the score ends up being less than 0

    if Player2score < 0:
        Player2score = 0
    else:
        Player2score = Player2score

    #print the score for the turn
    print("Player 2, you scored",Player2score)

    #code for running total
    Player1total = Player1total + Player1score
    Player2total = Player2total + Player2score

    print("Player 1 your total score is",Player1total)
    print("Player 2 your total score is",Player2total)

    #code for working out how many rounds have happened
    rounds = rounds + 1
    print("rounds =",rounds)

#Code tested and running as expected
