import Dice
import os
import Tables
import Text
import Input


class Screen:
    clear = lambda: os.system('cls')

class Menu:
    menu = [" 1) Creator",
        " 2) History",
        " 3) Minor Property",
        " 4) Quirk",
        " 5) All The Above",
        " 6) Back"]

def getOption():
    print(" What property would you like to generate?")
    print()
    numOptions = len(Menu.menu)
    option = Input.getIntegerInput(1, numOptions, Menu.menu)
    return option

def getCreator():
    d20Value = Dice.Roll.d20()
    if (d20Value == 1): 
        return Tables.MagicProperties.creator[0]
    elif (d20Value >= 2 and d20Value <= 4):
        return Tables.MagicProperties.creator[1]
    elif (d20Value == 5):
        return Tables.MagicProperties.creator[2]
    elif (d20Value == 6):
        return Tables.MagicProperties.creator[3]
    elif (d20Value == 7):
        return Tables.MagicProperties.creator[4]
    elif (d20Value == 8 or d20Value == 9):
        return Tables.MagicProperties.creator[5]
    elif (d20Value == 10):
        return Tables.MagicProperties.creator[6]
    elif (d20Value == 11):
        return Tables.MagicProperties.creator[7]
    elif (d20Value == 12):
        return Tables.MagicProperties.creator[8]
    elif (d20Value == 13):
        return Tables.MagicProperties.creator[9]
    elif (d20Value == 14 or d20Value == 15):
        return Tables.MagicProperties.creator[10]
    elif (d20Value == 16):
        return Tables.MagicProperties.creator[11]
    elif (d20Value == 17):
        return Tables.MagicProperties.creator[12]
    elif (d20Value == 18):
        return Tables.MagicProperties.creator[13]
    elif (d20Value == 19):
        return Tables.MagicProperties.creator[14]
    else:
        return Tables.MagicProperties.creator[15]

def getHistory():
    d8Value = Dice.Roll.d8()
    return Tables.MagicProperties.history[d8Value - 1]

def getMinorProperty():
    d20Value = Dice.Roll.d20()
    return Tables.MagicProperties.minorProperty[d20Value - 1]

def getQuirk():
    d12Value = Dice.Roll.d12()
    return Tables.MagicProperties.quirk[d12Value - 1]

def printProperties(creator, history, minorProperty, quirk):
    if (len(creator) > 0):
        print(Text.Color.yellow, end="")
        print(" Creator: " + creator)
        print(Text.Color.off)
    if (len(history) > 0):
        print(Text.Color.magenta, end="")
        print(" History: " + history)
        print(Text.Color.off)
    if (len(minorProperty) > 0):
        print(Text.Color.green, end="")
        print(" Minor Property: " + minorProperty)
        print(Text.Color.off)
    if (len(quirk) > 0):
        print(Text.Color.cyan, end="")
        print(" Quirk: " + quirk)
        print(Text.Color.off)

def run():
    Screen.clear()
    option = getOption()
    creator = ""
    history = ""
    minorProperty = ""
    quirk = ""
    
    if (option == 1):
        creator = getCreator()
    elif (option == 2):
        history = getHistory()
    elif (option == 3):
        minorProperty = getMinorProperty()
    elif (option  == 4):
        quirk = getQuirk()
    elif (option == 5):
        creator = getCreator()
        history = getHistory()
        minorProperty = getMinorProperty()
        quirk = getQuirk()
    else:
        return
    printProperties(creator, history, minorProperty, quirk)