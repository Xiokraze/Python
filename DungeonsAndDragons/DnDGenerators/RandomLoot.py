import Dice
import Tables
import Input
import Text


class Screen:
    clear = lambda: os.system('cls')

class Menu:
    menu = [" 1) Random Trinkets (3)",
        " 5) Back"]

def getOption():
    print(" What would you like to view?")
    print()
    numOptions = len(Menu.menu)
    option = Input.getIntegerInput(1, numOptions, Menu.menu)
    return option

def getTrinkets():
    for i in range(3):
        d100 = Dice.Roll.d100()
        print(Text.Color.yellow, end="")
        print(" " + str(i + 1) + ":" + Tables.AdventuringGear.trinkets[d100 - 1])
        print(Text.Color.off)
    return



def run():
    option = getOption()
    if (option == 1):
        getTrinkets()
    else:
        return
