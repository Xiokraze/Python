class Solving:                                                      # Class for handling the solving of Sudoku Boards
    numRows = None                                                  # Initialize a class variable for holding the number of rows in a board
    rowSize = None                                                  # Initialize a class variable for holding the size of a row in a board

    def setNumRows(size):                                           # Setter function for setting the number of rows
        Solving.numRows = size                                      # Set numRows to size
        return                                                      # Return from the function
    
    def setRowSize(size):                                           # Setter function for setting the size of a row
        Solving.rowSize = size                                      # Set rowSize to size
        return                                                      # Return from the function


def checkRow(board, number, position):                              # Checks the row for duplicate numbers
    for i in range(Solving.rowSize):                                # Look at each position in the row
        value = board[position[0]][i]                               # Get the positions value position[0] is the row value
        if (value == number and position[1] != i):                  # If the value and number are equal and isn't the one just inserted
            return False                                            # It's not valid, return false
    return True                                                     # No duplicates in the row, so it's valid, return True


def checkCol(board, number, position):                              # Checks the column for duplicate numbers
    for i in range(Solving.numRows):                                # Look at each column (number of rows)
        value = board[i][position[1]]                               # Get the positions value, position[1] is the column value
        if (value == number and position[0] != i):                  # If the value and number are equal and isn't the one just inserted
            return False                                            # It's not valid, return false
    return True                                                     # No duplicates in the column, so it's valid, return True


def checkBox(board, number, position):                              # Checks the 3x3 area the number is in for duplicates
    xBox = position[1] // 3                                         # Divide the row position by 3 to determine box row location
    yBox = position[0] // 3                                         # Divide the column position by 3 to determin box column location
    xStart = xBox * 3                                               # Multiply X position by 3 to get the starting row index
    xEnd = xBox * 3 + 3                                             # Multiply X position by 3, then add 3 to get the ending row index            
    yStart = yBox * 3                                               # Multiply Y position by 3 to get the starting column index
    yEnd = yBox * 3 + 3                                             # Multiply Y position by 3, then add 3 to get the ending column index
    for i in range(yStart, yEnd):                                   # Look at each row in the box
        for j in range(xStart, xEnd):                               # Look at each column in the box
            if (board[i][j] == number and (i,j) != position):       # If a duplicate number exists, box is not valid
                return False                                        # Return False
    return True                                                     # No duplicate numbers exist, box is valid, return True


def isValid(board, number, position):                               # Checks if board is valid
    rowCheck = checkRow(board, number, position)                    # Checks for duplciates in the row
    colCheck = checkCol(board, number, position)                    # Checks for duplicates in the column
    boxCheck = checkBox(board, number, position)                    # Checks for duplicates in the box
    if (rowCheck and colCheck and boxCheck):                        # If row, column, and box are all valid
        return True                                                 # Return True
    else:                                                           # If any of them were not valid (any were False)
        return False                                                # Return False


def findEmpty(board):                                               # Returns first 0 entry location
    for i in range(Solving.numRows):                                # Look at each row
        for j in range(Solving.rowSize):                            # Look at each position within the row
            if (board[i][j] == 0):                                  # If the row has no entry (is 0)
                return (i, j)                                       # Return it's location
    return None                                                     # No empty positions remain, so return None


def solve(board):                                                   # Recursively fills the board, checking for validation
    empty = findEmpty(board)                                        # Get first empty position on the board
    if not(empty):                                                  # If no empty positions remain
        return True                                                 # Board has been solved, return True
    else:                                                           # Else, board has not yet been solved
        row, column = empty                                         # Assign row and column to the position parameters in the empty location
    for i in range(1,10):                                           # Sudoku only uses numbers 1-9, so iterate through them
        if (isValid(board, i, (row, column))):                      # Check if submitted number is a valid entry for the board
            board[row][column] = i                                  # If valid, assign that number to the board
            if (solve(board)):                                      # Recursively submit additional numbers
                return True                                         # Number can be added, continue adding more to the board
            board[row][column] = 0                                  # Reset last element added
    return False                                                    # Looped through all the numbers and none are valid, need to return and change a previous number recursively
