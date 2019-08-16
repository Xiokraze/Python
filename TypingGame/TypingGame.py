import pygame
pygame.init()
import Screen as S
import MainMenu as MM
import time
import random
import sys
import Classes as C
import Variables as V

def quitGame():
    S.Time.running = False
    pygame.quit()
    sys.exit(0)

def checkButton(button, buttons):
    if (button.text == "Pause"):
        if (C.Word.falling):
            C.Word.falling = False
        else:
            C.Word.falling = True
    elif (button.text == "Start"): 
        C.Word.falling = True
        S.Time.running = False
        button.isVisible = False
        for b in buttons:
            if (b.text != "Start"):
                b.isVisible = True
    elif (button.text == "Mute"):
        if (S.Time.playBGMusic):
            pygame.mixer.music.pause()
            S.Time.playBGMusic = False
        else:
            pygame.mixer.music.unpause() 
            S.Time.playBGMusic = True
    elif (button.text == "1st"):
        C.GameWords.gw = V.vocab1stGrade
    elif (button.text == "2nd"):
        C.GameWords.gw = V.vocab2ndGrade
    elif (button.text == "3rd"):
        C.GameWords.gw = V.vocab3rdGrade
    elif (button.text == "4th"):
        C.GameWords.gw = V.vocab4thGrade
    elif (button.text == "5th"):
        C.GameWords.gw = V.vocab5thGrade
    elif (button.text == "6th"):
        C.GameWords.gw = V.vocab6thGrade
    elif (button.text == "7th"):
        C.GameWords.gw = V.vocab7thGrade
    elif (button.text == "8th"):
        C.GameWords.gw = V.vocab8thGrade
    return

def checkMousePosition(mousePosition, button):
    if (button.isOver(mousePosition)):
        button.color = S.btnHoverColor
        button.textColor = S.btnTextColor
        button.hovering = True
        if (button.playSound):
            V.menuBtnHover.play()
            button.playSound = False
    else:
        button.color = S.btnColor
        button.textColor = S.btnTextColor
        button.hovering = False
        button.playSound = True
    return

def checkEvents(events, buttons):
    mousePosition = pygame.mouse.get_pos()
    for event in events:
        if (buttons == []):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    S.Time.running = False
            if (event.type == pygame.QUIT):
                quitGame()
        else:
            if (event.type == pygame.QUIT):
                quitGame()
            elif (event.type == pygame.MOUSEMOTION):
                for button in buttons:
                    checkMousePosition(mousePosition, button)
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                for button in buttons:
                    if (button.isOver(mousePosition)):
                        checkButton(button, buttons)
    return

def updateInputVars(userInput):
    playerInput = userInput.get_text()
    P.resetInputTextBox(userInput)
    return playerInput

def playGame(wordbank):
    screen = S.getScreen()
    userInput = C.TextInput()
    buttons = C.Buttons.initializeGameButtons()
    playerInput = None
    words = [""]
    S.Time.running = True
    music = pygame.mixer.music.load(V.gameMusic)
    pygame.mixer.music.play(-1) 
    while(S.Time.running):
        events = pygame.event.get()
        checkEvents(events, buttons)
        if userInput.update(events):
            playerInput = updateInputVars(userInput)
        words = C.Words.wordObjects(words, playerInput)
        words = C.Words.checkCount(words, wordbank, S.numWords)
        if (C.Word.falling):
            if (S.Time.updateSeconds()):
                words.append(random.choice(wordbank))
            C.Words.fallingWords(words)
            S.drawScreen(
                screen, 
                words, 
                C.Word.charsTyped, 
                userInput.get_surface(), 
                C.Player.score, 
                buttons
            )
    return

def main():
    MM.titleScreen()
    #MM.menu(WB.allWords)
    playGame(C.GameWords.gw)
    pygame.quit()
        

if __name__ == "__main__":
    main()