import pygame
import Media

width = 600                                                 # Window width
height = 480                                                # Window height
maxFPS = 27                                                 # Number of frames to draw per second
imgFPS = 3                                                  # Number of frames to draw per image
clock = pygame.time.Clock()

def gameWindow():                                           # Set the parameters for the primary game window
    pygame.display.set_icon(Media.logo)                     # Set the logo
    pygame.display.set_caption("My Game")                   # Set window title text
    screen = pygame.display.set_mode((width, height))       # Set screen display mode to width and height
    return screen

def setMaxFPS():                                            # Sets max fames per second for the game
    clock.tick(maxFPS)
    return

def updateScreen(player, screen, bullets, enemy1):          # Primary screen updating function
    screen.blit(Media.backgroundImg, (0,0))                 # Print background image
    text = Media.scoreFont.render(
        'Score: ' + str(player.score), 
        1, 
        (0,0,0)
    )
    screen.blit(text, (width - (width * .25), 10))          # Prints text score to screen
    player.draw(screen)                                     # Draw player 1
    enemy1.draw(screen)                                     # Draw enemy 1
    for bullet in bullets:                                  # Iterate through the bulelts
        bullet.draw(screen)                                 # Draw each bullet to the screen
    pygame.display.update()                                 # Update the display
    return

def getRightBorder(player):                                 # Return the right border of the screen
    return (width - player.width - player.velocity)

def getBottomBorder(player):                                # Return the bottom border of the screen
    return (height - player.height - player.velocity)