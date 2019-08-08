import random
import Text
import Tables

class Variables:
    art25 = 25                                              # Variable to represent art worth 25g 
    art250 = 250
    art750 = 750
    art2500 = 2500
    art7500 = 7500

def getArtArray(artType):                                   # Returns the array for the corresponding art value type
    if (artType == Variables.art25):
        return Tables.Art.art25gpValue
    elif (artType == Variables.art250):
        return Tables.Art.art250gpValue
    elif (artType == Variables.art750):
        return Tables.Art.art750gpValue
    elif (artType == Variables.art2500):
        return Tables.Art.art2500gpValue
    else:
        return Tables.Art.art7500gpValue

def getArtValue(artType):                                   # Returns the value of the art type
    if (artType == Variables.art25):
        return Variables.art25
    if (artType == Variables.art250):
        return Variables.art250
    if (artType == Variables.art750):
        return Variables.art750
    if (artType == Variables.art2500):
        return Variables.art2500
    else:
        return Variables.art7500

def getArt(numArt, artValueTable):                          # Prints a random list of the requested amount and type of art
    print(Text.Color.magenta, end="")                       # Turn on magenta text color formatting
    artArray = getArtArray(artValueTable)                   # Get the requested art table based on the provided artValueTable
    artValue = getArtValue(artValueTable)                   # Get the art's value based on the provided artValueTable
    print(" Art worth " + str(artValue) + "gp each:")       # Print an informative header
    numArtTypes = len(artArray)                             # Get the number of art types in the requested table
    artTracker = [0] * numArtTypes                          # Initialize an art type tracker to track the amount of each piece of art generated
    for i in range(numArt):                                 # For the number of requested pieces of art
        art = random.randint(0, numArtTypes - 1)            # Generate an art piece from the art table array
        artTracker[art] += 1                                # Increment the array tracker location for the generated art piece
    for i in range(numArtTypes):                            # For each piece of art in the table
        if (artTracker[i] > 0):                             # If the tracker location for that piece is at least 1
            artCount = str(artTracker[i])                   # Print the number acquired in the tracker for that piece
            print(" " + artCount + " " + artArray[i])       # Print the count and the art piece
    print(Text.Color.off)                                   # Turn off magenta text color formatting
    return                                                  # Return from the function