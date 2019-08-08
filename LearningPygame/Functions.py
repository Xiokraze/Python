def bulletHitX(bullet, enemy):                                      # Checks if projectile lies within hitbox on X axis
    hitboxLeft = enemy.hitbox[0]                                    # Enemy x-axis left
    hitboxRight = bullet.x - bullet.radius                          # Enemy x-axis right
    bulletLeft = bullet.x + bullet.radius                           # Bullet x-axis left
    bulletRight = enemy.hitbox[0] + enemy.hitbox[2]                 # bullet x-axir right
    if (bulletLeft > hitboxLeft and hitboxRight < bulletRight):     # If projectile is within the enemy hitbox on X axis
        return True                                                 # Return true
    else:                                                           # Projectile is not within the enemy hitbox on X axis
        return False                                                # Return false


def bulletHitY(bullet, enemy):                                      # Checks if projectile lies within hitbox on Y axis
    hitboxTop = enemy.hitbox[1] + enemy.hitbox[3]                   # Top is technically the "bottom" y-axis, but screen pixels start at the top at 0
    hitboxBottom = enemy.hitbox[1]                                  # Enemy y-axis bottom
    bulletTop = bullet.y - bullet.radius                            # Bullet y-axis top
    bulletBottom = bullet.y + bullet.radius                         # Bullet y-axis bottom
    if (bulletTop < hitboxTop and bulletBottom > hitboxBottom):     # If projectile is within the hitbox on y-axis
        return True                                                 # Return true
    else:                                                           # Projectile is not within the hitbox on y-axis
        return False                                                # Return false


def bulletHitsEnemy(bullet, enemy):                                 # Checks if projectile hits on both the X and Y axis
    if (bulletHitX(bullet, enemy)) and (bulletHitY(bullet, enemy)): # If bullet is within both x and y-axis parameters
        return True                                                 # Return true
    else:                                                           # Bullet is not within both x and y-axis parameters
        return False                                                # Return false


def enemyHitX(player, enemy):                                       # Checks if enemy hitbox lies within player hitbox on x-axis
    playerLeft = player.hitbox[0]                                   # Player x-axis left
    playerRight = player.hitbox[0] + player.hitbox[2]               # Player x-axis right
    enemyLeft = enemy.hitbox[0]                                     # Enemy x-axis left
    enemyRight = enemy.hitbox[0] + enemy.hitbox[2]                  # Enemy x-axis right
    if (playerRight > enemyLeft and playerLeft < enemyRight):       # If player has crossed enemy on x-axis
        return True                                                 # Return true
    else:                                                           # Player has not crossed enemy on x-axis
        return False                                                # Return false


def enemyHitY(player, enemy):                                       # Checks if enemy hitbox lies within player hitbox on Y axis
    playerTop = player.hitbox[1] + player.hitbox[3]                 # Top is technically the "bottom" y-axis, but screen pixels start at the top at 0
    playerBottom = player.hitbox[1]                                 # Player y-axis bottom
    enemyTop = enemy.hitbox[1] + enemy.hitbox[3]                    # Enemy y-axis top
    enemyBottom = enemy.hitbox[1]                                   # Enemy y-axis bottom
    if ((playerBottom < enemyTop) and (playerTop > enemyBottom)):   # If player has crossed enemy on y-axis
        return True                                                 # Return true
    else:                                                           # Player has not crossed enemy on y-axis
        return False                                                # Return false


def enemyHitsPlayer(player, enemy):                                 # Checks if enemy hits player
    if (enemyHitX(player, enemy)) and (enemyHitY(player, enemy)):   # If player is within the bounds of both the x and y-axis of the enemy
        return True                                                 # Return true
    else:                                                           # Player is not within the bounds of both the x and y-axis of the enemy
        return False                                                # Return false


def playerJump(player):                                             # Controls player jumping trajectory, flipping the flag causes trajectory 
    if (player.jumpCount >= -10):                                   # If the player's jump count is >= -10
        negative = 1                                                # Flip the negative flag to 1
        if (player.jumpCount < 0):                                  # If the player's jump count is less than 0
            negative = -1                                           # Flip the negative flag to -1
        player.jump(negative)                                       # Jump
    else:                                                           # The jump has completed
        player.isJumping = False                                    # Player is no longer jumping
        player.jumpCount = 10                                       # Reset jump count
    return                                                          # Return from the function


def getPlayerX(player):                                             # Returns player's X axis position
    return (round(player.x + player.width // 2))


def GetPlayerY(player):                                             # Returns player's Y axis position
    return (round(player.y + player.height // 2))


def getPlayerFacing(player):                                        # Returns direction player is facing
    if (player.left):
        return -1
    else:
        return 1


def delayGame(pygame):                                              # Delay the game to make it run slower (so player's can see what's happening)
    i = 0
    delay = 100
    while ( i < delay):
        pygame.time.delay(10)                                       # Amount of time to delay in milliseconds
        i += 1
        for event in pygame.event.get():                            # Get pygame events
            if (event.type == pygame.QUIT):                         # If player clicks the window's X to close
                i = delay + 1
                pygame.quit()                                       # Quit the game
    return
