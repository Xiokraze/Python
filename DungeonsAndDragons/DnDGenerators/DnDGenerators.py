import os
import TreasureHoard
import MagicItemProperties
import StandardGear
import Input
import AdventureGear
import random
import RandomLoot

class Screen:
    clear = lambda: os.system('cls')

class Data:
    minLevel = 1
    maxLevel = 20
    partyLevel = 0
    levelPrompt = [
        " Please enter the party's average level (1-20): "
    ]

    menu = [
        " 1) Random Treasure Hoard Rewards",
        " 2) Random Magic Item Properties",
        " 3) Standard Weapons/Armor",
        " 4) Adventuring Gear",
        " 5) Random Loot",
        " 0) Quit"
    ]

def main():                                                             # Application entry point
    print(" Welcome to Dungeons and Dragons random generator!")         # Welcome message
    print()                                                             # Newline formatting
    while(1):                                                           # Loop until DM exits
        option = Input.getIntegerInput(0, len(Data.menu), Data.menu)    # Get the DM's menu option choice
        if (option == 0):                                               # If option is 0
            break                                                       # Exit the application
        elif (option == 1):                                             # If option is to get a treasure hoard
            if (Data.partyLevel == 0):                                  # If the party level has not been assigned
                Data.partyLevel = Input.getIntegerInput(                      # Get the party's level
                    Data.minLevel, Data.maxLevel, Data.levelPrompt
                )
            TreasureHoard.run(Data.partyLevel)                          # Get an appropriate level treasure hoard
        elif (option == 2):
            MagicItemProperties.run()
        elif (option == 3):
            StandardGear.run()
        elif (option == 4):
            AdventureGear.run()
        elif (option == 5):
            RandomLoot.run()


if __name__=="__main__":                                                # If module is run as a main program
       main()                                                           # Enter the main loop
