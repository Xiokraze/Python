import pygame
import Screen as S
import PlayerInput as P
from TypingGame import checkEvents
import WordBanks as WB


gradeVocabPrompt = "Grade Level Vocabulary"
gradeMenuX = S.screenW / 2 - S.menuButtonW / 2


def initializeMenuButtons(screen):
    wordsByGrade = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
    buttons = []
    fontSizePixels = S.font.getsize(gradeVocabPrompt)
    buttonGap = 10 # number of pixels between buttons
    topPadding = fontSizePixels[1] + S.borderW
    btnPadding = S.borderW*4
    numBorders = 2
    numButtons = 0
    
    for i in range(len(wordsByGrade)):
        if (i == 0):
            y = topPadding + S.menuButtonH*numButtons + btnPadding*numBorders
            buttons.append(P.Button(gradeMenuX, y, wordsByGrade[i], S.menuButtonW, S.menuButtonH, True))
        else:
            y = topPadding + S.menuButtonH*numButtons + btnPadding*numBorders
            buttons.append(P.Button(gradeMenuX, y, wordsByGrade[i], S.menuButtonW, S.menuButtonH, True))
        numButtons += 1
        numBorders += 2
    return buttons

def drawGradeHeading(screen):
    fontSizePixels = S.font.getsize(gradeVocabPrompt)
    xPadding = (S.menuButtonW - fontSizePixels[0]) / 2
    text = S.wordFont.render(gradeVocabPrompt, 1, S.textColor)
    screen.blit(text, (gradeMenuX + xPadding, 0))
    return

def drawMenu(screen, buttons):
    screen.blit(S.windowBGImg, (0,0))
    drawGradeHeading(screen)
    for button in buttons:
        button.draw(screen)
    pygame.display.update()

def menu(allWords):
    screen = S.getScreen()
    buttons = initializeMenuButtons(screen)
    while (S.Time.running):
        events = pygame.event.get()
        playerInput = checkEvents(events, buttons)
        if (WB.GameWords.gw != None): 
            S.Time.running = False
        drawMenu(screen, buttons)
    S.Time.running = True
    fontSizePixels = S.font.getsize("Start")
    x = S.screenW/2 - S.buttonW / 2
    y = S.screenH/2 - S.buttonH / 2
    buttons = [P.Button(x, y, "Start", S.buttonW, S.buttonH, True)]
    while (S.Time.running):
        events = pygame.event.get()
        playerInput = checkEvents(events, buttons)
        screen.blit(S.windowBGImg, (0,0))
        buttons[0].draw(screen)
        pygame.display.update()
    return
