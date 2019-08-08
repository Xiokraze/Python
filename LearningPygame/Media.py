import pygame

# Fonts
playerHitFont = pygame.font.Font('Media/comicbd.ttf', 100)
scoreFont = pygame.font.Font('Media/comicbd.ttf', 30)           

# Images
logo = pygame.image.load("Media/standing.png")              # Load the window logo
backgroundImg = pygame.image.load('Media/bg.jpg')           # Load background
playerOneImage = pygame.image.load('Media/standing.png')    # Load default character image
playerWalkLeft = [                                          # Load images for player walking left
    pygame.image.load('Media/L%s.png' % frame)
    for frame in range(1,10)
]
playerWalkRight = [                                         # Load images for player walking right
    pygame.image.load('Media/R%s.png' % frame)
    for frame in range(1,10)
]
enemyWalkLeft = [                                           # Load images for enemy walking left
    pygame.image.load('Media/L%sE.png' % frame)
    for frame in range(1,12)
]
enemyWalkRight = [                                          # Load images for enemy walking right
    pygame.image.load('Media/R%sE.png' % frame)
    for frame in range(1,12)
]

# Sounds
bulletSound = pygame.mixer.Sound('Media/bulletSound.wav')
bulletHitSound = pygame.mixer.Sound('Media/bulletHitSound.wav')
music = pygame.mixer.music.load('Media/bgmusic.mp3')
pygame.mixer.music.play(-1)