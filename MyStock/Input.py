import os

# ticker = ['ACB', 'MSFT', 'NTDOY', 'SNE', 'TTWO']
# columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

class Console:                                                      # Initiate Class for clearing the console
    clear = lambda: os.system('cls')                                # Class variable for clearing the console screen


def validInput(input):                                              # Checks if user entered only numbers for stocks
    for i in range(len(input)):                                     # Iterate through the user's input
        try:                                                        # Try casting the data to an int
            int(input[i])                                           # Cast the data to an int
        except:                                                     # If an exception is thrown
            return False                                            # User entered invalid text, return false
    return True                                                     # If no exceptions are raised, data is valid, return true


def validStock(input, list):                                        # Checks if user entered valid stock choices
    for i in range(len(input)):                                     # Iterate through the user's previously validated input
        number = int(input[i])                                      # Get the number
        if (number < 0 or number >= len(list)):                     # If any number is not a menu selection
            return False                                            # Return false
    return True                                                     # If the numbers are valid, return true


def selectAllStocks(numberOfStocks):                                # Inserts all the stock menu numbers into the list
    list = []                                                       # Initialize a temporary list
    for i in range(numberOfStocks - 1):                             # For each stock (minus 1 for "all stocks" menu choice)
        list.insert(i, i)                                           # Insert the number at its position in the list
    return list                                                     # Return the list


def getStocks(list):                                                # Gets user's stock selections
    print("Which stock(s) would you like to view?")                 # Print stock/data text
    invalid = True                                                  # Invalid input flag
    while(invalid):                                                 # Loop until user selects a valid menu option
        for i in range(len(list)):                                  # Iterate through the list
            print(str(i) + ": " + list[i])                          # Print the line number and list data
        try:                                                        # Try getting valid user input
            text = "Enter stock(s) number(s): "                     # Text to print
            userInput = [int(x) for x in input(text).split()]       # Get and split user input   
            if (validInput(userInput)):                             # If user entered only numbers
                if (validStock(userInput, list)):                   # If user entered a valid menu selection
                    invalid = False                                 # Set input flag to false to exit the loop
                else:                                               # If user entered invalid data or selection
                    raise Exception                                 # Raise an exception
            if (userInput[0] == len(list) - 1):                     # If user chose to select all stocks
                userInput = selectAllStocks(len(list))              # Reinitialize userInput to include all the stocks
        except:                                                     # User entered invalid data
            Console.clear()                                         # Clear the screen
            print("Enter the stock number(s) to view.")             # Print stock/data error text
    Console.clear()                                                 # Clear the screen
    return userInput                                                # Return the user's stock choice(s)


def getData(list):                                                  # Get's the user's data selection
    print("Which data would you like to view?")                     # Print data text
    invalid = True                                                  # Invalid input flag
    while(invalid):                                                 # Loop until user selects a valid menu option
        for i in range(len(list)):                                  # Iterate through the list
            if (i == 0):                                            # If looking at the first row
                continue                                            # Skip it since it's the stock's date
            print(str(i) + ": " + list[i])                          # Print the line number and list data
        try:                                                        # Try getting valid user input
            userInput = int(input("Data Number: "))                 # Get the user's input
            if (userInput == 0):                                    # If user entered 0
                raise Exception                                     # Raise an exception
            if (userInput >= 1 and userInput < len(list)):          # If user entered a valid menu data choice
                invalid = False                                     # Set input flag to false to exit the loop
            else:                                                   # If user entered invalid data or selection
                raise Exception                                     # Raise an exception
        except:                                                     # User entered invalid data
            Console.clear()                                         # Clear the screen
            print("Enter the data's number to view.")               # Print data error text
    Console.clear()                                                 # Clear the screen
    return userInput                                                # Return the user's data choice


def moreData():                                                     # Determines if user wants to view more data
    invalid = True                                                  # Invalid input flag
    while(invalid):                                                 # While input is invalid
        try:                                                        # Try getting valid input
            print()                                                 # Print a newline for output formatting
            print("See more data?")                                 # Ask if user wants to see more data
            print("1) Yes")                                         # Option 1
            print("2) No")                                          # Option 2
            userInput = int(input("Selection: "))                   # Get user's input
            if (userInput == 1 or userInput == 2):                  # If user entered a valid choice
                invalid = False                                     # Set input flag to false to exit the loop
        except:                                                     # User entered invalid data or selection
            Console.clear()                                         # Clear the screen
            print("Enter the 1 for yes or 2 for no.")               # Input error text
    Console.clear()                                                 # Clear the screen before returning
    if (userInput == 1):                                            # If user chose to see more data
        return True                                                 # Return true
    else:                                                           # If user chose not to see more data
        return False                                                # Return false