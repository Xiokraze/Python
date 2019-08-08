import pygame
import Media
import random

totalHeight = 640                                               # Total height of game window
height = 600                                                    # Height of playable area
width = 600                                                     # Width of game window
maxFPS = 20                                                     # Number of frames to draw per second
countFPS = 0                                                    # Tracks current frame count
imgFPS = 4                                                      # Number of frames an image will take up
boxColor = (0,0,255)                                            # Initialize reuseable window border color
boxWidth = 2                                                    # Initialize reuseable window border width
bgFillColor = (0,0,0)                                           # Initialize background fill color
scoreColor = (255,255,255)                                      # Initialize the color of the score text
screenBox = (0, 0, width, height)                               # Initialize window border
scoreBox = (0, height, width, totalHeight - height)             # Initialize score box location
scoreOffsetX = 50                                               # Initialize variable to offset score position
scoreTextX = width // 2 - scoreOffsetX                          # Initialize score X location
clock = pygame.time.Clock()                                     # Initialize time object to track time

def gameWindow():                                               # Define the game's window settings
    pygame.display.set_icon(Media.logo)                         # Set the logo
    pygame.display.set_caption("My Game")                       # Set window title text
    screen = pygame.display.set_mode((width, totalHeight))      # Set screen display mode to width and height
    return screen                                               # Return window/screen object

def drawProfessors(professors, screen):                         # Draws the professors to the screen
    for professor in professors:                                # For each porofessor
        screen.blit(professor.image, (professor.x, professor.y))# Update their position to the screen
        pygame.draw.rect(screen, boxColor, professor.hitbox, 2) # Draw the professor's hitbox to the screen
    return                                                      # Return from the function                                                      # Return from the function

def drawBorders(screen):                                        # Draws window and score borders
    pygame.draw.rect(screen, boxColor, screenBox, boxWidth)     # Draw the screen border
    pygame.draw.rect(screen, boxColor, scoreBox, boxWidth)      # Draw the score border
    return                                                      # Return from the function

def updateScreen(player, screen, professors):                   # Screen drawing/updating function
    scoreString = 'Score: ' + str(player.score)                 # Update the score string to be printed to screen
    scoreText = Media.scoreFont.render(scoreString,1,scoreColor)# Update the score string text with color, font, and size
    screen.fill(bgFillColor)                                    # Fill the screen with the background color
    screen.blit(scoreText, (scoreTextX, height + boxWidth))     # Draw the score text
    screen.blit(Media.josh, (player.x, player.y))               # Draw the player
    drawBorders(screen)                                         # Draw the window and score borders
    drawProfessors(professors, screen)                          # Draw the professors
    pygame.display.update()                                     # Update the display
    return                                                      # Return from the function

def setMaxFPS():                                                # Sets max fames per second for the game
    clock.tick(maxFPS)                                          # Set ticks to the maxFPS variable
    return                                                      # Return from the function

def getRightBorder(player):                                     # Get right border of screen
    return (width - player.width - player.velocity)             # Return right border

def getBottomBorder(player):                                    # Get bottom border of screen
    return (height - player.height - player.velocity)           # Return bottom border

def randomX(professor, startSide):                              # Generates random X starting location
    min = 0 + professor.velocity                                # Initialize min 
    max = (width - professor.velocity - professor.width)        # Initialize max
    if (startSide == 1): return min                             # If the starting side is left, return min value
    elif (startSide == 3): return max                           # If the starting side is right, return max value
    else:                                                       # Starting side is top or bottom
        return random.randint(min, max + 1)                     # Return random value between min and max

def randomY(professor, startSide):                              # Generates random Y starting location
    min = 0 + professor.velocity                                # Initialize min
    max = (height - professor.velocity - professor.height)      # Initialize max
    if (startSide == 2): return min                             # If starting side is top, return min value
    elif (startSide == 4): return max                           # If starting side is bottom, return max value
    else:                                                       # Starting side is left or right
        return random.randint(min, max + 1)                     # Return ranom value between min and max