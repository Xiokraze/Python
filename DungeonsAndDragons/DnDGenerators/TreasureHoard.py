import random
import os
import Gems
import Art
import MagicItems
import Dice
import Text
import Tables

class Screen:
    clear = lambda: os.system('cls')

class RewardTable:
    def earlyGame():
        CP = str(getCoins(6, 100))                          # CP = copper pieces
        SP = str(getCoins(3, 100))                          # SP = silver pieces
        GP = str(getCoins(2, 10))                           # GP = gold pieces
        PP = "0"
        printCoins(GP, SP, CP, PP)
        roll100 = Dice.Roll.d100()                          # Roll and save a d100
        getEarlyGameLoot(roll100)                           # Get gems/art/magic items based on the d100 roll
        return

    def midGame():
        CP = str(getCoins(2, 100))
        SP = str(getCoins(2, 1000))
        GP = str(getCoins(6, 100))
        PP = str(getCoins(3, 10))
        printCoins(GP, SP, CP, PP)
        roll100 = Dice.Roll.d100()                          # Roll and save a d100
        getMidGameLoot(roll100)                             # Get gems/art/magic items based on the d100 roll
        return

    def lateGame():
        CP = "0"
        SP = "0"
        GP = str(getCoins(4, 1000))
        PP = str(getCoins(5, 100))
        printCoins(GP, SP, CP, PP)
        roll100 = Dice.Roll.d100()                          # Roll and save a d100
        getLateGameLoot(roll100)                            # Get gems/art/magic items based on the d100 roll
        return

    def endGame():
        CP = "0"
        SP = "0"
        GP = str(getCoins(12, 1000))
        PP = str(getCoins(8, 1000))
        printCoins(GP, SP, CP, PP)
        roll100 = Dice.Roll.d100()                          # Roll and save a d100
        getEndGameLoot(roll100)                             # Get gems/art/magic items based on the d100 roll
        return

def printHeader(partyLevel):                                # Prints the text before the party level
    print(Text.Color.white, end="")
    if (partyLevel < 10):
        text = " Level 0"
    else:
        text = " Level "
    print(text + str(partyLevel) + " Treasure Hoard:")
    print(Text.Color.off)

def printCoins(GP, SP, CP, PP):
    print(Text.Color.yellow, end="")                        # Turn yellow text output on
    print(" " + GP + "GP " + SP + "SP ", end="")            # Print the coin amount
    print(CP + "CP "+ PP + "PP")                            # Print the coin amount
    print(Text.Color.off)                                   # Turn the yellow text output off
    return                                                  # Return from the function

def getCoins(numDice, multiplicitive):                      # Returns coin totals based on the number of dice and the multiplication value
    diceTotal = 0                                           # Initialize the dice total to 0                           
    coinTotal = 0                                           # Initialize the coin total to 0
    for i in range(numDice):                                # For each of the dice
        diceTotal += Dice.Roll.d6()                         # Roll a d6 and add it to the dice total
    coinTotal = diceTotal * multiplicitive                  # To get the coin total, multiple the total dice amount by the multiplication value
    return coinTotal                                        # Return the total amount of coins

def getCount(numDice, dieSides):                            # Retuns a count dependent upon the number of dice and corresponding sides
    diceTotal = 0                                           # Initialize dice total to 0       
    for i in range(numDice):                                # For each of the dice
        if (dieSides == 6):                                 # If a 6 sided die is rolling
            diceTotal += Dice.Roll.d6()                     # Roll a d6 and add it to the dice total
        else:                                               # Else, a 4 sided die is rolling
            diceTotal += Dice.Roll.d4()                     # Roll a d4 and add it to the dice total
    return diceTotal                                        # Return the total of the rolled dice

