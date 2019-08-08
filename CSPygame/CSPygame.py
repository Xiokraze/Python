import pygame
pygame.init()
import Screen
import Media
import Collision
import random

class Player(object):
    def __init__(self, width, height, x, y, screen):            # Player initialization function
        self.width = width                                      # Assign provided width
        self.height = height                                    # Assign provided height
        self.x = x                                              # Assign provided X location
        self.y = y                                              # Assign provided Y location
        self.velocity = 10                                      # Initialize amount to move each step
        self.hitbox = (self.x, self.y, self.width, self.height) # Initialize hitbox location
        self.hitPenalty = -2                                    # Initialize penalty if player gets hit
        self.score = 0                                          # Initialize player score

    def getPlayer(screen):                                      # Creates and returns a player object
        playerImgWidth = 50                                     # Player width
        playerImgHeight = 50                                    # Player height
        xPosition = Screen.width // 2 - playerImgWidth // 2     # Calculate starting X position
        yPosition = Screen.height // 2 - playerImgHeight // 2   # Calculate starting Y position
        return Player(                                          # Return player object
            playerImgWidth,
            playerImgHeight,
            xPosition,
            yPosition,
            screen
        )

    def getInput(self):
        keys = pygame.key.get_pressed()                         # Get player input
        if (keys[pygame.K_LEFT]):                               # Player moves left
            if (self.x > self.velocity):                        # If player has not reached left border
                self.x -= self.velocity                         # Move player left
        if (keys[pygame.K_RIGHT]):                              # Player moves right
            if (self.x < Screen.getRightBorder(self)):          # If player has not reached right border
                self.x += self.velocity                         # Move player right
        if (keys[pygame.K_UP]):                                 # Player moves up
            if (self.y > self.velocity):                        # If player has not reached top border
                self.y -= self.velocity                         # Move player up
        if (keys[pygame.K_DOWN]):                               # Player moves down
            if (self.y < Screen.getBottomBorder(self)):         # If player has not reached bottom border
                self.y += self.velocity                         # Move player down
        self.hitbox = (self.x, self.y, self.width, self.height) # Update hitbox location
        return                                                  # Return from the function

