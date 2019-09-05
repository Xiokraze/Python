import math
import pygame
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
 
# Size of break-out blocks
block_width = 23
block_height = 15
 
 
class Block(pygame.sprite.Sprite):
 
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
 
class Ball(pygame.sprite.Sprite):
    speed = 10.0
    x = 0.0
    y = 180.0
    direction = 200
    width = 10
    height = 10
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
    def bounce(self, diff): # horizontal bounce
        self.direction = (180 - self.direction) % 360
        self.direction -= diff
 
    def update(self):
        direction_radians = math.radians(self.direction)
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
        self.rect.x = self.x
        self.rect.y = self.y
 
        # Do we bounce off the top of the screen?
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
 
        # Do we bounce off the left of the screen?
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
 
        # Do we bounce of the right side of the screen?
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1
 
        # Did we fall off the bottom edge of the screen?
        if self.y > 600:
            return True
        else:
            return False
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((white))
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = 0
        self.rect.y = self.screenheight-self.height
 
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width
 

pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Breakout')
 
# Enable this to make the mouse disappear when over our window
pygame.mouse.set_visible(0)
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
 
# Create sprite lists
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
 
# Create the player paddle object
player = Player()
allsprites.add(player)
 
# Create the ball
ball = Ball()
allsprites.add(ball)
balls.add(ball)
 
# The top of the block (y position)
top = 80
 
# Number of blocks to create
blockcount = 32
 
# --- Create blocks
 
# Five rows of blocks
for row in range(5):
    # 32 columns of blocks
    for column in range(0, blockcount):
        # Create a block (color,x,y)
        block = Block(blue, column * (block_width + 2) + 1, top)
        blocks.add(block)
        allsprites.add(block)
    # Move the top of the next row down
    top += block_height + 2
 
# Clock to limit speed
clock = pygame.time.Clock()
 
# Is the game over?
game_over = False
 
# Exit the program?
exit_program = False
 
# Main program loop
while not exit_program:
 
    # Limit to 30 fps
    clock.tick(30)
 
    # Clear the screen
    screen.fill(black)
 
    # Process the events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
 
    # Update the ball and player position as long
    # as the game is not over.
    if not game_over:
        # Update the player and ball positions
        player.update()
        game_over = ball.update()
 
    # If we are done, print game over
    if game_over:
        text = font.render("Game Over", True, white)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 300
        screen.blit(text, textpos)
 
    # See if the ball hits the player paddle
    if pygame.sprite.spritecollide(player, balls, False):
        # The 'diff' lets you try to bounce the ball left or right
        # depending where on the paddle you hit it
        diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)
 
        # Set the ball's y position in case
        # we hit the ball on the edge of the paddle
        ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
        ball.bounce(diff)
 
    # Check for collisions between the ball and the blocks
    deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
 
    # If we actually hit a block, bounce the ball
    if len(deadblocks) > 0:
        ball.bounce(0)
 
        # Game ends if all the blocks are gone
        if len(blocks) == 0:
            game_over = True
 
    # Draw Everything
    allsprites.draw(screen)
 
    # Flip the screen and show what we've drawn
    pygame.display.flip()
 
pygame.quit()
