import pygame
import Screen as S
import PlayerInput as P


buttonW = 100
buttonH = 50

def checkEvents(events, buttons):
    mousePosition = pygame.mouse.get_pos()
    for event in events:
        if (event.type == pygame.QUIT):
            S.Time.running = False
            break
        elif (event.type == pygame.MOUSEMOTION):
            for button in buttons:
                if (button.isOver(mousePosition)):
                    button.color = S.btnColor
                    button.textColor = S.textColor
                    button.hovering = True
                else:
                    button.color = S.textColor
                    button.textColor = S.btnColor
                    button.hovering = False
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            for button in buttons:
                if (button.isOver(mousePosition)):
                    if (button.text == "1st"): return 1
                    elif (button.text == "2nd"): return 2
                    elif (button.text == "3rd"): return 3
                    elif (button.text == "4th"): return 4
                    elif (button.text == "5th"): return 5
                    elif (button.text == "6th"): return 6
                    elif (button.text == "7th"): return 7
                    elif (button.text == "8th"): return 8
    return 0


def initializeMenuButtons(screen):
    x = S.screenW / 2 - buttonW / 2
    wordsByGrade = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
    buttons = []
    numBorders = 2
    for i in range(len(wordsByGrade)):
        if (i == 0):
            buttons.append(P.Button(x, S.borderW, wordsByGrade[i], buttonH, True))
        else:
            y = S.borderW * numBorders + buttonH * (i)
            buttons.append(P.Button(x, y, wordsByGrade[i], buttonH, True))
    return buttons

def drawMenu(screen, buttons):
    for button in buttons:
        button.draw(screen)
    pygame.display.update()

def menu(allWords):
    screen = S.getScreen()
    buttons = initializeMenuButtons(screen)

    while (S.Time.running):
        events = pygame.event.get()
        playerInput = checkEvents(events, buttons)
        if (playerInput > 0): break
        drawMenu(screen, buttons)

    wordbank = allWords[playerInput - 1]
    return wordbank
