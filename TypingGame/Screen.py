import pygame
from random import randint


wordFont = pygame.font.Font("comicbd.ttf", 16)
screenW = 800
screenH = 600
screenGameH = screenH - 100
windowBGColor = (0,0,0)
textColor = (0,255,0)
maxFPS = 20
bottomTxtOffset = 35
maxFallSpeed = 6
clock = pygame.time.Clock()
inputLocation = (1, screenGameH + 1)

def getScreen():
    pygame.display.set_caption("TypingGame")
    return (pygame.display.set_mode((screenW, screenH)))

def drawWords(screen, words):
    for word in words:
        wordText = wordFont.render(word.value, 1, word.textColor)
        screen.blit(wordText, (word.x, word.y))
    return

def drawScreen(screen, words, inputTextBox):
    center = screenW / 2
    clock.tick(maxFPS)
    screen.fill(windowBGColor)
    drawWords(screen, words)
    screen.blit(inputTextBox, (center, screenH - bottomTxtOffset))
    pygame.display.update()
    return