def getEarlyGameLoot(d100):                                 # Controls printing gems, art, and magic items dependent upon the d100 roll
    # This function checks the d100 roll then generates
    # gems or art, and magic items based on the result. 
    # A die is rolled to determine the number of gems or
    # art, then the corresponding function is called to
    # generate the items. Another die and function call
    # is used to generate magic items and the appropriate
    # magic item table is retrieved.

    if (d100 >= 1 and d100 <= 6):
        print(Text.Color.magenta, end="")
        print("No gems or art")
        print(Text.Color.off)    
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 7 and d100 <= 16):
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems10)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 17 and d100 <= 26):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 27 and d100 <= 36):
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 37 and d100 <= 44):
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems10)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 45 and d100 <= 52):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 53 and d100 <= 60):
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 61 and d100 <= 65):
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems10)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 66 and d100 <= 70):
        numArt = Dice.rollDice(2, Dice.Roll.d4())
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 71 and d100 <= 75):
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 76 and d100 <= 78):
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems10)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 79 or d100 == 80):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 81 and d100 <= 85): 
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 86 and d100 <= 92):    
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)             

    elif (d100 >= 93 and d100 <= 97):
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 98 or d100 == 99):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    else:
        numGems = Dice.rollDice(2, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    return                                                  # Return from the function

def getMidGameLoot(d100):
    # See earlyGameLoot() description
    if (d100 >= 1 and d100 <= 4):
        print(Text.Color.magenta, end="")
        print(" No gems or art")
        print(Text.Color.off)  
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 5 and d100 <= 10):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25) 
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 11 and d100 <= 16):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 17 and d100 <= 22):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems100)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 23 and d100 <= 28):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250) 
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 29 and d100 <= 32):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 33 and d100 <= 36):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 37 and d100 <= 40):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems100)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableA 
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 41 and d100 <= 44):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 45 and d100 <= 49):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 50 and d100 <= 54):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 55 and d100 <= 59):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems100)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 60 and d100 <= 63):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 64 and d100 <= 66):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 67 and d100 <= 69):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 70 and d100 <= 72):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems100)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 73 or d100 == 74):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableC 
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 75 or d100 == 76):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 77 or d100 == 78):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 79):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems100)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 80):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 81 and d100 <= 84):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art25)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 85 and d100 <= 88):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems50)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 89 and d100 <= 91):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems100)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 92 and d100 <= 94):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 95 or d100 == 96):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems100)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 97 or d100 == 98):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 99):    
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems100)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    else:
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    return                                                  # Return from the function

def getLateGameLoot(d100):
    # See earlyGameLoot() description

    if (d100 >= 1 and d100 <= 3):
        print(Text.Color.magenta, end="")
        print("No gems or art")
        print(Text.Color.off)  
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 4 and d100 <= 6):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 7 and d100 <= 9):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art750)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 10 and d100 <= 12):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems500)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 13 and d100 <= 15):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 16 and d100 <= 19):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 20 and d100 <= 23):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art750)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 24 and d100 <= 26):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 27 and d100 <= 29):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableA
        MagicItems.getMagicItems(numMagicItems, tableValue)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableB
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 30 and d100 <= 35):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 36 and d100 <= 40):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art750)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 41 and d100 <= 45):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 46 and d100 <= 50):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 51 and d100 <= 54):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 55 and d100 <= 58):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art750)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 59 and d100 <= 62):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 63 and d100 <= 66):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 67 or d100 == 68):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableE
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 69 or d100 == 70):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableE
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 71 or d100 == 72):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems500)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableE
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 73 or d100 == 74):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableE
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 75 or d100 == 76):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 77 or d100 == 78):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art750)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 79 or d100 == 80):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems500)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 81 or d100 == 82):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableF
        MagicItems.getMagicItems(numMagicItems, tableValue)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 83 and d100 <= 85):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 86 and d100 <= 88):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art750)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 89 or d100 == 90):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 91 or d100 == 92):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 93 or d100 == 94):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art250)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableI
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 77 or d100 == 78):
        numArt = Dice.rollDice(2, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art750)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableI
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 91 or d100 == 92):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems500)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableI
        MagicItems.getMagicItems(numMagicItems, tableValue)

    else:
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = 1
        tableValue = MagicItems.Variables.TableI
        MagicItems.getMagicItems(numMagicItems, tableValue)

    return

