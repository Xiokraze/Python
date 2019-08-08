import Tables
import Input
import Text
import Dice

class Screen:
    clear = lambda: os.system('cls')

class Menu:
    menu = [" 1) Ammunition",
        " 2) Arcane Focus, Duridic Focus, Holy Symbols",
        " 3) General Goods",
        " 4) Back"]

def getOption():
    print(" What would you like to view?")
    print()
    numOptions = len(Menu.menu)
    option = Input.getIntegerInput(1, numOptions, Menu.menu)
    return option

def printGear(gearTable):
    max = len(gearTable)
    tableEntries = 3
    typeWidth = 30
    costWidth = 10
    weightWidth = 8
    count = 0
    textColorFlag = 1
    for i in range(max):
        if (textColorFlag == 1):
            print(Text.Color.yellow, end="")
        if (i % tableEntries == 0 and i != 0): 
            print()
        if (count == 0):
            print(gearTable[i].ljust(typeWidth), end="")
        elif(count == 1):
            print(gearTable[i].rjust(costWidth) + " ", end="")
        else:
            print(gearTable[i].rjust(weightWidth), end="")
        count += 1
        if (textColorFlag == 1 and i == 2):
            textColorFlag = 0
            print(Text.Color.off, end="")
        if (count == 3):
            count = 0
    print()
    print()
    return

def run():
    option = getOption()
    if (option == 1):
        printGear(Tables.AdventuringGear.ammunition)
    elif (option == 2):
        printGear(Tables.AdventuringGear.arcaneFocus)
        printGear(Tables.AdventuringGear.druidicFocus)
        printGear(Tables.AdventuringGear.holySymbol)
    elif (option == 3):
        printGear(Tables.AdventuringGear.otherGear)
    else:
        return