class Professor(object):
    def __init__(self, width, height, screen, image):           # Professor initialization function
        self.width = width                                      # Assign provided width
        self.height = height                                    # Assign provided height
        self.image = image                                      # Assign provided image
        self.velocity = 10                                      # Initialize amount to move each step
        self.stepCount = 0                                      # Initialize step counter
        self.steps = random.randint(20,30)                      # Initialize random number of steps
        self.startLocation = random.randint(1,4)                # Initialize random start location
        self.moveDirection = random.randint(1,4)                # Initialize random movement direction
        self.x = Screen.randomX(self, self.startLocation)       # Initialize random X coordinate
        self.y = Screen.randomY(self, self.startLocation)       # Randomly generate Y coordinate
        self.hitbox = (self.x, self.y, self.width, self.height) # Initialize professor hitbox

    def getInput(screen, professors):                           # Get input of professors
        for professor in professors:                            # Iterate through each professor
            key = professor.moveDirection                       # Get the key, which is a randomly assigned direction

            if (professor.stepCount == professor.steps):        # If step count is equal to max steps
                professor.stepCount = 0                         # Reset it

            if (key == 1):                                      # Professor moves left
                if (professor.x > professor.velocity):          # Check that the professor won't move off the left side of the screen
                    professor.x -= professor.velocity           # Move professor to the left
            if (key == 3):                                      # Professor moves right
                xRight = Screen.getRightBorder(professor)       # Get the right border of the screen
                if (professor.x < xRight):                      # Check that professor won't move off the right side of the screen
                    professor.x += professor.velocity           # Move the professor to the right
            if (key == 2):                                      # Professor moves up
                if (professor.y > professor.velocity):          # Check that the professor won't move off the top of the screen
                    professor.y -= professor.velocity           # Move the professor up
            if (key == 4):                                      # Professor moves down
                yBottom = Screen.getBottomBorder(professor)     # Get the bottom border of the screen
                if (professor.y < yBottom):                     # Check that the professor won't move off the bottom of the screen
                    professor.y += professor.velocity           # Move the professor down

            professor.checkMovement()                           # Change professor's direction if needed
            professor.hitbox = (                                # Initialize professor hitbox parameters
                professor.x, 
                professor.y, 
                professor.width, 
                professor.height
            )
        return                                                  # Return from the function

    def getProfessors(screen):                                  # Returns an array of professor objects
        P1 = Professor(50, 50, screen, Media.exo)               # Create professor object for Exoo
        P2 = Professor(50, 50, screen, Media.jeff)              # Create professor object for Jeff
        P3 = Professor(50, 50, screen, Media.rob)               # Create professor object for Robert
        P4 = Professor(50, 50, screen, Media.aby)               # Create professor object for Abhyankar
        P5 = Professor(50, 50, screen, Media.steve)             # Create professor object for Steve
        P6 = Professor(50, 50, screen, Media.troy)              # Create professor object for Troy
        professors = [P1, P2, P3, P4, P5, P6]                   # Initialize array of professor objects
        return professors                                       # Return the array of professors

    def maxSteps(self):                                         # Returns status of step count vs max step count
        if (self.stepCount + 1 == self.steps):                  # If number of steps reaches the max step count
            return True
        else:                                                   # Increasing 
            return False

    def offScreen(self):                                        # Tests if professor will move off the screen
        movingRight = self.x + self.velocity                    # New X position if professor moves right
        movingLeft = self.x - self.velocity                     # New X position if professor moves left
        movingUp = self.y + self.velocity                       # New Y position if professor moves up
        movingDown = self.y - self.velocity                     # New Y position if professor moves down
        if (movingRight >= Screen.getRightBorder(self)):        # If professor would move off right side of screen
            return True                                         # Return True
        if (movingLeft <= self.velocity):                       # If professor would move off left side of screen
            return True                                         # Return True
        if (movingUp >= Screen.getBottomBorder(self)):          # If professor would move off top of screen
            return True                                         # Return True
        if (movingDown <= self.velocity):                       # If professor would move off bottom of screen
            return True                                         # Return True
        return False                                            # Professor won't move off of screen, so return False

    def checkMovement(self):                                    # Checks if professor reached max steps or will go off screen
        if (self.maxSteps() or self.offScreen()):               # If above is true
            self.stepCount = 0                                  # Reset step count
            self.moveDirection = random.randint(1,4)            # Generate new direction
            self.steps = random.randint(10,20)                  # Generate new step count
        else:                                                   # Professor is still on screen and not at the path's max steps
            self.stepCount += 1                                 # Increase the professor's number of steps
        return                                                  # Return from function

def main():                                                     # Main
    screen = Screen.gameWindow()                                # Initialize game window parameters
    startTime = pygame.time.get_ticks()                         # Initialize game start clock time
    Player1 = Player.getPlayer(screen)                          # Initialize player
    professors = Professor.getProfessors(screen)                # Initialize professors
    running = True                                              # Control variable for game loop
    
    while running:                                              # Run while true
        currentTime = pygame.time.get_ticks()                   # Get clock time since game started
        Screen.setMaxFPS()                                      # Set max frames per second
        for event in pygame.event.get():                        # Event handling, gets all event from the event queue
            if (event.type == pygame.QUIT):                     # Player clicked the window's X to quit
                running = False                                 # Set game loop control variable to false
        Player1.getInput()                                      # Get player 1 input
        Professor.getInput(screen, professors)                  # Get input of professors
        Collision.checkCollision(Player1, professors, screen)   # Check if player collides with any professors
        Screen.updateScreen(Player1, screen, professors)        # Update screen output

if __name__=="__main__":                                        # If module is run as a main program
    main()                                                      # Enter the main loop