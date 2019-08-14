import pygame
import Screen as S
import PlayerInput as P
from TypingGame import checkEvents
import WordBanks as WB

buttonW = 100
buttonH = 50
gradeVocabPrompt = "Grade Level"
gradeMenuX = S.screenW / 4 - buttonW / 2

#def checkEvents(events, buttons):
#    mousePosition = pygame.mouse.get_pos()
#    for event in events:
#        if (event.type == pygame.QUIT):
#            S.Time.running = False
#            break
#        elif (event.type == pygame.MOUSEMOTION):
#            for button in buttons:
#                if (button.isOver(mousePosition)):
#                    button.color = S.btnHoverColor
#                    button.textColor = S.btnTextColor
#                    button.hovering = True
#                else:
#                    button.color = S.btnColor
#                    button.textColor = S.btnTextColor
#                    button.hovering = False
#        elif (event.type == pygame.MOUSEBUTTONDOWN):
#            for button in buttons:
#                if (button.isOver(mousePosition)):
#                    if (button.text == "Start"): return 0
#                    elif (button.text == "1st"): return 1
#                    elif (button.text == "2nd"): return 2
#                    elif (button.text == "3rd"): return 3
#                    elif (button.text == "4th"): return 4
#                    elif (button.text == "5th"): return 5
#                    elif (button.text == "6th"): return 6
#                    elif (button.text == "7th"): return 7
#                    elif (button.text == "8th"): return 8
#    return 0


def initializeMenuButtons(screen):
    wordsByGrade = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
    buttons = []
    fontSizePixels = S.font.getsize(gradeVocabPrompt)
    topPadding = fontSizePixels[1] + S.borderW
    btnPadding = 5
    numBorders = 2
    numButtons = 0
    for i in range(len(wordsByGrade)):
        if (i == 0):
            y = topPadding + btnPadding*numBorders + buttonH*numButtons
            buttons.append(P.Button(gradeMenuX, y, wordsByGrade[i], buttonH, True))
        else:
            y = topPadding + btnPadding*numBorders + buttonH*numButtons
            buttons.append(P.Button(gradeMenuX, y, wordsByGrade[i], buttonH, True))
        numButtons += 1
        numBorders += 2
    return buttons

def drawGradeHeading(screen):
    fontSizePixels = S.font.getsize(gradeVocabPrompt)
    xPadding = (S.buttonW - fontSizePixels[0]) / 2
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
            break
        drawMenu(screen, buttons)
    return
