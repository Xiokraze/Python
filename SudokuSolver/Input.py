import os

class Console:                                                      # Initiate Class for clearing the console
    clear = lambda: os.system('cls')                                # Class variable for clearing the console screen

def getMenuInput():                                                 # Returns user's selected menu option
    print("Choose a menu option:")
    print("1) Default Board")
    print("2) Manual Board")
    while(1):                                                       # Loop until valid input is given
        try:                                                        # Try getting user input
            userInput = int(input("Enter Menu Number: "))           # Assign user input to a variable
            if (userInput == 1 or userInput == 2):                  # If user entered a valid menu option
                break                                               # Break out of the loop
        except ValueError:                                          # If non-valid data was entered
            print("Please select menu option 1 or 2")               # Print error message
    Console.clear()                                                 # Clear the screen
    return userInput                                                # Return the user's selection


def getBoardInput():                                                # Returns a board entered by the user
    print("Enter each row individually.")
    print("If a position is blank, enter a 0.")
    print("Enter numbers separated by a space.")
    board = [[] for i in range(9)]                                  # Create a list of lists, Sudoku is traditionally 9 by 9
    errorMessage = "Enter 0-9, each separated by one space."        # Define an error message for invalid input
    rowLength = 17                                                  # 9 numbers and 8 spaces, each row should be 17 characters long
    for i in range(9):                                              # Iterate through the rows
        while(1):                                                   # Loop until valid input is given
            try:                                                    # Try getting valid input from the user
                print("Row " + str(i + 1) + ": ", end="")           # Print current row number
                valid = True                                        # Initialize flag for valid input status
                userInput = input()                                 # Assign user input to a variable
                if (len(userInput) == rowLength):                   # If the user entered the right number of characters
                    for x in userInput.split():                     # Iterate through the characters
                        if (int(x) < 0 or int(x) > 9):              # If any character is not a valid digit
                            valid = False                           # Set valid input flag to false
                    if (valid):                                     # After checking the characters, if the status is still valid
                        board[i] = [                                # Set the current row to the user's inpt list
                            int(x) for x in userInput.split()]      # Cast the input to an int and split the string
                        break                                       # Exit the loop
                else:                                               # User input was either too short, too long, or contained a non-digit
                    print(errorMessage)                             # Print error message
            except ValueError:                                      # Initial non-digit character check failed
                print(errorMessage)                                 # Print error message
    return board                                                    # Return the board


def printBoard(board):                                              # Prints the board entered by the user
    for i in range(9):                                              # For each row in the board
        print(*board[i], sep=" ")                                   # Print the list for that row
    print("")                                                       # Print a newline after the board
    return                                                          # Return from the function


def validateBoardInput(board):                                      # Asks the user to double check their board entries
    printBoard(board)                                               # Print the board
    print("Does this board look correct?")
    print("1) Yes")
    print("2) No")
    errorMessage = "Please select menu option 1 or 2"               # Define an error message for invalid input
    while(1):                                                       # Loop until valid input is given                                                       
        try:                                                        # Try getting valid input from the user
            userInput = int(input("Enter Menu Number: "))           # Assign user's input to a variable
            if (userInput == 1 or userInput == 2):                  # If a valid menu option was selected
                break                                               # Exit the loop
            else:                                                   # If a valid menu option was not selected
                print(errorMessage)                                 # Print error message
        except ValueError:                                          # Initial non-digit character check failed
            print (errorMessage)                                    # Print error message
    return userInput                                                # Return the user's menu selection


def getManualBoard():                                               # Controls getting a valid board manually entered from the user
    Console.clear()                                                 # Clear the console screen
    while(1):                                                       # Loop until a board with only digits is entered
        board = getBoardInput()                                     # Get a manually entered board from the user
        Console.clear()                                             # Clear the console screen
        userInput = validateBoardInput(board)                       # Have user validate board entry
        if (userInput == 1):                                        # If user confirms board is valid
            break                                                   # Exit the loop
        Console.clear()                                             # Clear the console screen before repeating the loop
    return board                                                    # Return the manually entered board


def getBoard():                                                     # Returns either a default board or one manually entered by the user
    userInput = getMenuInput()                                      # Get user's menu choice of default or manual
    if (userInput == 1):                                            # If user chose default
        board = [                                                   # Initialze board to the default one
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]                                       
    else:                                                           # If user chose manual entry
        board = getManualBoard()                                    # Initialize board to the manual entry
    return board                                                    # Return the board
