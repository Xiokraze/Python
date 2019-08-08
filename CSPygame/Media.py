import pygame

# Fonts
scoreFont = pygame.font.Font('Media/comicbd.ttf', 20)           # Load score font

# Images
logo = pygame.image.load("Media/logo.png")
josh = pygame.image.load("Media/josh.jpg")
exo = pygame.image.load("Media/exo.jpg")
jeff = pygame.image.load("Media/jeff.jpg")
rob = pygame.image.load("Media/rob.jpg")
troy = pygame.image.load("Media/troy.jpg")
steve = pygame.image.load("Media/steve.jpg")
aby = pygame.image.load("Media/aby.jpg")

# Sounds
music = pygame.mixer.music.load('Media/bgmusic.mp3')            # Load background music
pygame.mixer.music.play(-1)                                     # Play the background music on a continuous loop
hitSound = pygame.mixer.Sound('Media/hit.wav')                  # Load player hit sound

# References
# logo:     http://mcaagreatfutures.org/university/indiana-state-university/
# music:    https://www.dl-sounds.com/royalty-free/defense-line/
# hitSound: https://freesound.org/people/LittleRobotSoundFactory/sounds/270335/
# jef, exo  http://statemagazine.com/256/
# rob, troy, steve, aby http://cs.indstate.edu/info/people.php