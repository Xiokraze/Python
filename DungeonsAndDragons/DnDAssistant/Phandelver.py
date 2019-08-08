import os
import GoblinArrows



class Console:                                                          # Initiate Class for clearing the console
    clear = lambda: os.system('cls')                                    # Class variable for clearing the console screen

def printIntro():
    print("Welcome to the Lost Mine of Phandelver!")
    print("Campaign Source: https://www.dndbeyond.com/sources/lmop/introduction")
    print()
    return  

def getPartNumber():
    invalid = False                                                     # Input flag to control print outputs based on user input
    while(1):                                                           # Loop (until valid selection is entered)
        try:                                                            # Try to get a valid selection from the user
            print("Lost Mine of Phandelver Campaign")                   # Campaign header
            print("Which part is your group on?")                       # Requested information statement
            print(" 1) Goblin Arrows")                                  # Part 1
            print(" 2) Phandalin")                                      # Part 2
            print(" 3) The Spider's Web")                               # Part 3
            print(" 4) Wave Echo Cave")                                 # Part 4
            if (invalid == False):                                      # If invalid input flag is false
                partNumber = int(input("Enter campaign number: "))      # Print original input prompt
            else:                                                       # If invalid entry flag is true
                partNumber = int(input("Invalid campaign number: "))    # Print invalid input prompt
            if (partNumber > 0 and partNumber <= 4):                    # If user entered valid menu selection
                break                                                   # Break out of the loop
            else:                                                       # User entered an invalid menu number
                invalid = True                                          # Set invalid entry flag to true
        except ValueError:                                              # If invalid text was entered, catch the error
            invalid = True                                              # Set invalid entry flag to true
        Console.clear()                                                 # Clear the screen
    Console.clear()                                                     # Clear the screen
    return partNumber                                                   # Return the part menu value

def runCampaign():
    printIntro()
    partNumber = getPartNumber()
    if (partNumber == 1):
        GoblinArrows.run()
