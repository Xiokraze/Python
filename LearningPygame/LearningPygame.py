# Initial tutorial I followed: https://www.youtube.com/watch?v=i6xMBig-pP4

import pygame                                                   # Import the pygame module
pygame.init()                                                   # Initialize pygame module
import Media                                                    # Import media file
import Screen                                                   # Import screen file
import Functions                                                # Import functions file


class Player(object):                                           # Create character parameters
    def __init__(self, width, height, x, y, screen):
        self.width = width                                      # Player width
        self.height = height                                    # Player height
        self.x = x                                              # Player's starting x-axis position
        self.y = y                                              # Player's starting y-axis position
        self.velocity = 5                                       # Amount to move each frame
        self.isJumping = False                                  # Flag for jumping status, initially false
        self.jumpCount = 10                                     # Counter for creating jump trajectory (10 to -10)
        self.left = False                                       # Flag for facing left, initially false
        self.right = True                                       # Flag for facing right, initially true
        self.walkCount = 0                                      # Counter for walking, used to determine sprite images
        self.playerNumber = 1                                   # Player number
        self.isStanding = True                                  # Flag for if player is standing still
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)        # Initial hitbox coordinates
        self.score = 0                                          # Score tracking

    def moveLeft(self):                                         # Player is moving left
        if (self.x > self.velocity):                            # If player has room to move left
            self.x -= self.velocity                             # Move the x-axis left by the velocity amount
            self.left = True                                    # Set left flag to true
            self.right = False                                  # Set right flag to false
            self.isStanding = False                             # set standing flag to false
        return                                                  # Return from the function

    def moveRight(self):                                        # Player is moving right
        if (self.x < Screen.getRightBorder(self)):              # If player has room to move right
            self.x += self.velocity                             # Move the x-axis right by the velocity amount
            self.left = False                                   # Set left flag to false
            self.right = True                                   # Set right flag to true
            self.isStanding = False                             # Set standing flag to false
        return                                                  # Return from the function

    def standing(self):                                         # Player is standing still
        self.isStanding = True                                  # Set standing flag to true
        self.walkCount = 0                                      # Reset walk count
        return                                                  # Return from the function

    def jumping(self):                                          # Player is jumping
        self.isJumping = True                                   # Set jumping flag to true
        self.walkCount = 0                                      # Reset walk count
        return                                                  # Return from the function

    def jump(self, negative):                                   # Jump algorithm 
        self.y -= (self.jumpCount ** 2) * 0.5 * negative        # Quadratic formula for basic jump
        self.jumpCount -= 1                                     # Decrement jump count
        return                                                  # Return from the function

    def draw(self, screen):                                     # Draw player according to their direction
        if ((self.walkCount + 1) >= Screen.maxFPS):
            self.walkCount = 0
        if (self.left):
            screen.blit(Media.playerWalkLeft[self.walkCount // Screen.imgFPS], (self.x, self.y))
            self.walkCount += 1
        elif (self.right):
            screen.blit(Media.playerWalkRight[self.walkCount // Screen.imgFPS], (self.x, self.y))
            self.walkCount += 1
        else:
            if (self.right):
                screen.blit(Media.playerWalkRight[0], (self.x, self.y))
            else:
                screen.blit(Media.playerWalkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)        # Initiate player hitbox coordiates
        return

    def hit(self, screen):
        self.isJumping = False                                  # End jump if jumping
        self.jumpCount = 10                                     # Reset jump count
        hitPenalty = -5                                         # Amount of score to loose if hit
        self.score += hitPenalty                                # Update score
        self.x = 60                                             # Reset player to this X axis coordinate
        self.y = Screen.height - 70                             # Reset player to this Y axis coordinate
        self.walkCount = 0
        text = Media.playerHitFont.render(str(hitPenalty), 1, (255,0,0))
        textX = ((Screen.width // 2) - (text.get_width() // 2))
        textY = (Screen.height // 2)
        screen.blit(text, (textX, textY))                       # Print score loss to the screen
        pygame.display.update()                                 # Update the display
        Functions.delayGame(pygame)                             # Add a delay so the player sees they got hit
        return

    def checkEnemyCollision(player, enemy, screen):             # Checks if enemy and player collide
        if (enemy.visible):                                     # If enemy is visible (not defeated)
            if (Functions.enemyHitsPlayer(player, enemy)):      # Check if they collide
                player.hit(screen)                              # They collided, player gets hit
        return


class Enemy(object):
    def __init__(self, width, height, x, y, end):
        self.width = width                                      # Enemy width
        self.height = height                                    # Enemy height
        self.x = x                                              # Starting x-axis position
        self.y = y                                              # Starting y-axis position
        self.end = end                                          # End of path flag
        self.walkCount = 0                                      # Counter for walking, used to determine sprite images
        self.velocity = 3                                       # Amount to move each frame
        self.path = [self.x, self.end]                          # Path end
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)         # Hitbox parameters
        self.startHealth = 10                                   # Starting health
        self.health = 10                                        # Current health
        self.visible = True                                     # Flag for if enemy is visible
    
    def drawHealthBar(self, screen):                            # Draws enemy health bars
        healthBarSizeX = 50                                     # Health bar width
        healthBarSizeY = 10                                     # Health bar height
        healthBarPosX = self.hitbox[0]                          # Health bar X axis coordinate
        healthBarPosY = self.hitbox[1] - 20                     # Health bar Y axis coordinate
        healthLost = (5 * (self.startHealth - self.health))     # Amount of health currently lost
        remHealthSizeX = healthBarSizeX - healthLost            # Remaining health
        if (remHealthSizeX < 0): remHealthSizeX = 0             # If enemy has health left, draw the health foreground/background
        pygame.draw.rect(screen, (255,0,0), (healthBarPosX, healthBarPosY, healthBarSizeX, healthBarSizeY))
        pygame.draw.rect(screen, (0,128,0), (healthBarPosX, healthBarPosY, remHealthSizeX, healthBarSizeY))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)         # Set enemy hitbox cooridinates
        return

    def draw(self, screen):                                     # Draw enemy to the screen
        self.move()                                             # Move the enemy
        if (self.visible):                                      # If enemy is visible
            if (self.walkCount + 1 >= 33):                      # Check if enemy reached their end path location
                self.walkCount = 0                              # Reset walk count steps to 0
            if (self.velocity > 0):                             # If velocity is positive, enemy is moving right
                screen.blit(                                    # Print walking right images
                    Media.enemyWalkRight[self.walkCount // 3], 
                    (self.x, self.y)
                )
                self.walkCount += 1
            else:                                               # If velocity is negative, enemy is moving left
                screen.blit(                                    # Print walking left images
                    Media.enemyWalkLeft[self.walkCount // 3], 
                    (self.x, self.y)
                )
                self.walkCount += 1
            Enemy.drawHealthBar(self, screen)                   # Draw enemy health bars
            #pygame.draw.rect(                                  # draws hitbox to screen
            #screen, 
            #(255, 0, 0), 
            #self.hitbox, 2)

    def hit(self, player):                                      # Controls what happens when a bullet hits enemies
        player.score += 1                                       # Increase score
        Media.bulletHitSound.play()                             # Play bullet hit sound
        if (self.health > 1):                                   # Check if enemy has remaining health
            self.health -= Projectile.bulletDamage              # If so, deduct bullet damage from health
        else:                                                   # If no health is left
            self.visible = False                                # Set enemy to not visible
            
        return

    def move(self):
        if (self.velocity > 0):                                 # if enemy is moving toward their end location
            if (self.x + self.velocity < self.path[1]):         # if enemy position plus movement amount is less than the path end
                self.x += self.velocity                         # move the enemy by the velocity amount
            else:
                self.velocity = self.velocity * -1              # enemy would move beyond where their path should end, reverse direction
                self.walkCount = 0                              # reset walk count
        else:
            if (self.x - self.velocity > self.path[0]):         # if enemy is moving toward their start location
                self.x += self.velocity                         # move the enemy by the velocity amount
            else:
                self.velocity = self.velocity * -1              # enemy would move beyond where their path started, reverse direction
                self.walkCount = 0                              # reset walk count


class Projectile(object):
    bulletMax = 5                                               # Max number of bullets allowed on screen at once
    shootDelay = 0                                              # Initialize shoot delay variable
    bulletColor = (0,0,0)                                       # Initialize bullet color
    bulletDamage = 3                                            # Initialize bullet damage

    def __init__(self, x, y, color, direction):
        self.x = x                                              # Bullet start x-axis position
        self.y = y                                              # Bullet start y-axis position
        self.radius = 5                                         # Bullet radius in pixels
        self.color = color                                      # Bullet color
        self.direction = direction                              # Direction flag
        self.velocity = 8 * direction

    def draw(self, screen):                                     # Draws the bullet to the screen
        pygame.draw.circle(
            screen, self.color, 
            (self.x, self.y), 
            self.radius
        )
        return

    def checkShootDelay():                                      # Adds a shoot delay
        if (Projectile.shootDelay > 0):
            Projectile.shootDelay += 1
        if (Projectile.shootDelay > 3):
            Projectile.shootDelay = 0
        return

    def isOnScreen(bullet):                                     # Check if bullet is on the screen
        if (bullet.x < Screen.width and bullet.x > 0):          # Check bullet X coordinates
            return True                                         # If within screen borders, return true
        else:                                                   # Bullet is off screen
            return False                                        # Return false since bullet is not on screen

    def shootBullets(player, bullets):                          # Shoots bullets
        Projectile.checkShootDelay()                            # Add a delay so multiple bullets aren't shot at once
        if (Projectile.shootDelay == 0):                        # If no delay, a bullet can be fired
            if(len(bullets) < Projectile.bulletMax):            # Only a max number of bullets can be on screen at once
                x = Functions.getPlayerX(player)                # Get player X coordinate
                y = Functions.GetPlayerY(player)                # Get player Y coordinate
                color = Projectile.bulletColor                  # Get bullet color
                facing = Functions.getPlayerFacing(player)      # Get direction player is facing
                bullets.append(Projectile(x, y, color, facing)) # Add the bullet to the bullets list
                Media.bulletSound.play()                        # Play the shooting bullet sound
            Projectile.shootDelay = 1                           # Add shoot delay
        return

    def checkBullets(enemy, bullets, player):                   # Checks if bullet hit enemy or is off screen
        for bullet in bullets:                                  # Iterate through each bullet
            if (enemy.visible):                                 # Check if the enemy is visible
                if (Functions.bulletHitsEnemy(bullet, enemy)):  # If so, check if bullet hits it
                    enemy.hit(player)                           # Bullet hit the enemy
                    bullets.pop(bullets.index(bullet))          # Delete bullet
            if (Projectile.isOnScreen(bullet)):                 # Check if bullet is still on screen
                bullet.x += bullet.velocity                     # Move bullet
            else:                                               # Bullet is not on screen
                bullets.pop(bullets.index(bullet))              # Delete it
        return


def playerInput(player, bullets):                               # Get movement input from player
    keys = pygame.key.get_pressed()                             # Get player input

    if (keys[pygame.K_LEFT]): player.moveLeft()                 # Player pushes button to move left
    elif (keys[pygame.K_RIGHT]): player.moveRight()             # Player pushes button to move right
    else: player.standing()                                     # Player is standing still

    if (keys[pygame.K_SPACE]):                                  # Player pushes button to shoot
        Projectile.shootBullets(player, bullets)                # Shoot the bullet

    if (not(player.isJumping)):                                 # If player is not jumping
        if (keys[pygame.K_LCTRL]):                              # If player presses jump
                player.jumping()                                # Player jumps is true
    else:                                                       # Player is jumping
        Functions.playerJump(player)                            # Execute the jump
    return


def main():                                                     # Main
    screen = Screen.gameWindow()                                # Initialize the game window screen
    Player1 = Player(64, 64, 50, 410, screen)                   # Initialize player1
    Enemy1 = Enemy(64, 64, 100, 414, 450)                       # Initialize enemy1
    bullets = []                                                # Initialize empty bullets array
    running = True                                              # Define a variable to control the main loop

    while running:                                              # Main loop
        Screen.setMaxFPS()                                      # Set the game's maximum FPS
        for event in pygame.event.get():                        # event handling, gets all event from the event queue
            if (event.type == pygame.QUIT):                     # player clicked the window's X to quit
                running = False                                 # quit the game
        
        Player.checkEnemyCollision(Player1, Enemy1, screen)     # Check if an enemy runs into the player
        Projectile.checkBullets(Enemy1, bullets, Player1)       # Check if the bullets have hit enemies or gone off screen
        playerInput(Player1, bullets)                           # Get input from the player
        Screen.updateScreen(Player1, screen, bullets, Enemy1)   # Update the screen
   
if __name__=="__main__":                                        # Run the main function only if this module is executed as the main script
    main()                                                      # Call the main function