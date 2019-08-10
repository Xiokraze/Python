import pygame
from random import randint
from Words import Word, Player
from PIL import ImageFont

#Screen
screenW = 800
screenH = 600
center = screenW // 2
bottomBoxH = 50
borderWidth = 2
screenGameH = screenH - bottomBoxH
windowBGColor = (0,0,0)
maxFPS = 30
maxFallSpeed = 6
clock = pygame.time.Clock()

#Fonts
masterFont = "ariblk.ttf"
fontSize = 20
wordFont = pygame.font.Font(masterFont, fontSize)
textColor = (0,255,0)

#Input Box
inputPrompt = "Input: "
scorePrompt = "Score: "
inputLeftPadding = 20

def getScreen():
    pygame.display.set_caption("TypingGame")
    return (pygame.display.set_mode((screenW, screenH)))

def drawWords(screen, words):
    for word in words:
        wordText = wordFont.render(word.value, 1, word.textColor)
        screen.blit(wordText, (word.x, word.y))
    return

def drawBottomBox(screen):
    height = screenH - bottomBoxH
    leftBorder = 0
    topBorder = height - borderWidth
    rightBorder = screenW - borderWidth + 1
    bottomBorder = bottomBoxH
    bottomBox = (leftBorder, topBorder, rightBorder, bottomBorder)
    pygame.draw.rect(screen, textColor, bottomBox, borderWidth)

def getBottomOffset():
    return screenH - int((bottomBoxH + borderWidth * 2) / 4 * 3)

def getRightOffset():
    font = ImageFont.truetype(masterFont, fontSize)
    fontSizePixels = font.getsize(scorePrompt + str(Player.score) + str(borderWidth))
    return screenW - fontSizePixels[0]

def getInputOffset():
    font = ImageFont.truetype(masterFont, fontSize)
    fontSizePixels = font.getsize(inputPrompt)
    return inputLeftPadding + fontSizePixels[0]

def drawInputText(screen):
    fontText = pygame.font.Font(masterFont, fontSize)
    text = wordFont.render(inputPrompt, 1, textColor)
    screen.blit(text, (inputLeftPadding, getBottomOffset()))
    return

def drawScoreText(screen):
    fontText = pygame.font.Font(masterFont, fontSize)
    text = wordFont.render(scorePrompt + str(Player.score), 1, textColor)
    screen.blit(text, (getRightOffset(), getBottomOffset()))
    return

def drawScreen(screen, words, inputTextBox):
    clock.tick(maxFPS)
    screen.fill(windowBGColor)
    drawWords(screen, words)
    drawBottomBox(screen)
    drawInputText(screen)
    drawScoreText(screen)
    screen.blit(inputTextBox, (getInputOffset(), getBottomOffset()))
    pygame.display.update()
    return