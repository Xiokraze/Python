import pygame
from random import randint
from Words import Word

#Screen
screenW = 800
screenH = 600
bottomBoxH = 100
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

#Bottom Box
inputLocation = (1, screenGameH + 1)

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
    bottomBox = (0, height, screenW, height)
    pygame.draw.rect(screen, textColor, bottomBox, borderWidth)

def drawScreen(screen, words, inputTextBox):
    center = screenW // 2
    clock.tick(maxFPS)
    screen.fill(windowBGColor)
    drawWords(screen, words)
    drawBottomBox(screen)
    bottomTxtOffset = Word.maxCharHeight
    screen.blit(inputTextBox, (center, screenH - bottomTxtOffset))
    pygame.display.update()
    return