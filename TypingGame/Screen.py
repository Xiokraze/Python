import pygame
from random import randint
from Words import Word, Player
from PIL import ImageFont

#Screen
screenW = 800
screenH = 600
center = screenW // 2
bottomBoxH = 35
borderWidth = 2
screenGameH = screenH - bottomBoxH
windowBGColor = (0,0,0)
maxFPS = 40
maxFallSpeed = 1
clock = pygame.time.Clock()

#Fonts
masterFont = "ariblk.ttf"
fontSize = 20
wordFont = pygame.font.Font(masterFont, fontSize)
textColor = (0,255,0)

#Input Box
inputPrompt = "Input: "
scorePrompt = "Score: "
gwpmPrompt = "gwpm: "
inputLeftPadding = 20

class Time:
    seconds = 0
    running = True

class Frames:
    frameCount = 0
    fall = False

def getScreen():
    pygame.display.set_caption("TypingGame")
    return (pygame.display.set_mode((screenW, screenH)))

def drawWords(screen, words):
    for word in words:
        try:
            wordText = wordFont.render(word.value, 1, word.textColor)
            screen.blit(wordText, (word.x, word.y))
        except:
            break
    return

def drawWordsPerMin(screen):
    chars = Word.charsTyped
    gwpm = 0
    if (chars != 0 and Time.seconds != 0):
        gwpm = (chars/5) / (Time.seconds/60)
    gwpm = round(gwpm)
    font = ImageFont.truetype(masterFont, fontSize)
    fontSizePixels = font.getsize(gwpmPrompt + str(gwpm))
    positionX =  center - (fontSizePixels[0] / 2)
    text = wordFont.render(gwpmPrompt + str(gwpm), 1, textColor)
    screen.blit(text, (positionX, getBottomOffset()))
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
    font = ImageFont.truetype(masterFont, fontSize)
    fontSizePixels = font.getsize(scorePrompt + str(Player.score) + str(borderWidth))
    fontHeight = fontSizePixels[1]
    return screenH - fontHeight - borderWidth * 3 - ((bottomBoxH - fontHeight) // 2)

def getRightOffset():
    font = ImageFont.truetype(masterFont, fontSize)
    fontSizePixels = font.getsize(scorePrompt + str(Player.score) + str(borderWidth))
    return screenW - fontSizePixels[0]

def getInputOffset():
    font = ImageFont.truetype(masterFont, fontSize)
    fontSizePixels = font.getsize(inputPrompt)
    return inputLeftPadding + fontSizePixels[0]

def drawInputText(screen):
    text = wordFont.render(inputPrompt, 1, textColor)
    screen.blit(text, (inputLeftPadding, getBottomOffset()))
    return

def drawScoreText(screen):
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
    drawWordsPerMin(screen)
    screen.blit(inputTextBox, (getInputOffset(), getBottomOffset()))
    pygame.display.update()
    return