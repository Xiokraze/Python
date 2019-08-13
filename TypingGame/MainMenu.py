import pygame
import Screen as S
import PlayerInput as P


def initializeMenuButtons():
    x = S.screenW / 2 - S.buttonW / 2
    wordsByGrade = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
    buttons = []
    numBorders = 2
    for i in range(len(wordsByGrade)):
        if (i == 0):
            buttons.append(P.Button(x, S.borderW, wordsByGrade[i]))
        else:
            y = S.borderW * numBorders + S.buttonH * (i + 1)
            buttons.append(P.Button(x, y, wordsByGrade[i]))
    return buttons

def drawMenuButtons(buttons):
    screen = S.getScreen()
    for button in buttons:
        button.draw(screen)
        pygame.display.update()

def printMenu():
    #wordsByGrade = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
    #wordsByLength = ("3", "4", "5", "6", "7", "8", "9+")
    #num = 1
    #print("Wordbank Menu")
    #for word in wordsByGrade:
    #    print(f" {num}) {word} Grade Vocabulary")
    #    num += 1
    #for word in wordsByLength:
    #    print(f" {num}) {word} Letter Words")
    #    num += 1
    #return num
    buttons = initializeMenuButtons()
    drawMenuButtons(buttons)


def getInput():
    clearScreen = lambda: os.system('cls')
    while (True):
        try:
            numChoices = printMenu()
            userInput = int(input("Enter Menu Number: "))
            if (userInput > 0 and userInput <= numChoices):
                break
        except ValueError:
            clearScreen()
    clearScreen()
    return userInput

def menu(allWords):
    playerInput = getInput()
    wordbank = allWords[playerInput - 1]
    return wordbank
