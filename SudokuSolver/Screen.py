import pygame
import Solve

width = 725                                                         # Window width
height = 390                                                        # Window height
backgroundColor = (0,255,0)                                         # Background color
textColor = (0,0,0)                                                 # Text color
textFont = pygame.font.Font('comicbd.ttf', 30)                      # Text font
lineWidth = 3                                                       # Line width

def gameWindow():                                                   # Initialize the output window
    pygame.display.set_caption("Sudoku Solver")                     # Set window title text
    screen = pygame.display.set_mode((width, height))               # Set screen display mode
    return screen                                                   # Return window/screen object

def writeHeaders(screen):                                           # Writes the text headers to the screen
    originalString = 'Original'                                     # First board's title
    solvedString = 'Solved'                                         # Second board's title
    originalText = textFont.render(originalString, 1, textColor)    # Initialize first title's text parameters
    solvedText = textFont.render(solvedString, 1, textColor)        # Initialize second title's text parameters
    screen.blit(originalText, (133, 5))                             # Draw first title to the screen
    screen.blit(solvedText, (490, 5))                               # Draw the second title to the screen
    return                                                          # Return from the function

def drawBoard(screen, board, isSolved):                             # Draws the board numbers to the screen
    if (isSolved):                                                  # If the board being printed has been solved
        xOffset = 350                                               # Add an X-axis offset for printing the second board
    else:                                                           # If the board being printed has not been solved
        xOffset = 0                                                 # No X-axis offset is needed
    offset = 30                                                     # Amount of pixels used for each number's position
    offsetWithLine = 40                                             # amount of pixels used for a number's position that includes a line
    startX = 50                                                     # Starting X-axis coordinate
    startY = 50                                                     # Starting Y-axis coordinate

    for i in range(Solve.Solving.numRows):                          # Outer loop for updating X and Y axis coordinates with each row
        solvedStartX = startX + xOffset                             # Initialize/reset X-axis starting location
        solvedStartY = 50                                           # Initialize/reset Y-axis location
        for j in range(Solve.Solving.numRows):                      # After updating X/Y location, look at each row
            for k in range(Solve.Solving.rowSize):                  # Iterate through each position in the row
                numString = str(board[j][k])                        # Get the value at the current row/column
                numText = textFont.render(numString, 1, textColor)  # Initialize the value's text parameters
                screen.blit(numText, (solvedStartX, solvedStartY))  # Draw the value to the screen
                if (k == 2 or k == 5):                              # If 3 X-axis values have been printed
                    solvedStartX += offsetWithLine                  # Increase X-axis offset for the number and line
                else:                                               # If 3 values have not been printed
                    solvedStartX += offset                          # Add the X-axis offset for just the number 
            if (j == 2 or j == 5):                                  # If 3 Y-axis values have been printed
                solvedStartY += offsetWithLine                      # Increase Y-axis offset for the number and line
            else:                                                   # If 3 Y-axis values have not been printed
                solvedStartY += offset                              # Add the Y axis offset for just the number
            solvedStartX = startX + xOffset                         # Update X-axis location
    return                                                          # Return from the function

def drawLines(screen, isSolved):                                    # Draws the grid lines to the screen
    if (isSolved):                                                  # If the board being printed has been solved
        xOffset = 400                                               # Add an X-axis offset for printing the second board's gridlines
    else:                                                           # If the board being printed has not been solved
        xOffset = 50                                                # No X-axis offset for the gridlines is needed
    rowWidth = 284                                                  # Initialize row line width
    colWidth = 306                                                  # Initialize column line width
    y = 50                                                          # Initialize starting y-axis coordinate
    rowEndX = xOffset + rowWidth                                    # End X-axis coordinate for row lines
    colEndY = y + colWidth                                          # End Y-axis coordinate for column lines
    xOffset1 = xOffset + lineWidth * 2 + 80                         # Starting X-axis coordinate for first column line
    xOffset2 = xOffset + lineWidth * 3 + 180                        # Starting X-axis coordinate for second column line
    yOffset1 = y + lineWidth * 2 + 95                               # Starting Y-axis coordinate for first row line
    yOffset2 = y + lineWidth * 3 + 195                              # Starting Y-axis coordinate for second row line
    pygame.draw.line(                                               # Draw first column line to the screen
        screen,                                                     # Screen/window to draw to
        textColor,                                                  # Color of the text to draw
        (xOffset1, y),                                              # Starting X/Y coordinate 
        (xOffset1, colEndY),                                        # Ending X/Y coordinate 
        lineWidth)                                                  # Width of the line to draw
    pygame.draw.line(                                               # Draw second column line to the screen
        screen,                                                     # Screen/window to draw to 
        textColor,                                                  # Color of the text to draw 
        (xOffset2, y),                                              # Starting X/Y coordinate  
        (xOffset2, colEndY),                                        # Ending X/Y coordinate
        lineWidth)                                                  # Width of the line to draw
    pygame.draw.line(                                               # Draw the first row line to the screen
        screen,                                                     # Screen/window to draw to 
        textColor,                                                  # Color of the text to draw 
        (xOffset-10, yOffset1),                                     # Starting X/Y coordinate  
        (rowEndX, yOffset1),                                        # Ending X/Y coordinate 
        lineWidth)                                                  # Width of the line to draw
    pygame.draw.line(                                               # Draw the second row line to the screen
        screen,                                                     # Screen/window to draw to 
        textColor,                                                  # Color of the text to draw 
        (xOffset-10, yOffset2),                                     # Starting X/Y coordinate  
        (rowEndX, yOffset2),                                        # Ending X/Y coordinate 
        lineWidth)                                                  # Width of the line to draw
    pygame.draw.rect(                                               # Draw the board's border to the screen
        screen,                                                     # Screen/window to draw to 
        textColor,                                                  # Color of the text to draw 
        (xOffset-10, y, rowWidth + 13, colWidth),                   # Starting and Ending X/Y coordinates 
        lineWidth)                                                  # Width of the line to draw
    return                                                          # Return from the function

def updateScreen(screen, board1, board2):                           # Controls updating all parameters to the display
    screen.fill(backgroundColor)                                    # Fill the background
    writeHeaders(screen)                                            # Write the board title headers
    isSolved = False                                                # Initialize solved to false
    drawBoard(screen, board1, isSolved)                             # Draw the original board's numbers to the screen
    drawLines(screen, isSolved)                                     # Draw the original board's lines to the screen
    isSolved = True                                                 # Set solved to true
    drawBoard(screen, board2, isSolved)                             # Draw the solved board's numbers to the screen
    drawLines(screen, isSolved)                                     # Draw the solved board's lines to the screen
    pygame.display.update()                                         # Update the display
    return                                                          # Return from the function