import pygame
from PIL import ImageFont
from Classes import Time
import Variables as V

#Screen
mainScreenText = pygame.image.load("Media/mainScreenText.png") 
pauseText = pygame.image.load("Media/pause.png")
muteText = pygame.image.load("Media/mute.png")
maxFPS = 40
maxFallSpeed = 2
clock = pygame.time.Clock()

#Title Screen
titleScreenTopPadding = 100
gradeVocabX = V.screenW / 2 - V.menuButtonW / 2
titleScreenMusic = pygame.mixer.music.load("Media/titleScreenMusic.mp3")
bubblePop = [pygame.image.load("Media/bubbles/b%s.png" % img)
           for img in range(2,8)
]
bubble = pygame.image.load("Media/bubbles/b1.png")

#Fonts
masterFont = "Media/ariblk.ttf"
fontSize = 20
wordFont = pygame.font.Font(masterFont, fontSize)
font = ImageFont.truetype(masterFont, fontSize)
textColor = (255,255,255)
btnTextColor = (255,255,255)
btnColor = (44, 150, 199)
btnHoverColor = (194,178,128)

#Falling Words
numWords = 3

# Prompts
blinkDelay = 1
inputPrompt = "Input: "
scorePrompt = "Score: "
gwpmPrompt = "gwpm: "
startPrompt = "Start"
titleScreenPrompt = "Press Enter"
gradeVocabPrompt = "Grade Level Vocabulary"
wordsByGrade = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
inputLeftPadding = 20


def getFontSizePixels(text):
    return font.getsize(text)

def getScreen():
    pygame.display.set_caption("TypingGame")
    return (pygame.display.set_mode((V.screenW, V.screenH)))

def getEvents():
    return pygame.event.get()

def drawWords(screen, words):
    for word in words:
        try:
            wordText = wordFont.render(word.value, 1, word.textColor)
            screen.blit(wordText, (word.x, word.y))
        except:
            break
    return

def drawWordsPerMin(screen, chars, playerScore):
    gwpm = 0
    if (chars != 0 and Time.seconds != 0):
        gwpm = round((chars/5) / (Time.seconds/60))
    fontSizePixels = getFontSizePixels(gwpmPrompt + str(gwpm))
    positionX =  V.screenW // 2 - (fontSizePixels[0] / 2)
    text = wordFont.render(gwpmPrompt + str(gwpm), 1, textColor)
    screen.blit(text, (positionX, getBottomOffset(playerScore)))
    return

def drawButtons(screen, buttons):
    for button in buttons:
        button.draw(screen)

def drawGameMenuButton(screen, img, heightMultiplier):
    size = img.get_size()
    width = size[0]
    height = size[1]
    x = V.screenW - V.buttonW + (V.buttonW - width) / 2
    y = V.screenH - heightMultiplier - V.bottomBoxH + (V.buttonH - height) / 2
    screen.blit(img, (x, y))
    return

def drawBottomBox(screen):
    height = V.screenH - V.bottomBoxH
    leftBorder = 0
    topBorder = height - V.borderW
    rightBorder = V.screenW - V.borderW + 1
    bottomBorder = V.bottomBoxH
    bottomBox = (leftBorder, topBorder, rightBorder, bottomBorder)
    pygame.draw.rect(screen, textColor, bottomBox, V.borderW)

def getBottomOffset(playerScore=""):
    fontSizePixels = getFontSizePixels(scorePrompt + str(playerScore) + str(V.borderW))
    fontHeight = fontSizePixels[1]
    return V.screenH - fontHeight - V.borderW * 3 - ((V.bottomBoxH - fontHeight) // 2)

def getRightOffset(playerScore):
    fontSizePixels = getFontSizePixels(scorePrompt + str(playerScore) + str(V.borderW))
    return V.screenW - V.buttonW - fontSizePixels[0]

def getInputOffset():
    fontSizePixels = getFontSizePixels(inputPrompt)
    return inputLeftPadding + fontSizePixels[0]

def drawInputText(screen, playerScore):
    text = wordFont.render(inputPrompt, 1, textColor)
    screen.blit(text, (inputLeftPadding, getBottomOffset(playerScore)))
    return

def drawScoreText(screen, playerScore):
    text = wordFont.render(scorePrompt + str(playerScore), 1, textColor)
    screen.blit(text, (getRightOffset(playerScore) + V.buttonW, getBottomOffset(playerScore)))
    return

def drawScreen(screen, words, chars, inputTextBox, playerScore, buttons):
    clock.tick(maxFPS)
    screen.blit(V.windowBGImg, (0,0))
    drawWords(screen, words)
    drawButtons(screen, buttons)
    drawBottomBox(screen)
    drawInputText(screen, playerScore)
    drawScoreText(screen, playerScore)
    drawWordsPerMin(screen, chars, playerScore)
    screen.blit(inputTextBox, (getInputOffset(), getBottomOffset(playerScore)))
    pygame.display.update()
    return