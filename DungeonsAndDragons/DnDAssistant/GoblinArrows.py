import os

class Console:                                                          # Initiate Class for clearing the console
    clear = lambda: os.system('cls')                                    # Class variable for clearing the console screen

class StoryGuide:
    menu = ["Part 1 - Goblin Arrows",                                   # Text for Goblin Arrows menu
        "Which story of Goblin Arrows is your group on?",
        " 1) New Campaign",
        " 2) Goblin Ambush",
        " 3) Goblin Trail",
        " 4) Cragmaw Cave"]

    intro = ["Open the associated LostMinePhandelver.txt file.",        # Inscructions for a new game
            "Open the EnemyStats folder.\n",
            "The file will provide you with important readings, both",
            "for yourself (the DM) and for you to read to your party.\n",
            "The folder will provide you with quick stat images for the monsters.\n"]

    newGame = ["Part 1-1 New Campaign",                                 # Instructions for starting the campaign
        "1) Read Introduction",
        "2) Read 1-1",
        "3) Read 1-2 to the party",
        "4) Encourage party to introduce their characters if they haven't already",
        "5) Have party think about how they met Gundren Rockseeker",
        "6) Have party tell you how they're marching/riding/walking/etc",
        "7) Read 1-3",
        "8) Read 1-4 to the party",
        "9) Read 1-5",
        "10) Read 1-6 to the party (dependent upon 1-5)\n"]

    ambush = ["Part 1-2 Goblin Ambush",                                 # Instructions for the goblin ambush
        "1) Read 2-1 to the party",
        "2) Read 2-2",
        "3) Open the goblin image in the EnemyStats folder",
        "4) Read 2-3",
        "5) Determine initiative order",
        "6) Read 2-4 to conduct combat",
        "7) Read 2-5 if party are defeated",
        "8) Read 2-6 if the party captures at least 1 goblin",
        "9) Rest if the party desires\n"]

def getStoryNumber():                                                   # Gets the party's story location
    invalid = False                                                     # Input flag to control print outputs based on user input
    while(1):                                                           # Loop (until valid selection is entered)
        try:                                                            # Try to get a valid selection from the user
            for i in range(len(StoryGuide.menu)):                       # Print the story menu
                print(StoryGuide.menu[i])                               # Print the story menu
            if (invalid == False):                                      # If invalid input flag is false
                storyNumber = int(input("Enter story number: "))        # Print original input prompt
            else:                                                       # If invalid entry flag is true
                storyNumber = int(input("Invalid story number: "))      # Print invalid input prompt
            if (storyNumber > 0 and storyNumber <= 4):                  # If user entered valid menu selection
                break                                                   # Break out of the loop
            else:                                                       # User entered an invalid menu number
                invalid = True                                          # Set invalid entry flag to true
        except ValueError:                                              # If invalid text was entered, catch the error
            invalid = True                                              # Set invalid entry flag to true
        Console.clear()                                                 # Clear the screen
    Console.clear()                                                     # Clear the screen
    return storyNumber                                                  # Return the part menu value

def DMPause():                                                          # Returns true or false for continuing the story
    resume = input("Continue? y/n: ")                                   # Get DM's input
    if (resume == 'y' or resume == 'Y'):                                # If DM is ready to continue
        return True                                                     # Return true
    else:                                                               # If DM is not ready to continue
        return False                                                    # Return false

def printGuide(textArray):
    continueGame = False 
    while(continueGame == False):                                           
        for i in range(len(textArray)):
            print(textArray[i])
        continueGame = DMPause()
        Console.clear()
    return

def postAmbush():
    invalid = False
    while(1):
        print("1) Taking the goblin path")
        print("2) Continuing to Phandalin")
        try:
            partyAction = int(input("What is the party doing next? "))
            if (partyAction == 1 or partyAction == 2):
                break
            else:
                Console.clear()
                continue
        except ValueError:
            Console.clear()
            continue
    return partyAction

def run():
    storyNumber = getStoryNumber()
    if (storyNumber == 1):
        printGuide(StoryGuide.intro)
        printGuide(StoryGuide.newGame)
        storyNumber += 1
    if (storyNumber == 2):
        printGuide(StoryGuide.ambush)
        nextStory = postAmbush()
        storyNumber += 1