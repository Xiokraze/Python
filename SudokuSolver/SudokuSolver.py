# Initial guide for basic logic https://www.youtube.com/watch?v=eqUwSA0xI-s&t=732s

import pygame
pygame.init()
import copy
import Screen
import Input
import Solve


def solveBoard(board):                                              # Sets the Solve class's variables and solves the puzzle
    Solve.Solving.setNumRows(len(board))                            # Set Solve class's numRows variable
    Solve.Solving.setRowSize(len(board[0]))                         # Set Solve class's rowSize variable
    Solve.solve(board)                                              # Solve the board
    return                                                          # Return from the function


def main():                                                         # Primary program function
    board = Input.getBoard()                                        # Get the board option from the user
    original = copy.deepcopy(board)                                 # Save the original board to a variable
    solveBoard(board)                                               # Set the Solve Class variables and solve the board
    screen = Screen.gameWindow()                                    # Initialize screen/window parameters

    running = True                                                  # Initialize variable for tracking the window loop
    while(running):                                                 # While the window is open
        for event in pygame.event.get():                            # Get the user input vents from pygame
            if (event.type == pygame.QUIT):                         # If user closes the window
                running = False                                     # Set running to false to exit the loop
        Screen.updateScreen(screen, original, board)                # Update the screen


if __name__=="__main__":                                            # If module is run as a main program
    main()                                                          # Enter the main loop
