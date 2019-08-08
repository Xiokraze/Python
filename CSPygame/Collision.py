import Screen
import Media
    
def collideX(player, professor):                                # Checks for collision on X axis
    playerLeft = player.hitbox[0]                               # Get player's left most X position
    playerRight = player.hitbox[0] + player.hitbox[2]           # Get player's right most X position
    profLeft = professor.hitbox[0]                              # Get professor's left most X position
    profRight = professor.hitbox[0] + professor.hitbox[2]       # Get professor's right most X position
    if (playerRight > profLeft and playerLeft < profRight):     # If player's X position is between professor's left and right
        return True                                             # X axis collision has happened, return True
    else:                                                       # X axis collision has not happened
        return False                                            # Return False

def collideY(player, professor):                                # Checks for collision on Y axis
    playerTop = player.hitbox[1] + player.hitbox[3]             # Get player's top most Y position
    playerBottom = player.hitbox[1]                             # Get player's bottom most Y position
    profTop = professor.hitbox[1]                               # Get professor's top most Y position
    profBottom = professor.hitbox[1] + professor.hitbox[3]      # Get professor's bottom most Y position
    if ((playerBottom < profBottom) and (playerTop > profTop)): # If player's Y position is between professor's top and bottom
        return True                                             # Y axis collision has happened, return True
    else:                                                       # Y axis collision has not happened
        return False                                            # Return False

def checkCollision(player, professors, screen):
    for professor in professors:                                # Iterate through each professor
        if (collideX(player, professor)):                       # If collision on X axis
            if (collideY(player, professor)):                   # And if collision on Y axis
                player.score += player.hitPenalty               # Player has been hit, add hit penalty to score
                Media.hitSound.play()                           # Play hit sound
        else:                                                   # Player has not been hit
            Screen.countFPS += 1                                # Increment screen frame count
            if (Screen.countFPS == Screen.maxFPS):              # If screen count has reached max frames per second
                Screen.countFPS = 0                             # Reset screen count
                player.score += 1                               # Increment player score
    return                                                      # Return from the function
