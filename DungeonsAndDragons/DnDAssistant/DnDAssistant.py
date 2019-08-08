# Joshua Worthington

import os
import Phandelver

class Console:                                                          # Initiate Class for clearing the console
    clear = lambda: os.system('cls')                                    # Class variable for clearing the console screen


def printIntro():                                                       # Prints application intro
    print("Welcome to the Dungeons and Dragons campaign assistant!")
    print()
    return                                                              # Return from the function

def getCampaignNumber():                                                # Gets validated campaign menu selection value
    invalid = False                                                     # Input flag to control print outputs based on user input
    while(1):                                                           # Loop (until valid selection is entered)
        try:                                                            # Try to get a valid selection from the user
            print("Dungeons and Dragons Campaigns")                     # Campaign header
            print(" 1) Lost Mine of Phandelver")                        # Campaign 1
            if (invalid == False):                                      # If invalid input flag is false
                campaignNumber = int(input("Enter campaign number: "))  # Print original input prompt
            else:                                                       # If invalid entry flag is true
                campaignNumber = int(input("Invalid campaign number: "))# Print invalid input prompt
            if (campaignNumber > 0 and campaignNumber <= 1):            # If user entered valid menu selection
                break                                                   # Break out of the loop
            else:                                                       # User entered an invalid menu number
                invalid = True                                          # Set invalid entry flag to true
        except ValueError:                                              # If invalid text was entered, catch the error
            invalid = True                                              # Set invalid entry flag to true
        Console.clear()                                                 # Clear the screen
    Console.clear()                                                     # Clear the screen
    return campaignNumber                                               # Return the campaign menu value

def main():                                                             # Main function that controls entry point to different campaigns
    printIntro()
    campaignNumber = getCampaignNumber()                                # Get the user's campaign value
    if (campaignNumber == 1):
        Phandelver.runCampaign()

if __name__=="__main__":                                                # If module is run as a main program
       main()                                                           # Enter the main loop