import Classes as C
import PlayerInput as P
import pygame
import random
import Screen as S
from TypingGame import checkEvents
import WordBanks as WB


#############################
#       Title Screen        #
#############################

def playMusic():
    music = S.titleScreenMusic
    pygame.mixer.music.play(-1)
    return

def drawTitle(screen):
    size = S.mainScreenText.get_size()
    width = size[0]
    leftPadding = (S.screenW - width) / 2
    screen.blit(S.mainScreenText, (leftPadding, S.titleScreenTopPadding))
    return

def drawTitleScreen(screen, x, y):
    text = S.wordFont.render(S.titleScreenPrompt, 1, S.textColor)
    screen.blit(text, (x, y))
    return

def blinkText(screen):
    if (S.Time.updateSeconds(S.blinkDelay)):
        if (C.TextBlink.textOn):
            C.TextBlink.textOn = False
        else:
            C.TextBlink.textOn = True
    if (C.TextBlink.textOn):
        fontSizePx = S.getFontSizePixels(S.titleScreenPrompt)
        x = S.screenW / 2 - fontSizePx[0] / 2
        y = S.screenH / 2 - fontSizePx[1] / 2 + S.titleScreenTopPadding
        drawTitleScreen(screen, x, y)
    return

def handleTitleScreen(screen):
    playerInput = checkEvents(S.getEvents(), C.Buttons.buttons)
    screen.blit(S.windowBGImg, (0,0))
    drawTitle(screen)
    blinkText(screen)
    return

#############################
#          Bubbles          #
#############################

def drawBubbles(screen):
    for b in C.Bubble.bubbles:
        if not (b.draw(screen)):
            if (b.popBubble(screen)):
                C.Bubble.bubbles.remove(b)
    return

def handleBubbles(screen, frameCount):
    drawBubbles(screen)
    pygame.display.update()
    for b in C.Bubble.bubbles:
        b.updateWobble()
    if (frameCount == 30):
        C.Bubble.bubbles.append(C.Bubble())
        frameCount = 0
    frameCount += 1
    return frameCount

#############################
#      Difficulty Menu      #
#############################

def initializeMenuButtons(screen):
    fontSizePixels = S.getFontSizePixels(S.gradeVocabPrompt)
    topPadding = fontSizePixels[1] + S.borderW
    btnPadding = S.borderW*4
    numBorders = 2   
    for index in range(len(S.wordsByGrade)):
        numButtons = C.Buttons.numButtons
        if (index == 0):
            y = topPadding + S.menuButtonH*numButtons + btnPadding*numBorders
            C.Buttons.addButton(y, index)
        else:
            y = topPadding + S.menuButtonH*numButtons + btnPadding*numBorders
            C.Buttons.addButton(y, index)
        numBorders += 2
    C.Buttons.numButtons = []
    return

def drawGradeHeading(screen):
    fontSizePx = S.getFontSizePixels(S.gradeVocabPrompt)
    xPadding = (S.menuButtonW - fontSizePx[0]) / 2
    text = S.wordFont.render(S.gradeVocabPrompt, 1, S.textColor)
    screen.blit(text, (S.gradeVocabX + xPadding, 0))
    return

def drawMenu(screen):
    screen.blit(S.windowBGImg, (0,0))
    drawGradeHeading(screen)
    for button in C.Buttons.buttons:
        button.draw(screen)
    pygame.display.update()
    return

def handleMenu(screen, frameCount):
    initializeMenuButtons(screen)
    while (S.Time.running):
        playerInput = checkEvents(S.getEvents(), C.Buttons.buttons)
        if (WB.GameWords.gw != None): 
            S.Time.running = False
        frameCount = handleBubbles(screen, frameCount)
        drawMenu(screen)
    S.Time.running = True
    return

def menu(screen, frameCount, bubbles):
    handleMenu(screen, frameCount)
    handleStartScreen(screen)
    return

#############################
#        Start Screen       #
#############################

def handleStartScreen(screen):
    x = S.screenW / 2 - S.buttonW / 2
    y = S.screenH / 2 - S.buttonH / 2
    buttons = [P.Button(x, y, S.startPrompt, S.buttonW, S.buttonH, True)]
    while (S.Time.running):
        playerInput = checkEvents(S.getEvents(), buttons)
        screen.blit(S.windowBGImg, (0,0))
        buttons[0].draw(screen)
        pygame.display.update()

#############################
#     Title Screen Main     #
#############################

def titleScreen():
    screen = S.getScreen()
    playMusic() 
    frameCount = 1
    while (S.Time.running):
        handleTitleScreen(screen)
        frameCount = handleBubbles(screen, frameCount)
        
    frameCount = 1
    S.Time.running = True
    menu(screen, frameCount, C.Bubble.bubbles)
    return