def getEndGameLoot(d100):
    if (d100 == 1 or d100 == 2):
        print(Text.Color.magenta, end="")
        print("No gems or art")
        print(Text.Color.off)  
        print(Text.Color.green, end="")
        print(" No magic items")
        print(Text.Color.off)

    elif (d100 >= 3 and d100 <= 5):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d8)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 6 and d100 <= 8):
        numArt = Dice.rollDice(1, Dice.Die.d10)
        Art.getArt(numArt, Art.Variables.art2500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d8)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 9 and d100 <= 11):
        numArt = Dice.rollDice(1, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art7500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d8)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 12 and d100 <= 14):
        numGems = Dice.rollDice(1, Dice.Die.d8)
        Gems.getGems(numGems, Gems.Variables.gems5000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d8)
        tableValue = MagicItems.Variables.TableC
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 15 and d100 <= 22):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 23 and d100 <= 30):
        numArt = Dice.rollDice(1, Dice.Die.d10)
        Art.getArt(numArt, Art.Variables.art2500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 31 and d100 <= 38):
        numArt = Dice.rollDice(1, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art7500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 39 and d100 <= 46):
        numGems = Dice.rollDice(1, Dice.Die.d8)
        Gems.getGems(numGems, Gems.Variables.gems5000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableD
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 47 and d100 <= 52):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableE
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 53 and d100 <= 58):
        numArt = Dice.rollDice(1, Dice.Die.d10)
        Art.getArt(numArt, Art.Variables.art2500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableE
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 59 and d100 <= 63):
        numArt = Dice.rollDice(1, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art7500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableE
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 64 and d100 <= 68):
        numGems = Dice.rollDice(1, Dice.Die.d8)
        Gems.getGems(numGems, Gems.Variables.gems5000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d6)
        tableValue = MagicItems.Variables.TableE
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 69):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 70):
        numArt = Dice.rollDice(1, Dice.Die.d10)
        Art.getArt(numArt, Art.Variables.art2500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 71):
        numArt = Dice.rollDice(1, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art7500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 72):
        numGems = Dice.rollDice(1, Dice.Die.d8)
        Gems.getGems(numGems, Gems.Variables.gems5000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableG
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 73 or d100 == 74):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 75 or d100 == 76):
        numArt = Dice.rollDice(1, Dice.Die.d10)
        Art.getArt(numArt, Art.Variables.art2500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 77 or d100 == 78):
        numArt = Dice.rollDice(1, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art7500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 == 79 or d100 == 80):
        numGems = Dice.rollDice(1, Dice.Die.d8)
        Gems.getGems(numGems, Gems.Variables.gems5000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableH
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 81 and d100 <= 85):
        numGems = Dice.rollDice(3, Dice.Die.d6)
        Gems.getGems(numGems, Gems.Variables.gems1000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableI
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 86 and d100 <= 90):
        numArt = Dice.rollDice(1, Dice.Die.d10)
        Art.getArt(numArt, Art.Variables.art2500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableI
        MagicItems.getMagicItems(numMagicItems, tableValue)

    elif (d100 >= 91 and d100 <= 95):
        numArt = Dice.rollDice(1, Dice.Die.d4)
        Art.getArt(numArt, Art.Variables.art7500)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableI
        MagicItems.getMagicItems(numMagicItems, tableValue)

    else:
        numGems = Dice.rollDice(1, Dice.Die.d8)
        Gems.getGems(numGems, Gems.Variables.gems5000)
        numMagicItems = Dice.rollDice(1, Dice.Die.d4)
        tableValue = MagicItems.Variables.TableI
        MagicItems.getMagicItems(numMagicItems, tableValue)

def run(partyLevel):                                        # Generates random treasure hoard rewards based on party level 
    Screen.clear()
    printHeader(partyLevel)
    if (partyLevel >= 0 and partyLevel <= 4):               # If party is level...
       RewardTable.earlyGame()                              # Generate early game rewards
    elif (partyLevel >= 5 and partyLevel <= 10):            # If party is level...
        RewardTable.midGame()                               # Generate mid game rewards
    elif (partyLevel >= 11 and partyLevel <= 16):           # If party is level...
        RewardTable.lateGame()                              # Generate late game rewards
    else:                                                   # Party is lvl 17+
        RewardTable.endGame()                               # Generate end game rewards
    return