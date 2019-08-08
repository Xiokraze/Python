import random

class Die:                                                  # Class for saving sizes of dice to accessible variables
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

class Roll:                                                 # Class for rolling specified dice
    def d4():
        return random.randint(1, 4)
    def d6():
        return random.randint(1, 6)
    def d8():
        return random.randint(1, 8)
    def d10():
        return random.randint(1, 10)
    def d12():
        return random.randint(1, 12)
    def d20():
        return random.randint(1, 20)
    def d100():
        return random.randint(1, 100)

def rollDice(numDice, dieSides):                            # Retuns a count dependent upon the number of dice and corresponding sides
    diceTotal = 0                                           # Initialize dice total to 0       
    for i in range(numDice):                                # For each of the dice
        if (dieSides == 4):                                 # If a 4 sided die is rolling
            diceTotal += Roll.d4()                          # Roll a d4 and add it to the dice total
        elif (dieSides == 6):                               # If a 6 sided die is rolling
            diceTotal += Roll.d6()                          # Roll a d6 and add it to the dice total
        elif (dieSides == 8):                               # If a 6 sided die is rolling
            diceTotal += Roll.d8()                          # Roll a d6 and add it to the dice total
        elif (dieSides == 10):                              # If a 6 sided die is rolling
            diceTotal += Roll.d10()                         # Roll a d6 and add it to the dice total
        elif (dieSides == 12):                              # If a 6 sided die is rolling
            diceTotal += Roll.d12()                         # Roll a d6 and add it to the dice total
        elif (dieSides == 20):                              # If a 6 sided die is rolling
            diceTotal += Roll.d20()                         # Roll a d6 and add it to the dice total
        elif (dieSides == 100):                             # If a 6 sided die is rolling
            diceTotal += Roll.d100()                        # Roll a d6 and add it to the dice total
    return diceTotal                                        # Return the total of the rolled dice