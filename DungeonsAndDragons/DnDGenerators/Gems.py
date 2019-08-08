import random
import Text
import Tables

class Variables:
    gems10 = 10                                             # Variable to represent gems worth 10g                        
    gems50 = 50                                             # Variable to represent gems worth 50g
    gems100 = 100
    gems500 = 500
    gems1000 = 1000
    gems5000 = 5000

def getGemArray(gemType):                                   # Returns the value of the gem type
    if (gemType == Variables.gems10):
        return Tables.Gems.gems10gpValue
    else:
        return Tables.Gems.gems50gpValue

def getGemValue(gemType):                                   # Returns the gem array table corresponding to the gem type value
    if (gemType == Variables.gems10):
        return Variables.gems10
    else:
        return Variables.gems50

def getGems(numGems, gemValueTable):                        # Prints a random list of an amount and type of gems
    print(Text.Color.magenta, end="")                       # Turn the magenta text output off  
    gemArray = getGemArray(gemValueTable)                   # Get the gem array based on the value table
    gemValue = getGemValue(gemValueTable)                   # Get the gem value based on the 
    print(" Gems worth " + str(gemValue) + "gp each:")      # Print an informative header
    numGemTypes = len(gemArray)                             # Get the number of gems worth 10gp
    gemTracker = [0] * numGemTypes                          # Initialize an array with 0s for every gem type (12)
    for i in range(numGems):                                # For the number of gems awarded
        gem = random.randint(0, numGemTypes - 1)            # Get a random gem location in the gem's list
        gemTracker[gem] += 1                                # Increment that gem's count in the initialized list
    for i in range(numGemTypes):                            # For each gem type
        if (gemTracker[i] > 0):                             # If that gem has at least 1 gem
            gemCount = str(gemTracker[i])                   # Save the number of that gem to a variable
            print(" " + gemCount + " " + gemArray[i])       # Print the number and the gem/description
    print(Text.Color.off)                                   # Add a newline and disable the magenta text output color
    return                                                  # Return from the function