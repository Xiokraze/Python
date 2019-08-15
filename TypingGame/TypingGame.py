import pygame
pygame.init()
import Screen as S
import MainMenu as MM
import Words as W
import time
import PlayerInput as P
import WordBanks as WB
import random
import sys

def quitGame():
    S.Time.running = False
    pygame.quit()
    sys.exit(0)

def checkButton(button, buttons):
    if (button.text == "Pause"):
        if (W.Word.falling):
            W.Word.falling = False
        else:
            W.Word.falling = True
    elif (button.text == "Start"): 
        W.Word.falling = True
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
        WB.GameWords.gw = WB.allWords[0]
    elif (button.text == "2nd"):
        WB.GameWords.gw = WB.allWords[1]
    elif (button.text == "3rd"):
        WB.GameWords.gw = WB.allWords[2]
    elif (button.text == "4th"):
        WB.GameWords.gw = WB.allWords[3]
    elif (button.text == "5th"):
        WB.GameWords.gw = WB.allWords[4]
    elif (button.text == "6th"):
        WB.GameWords.gw = WB.allWords[5]
    elif (button.text == "7th"):
        WB.GameWords.gw = WB.allWords[6]
    elif (button.text == "8th"):
        WB.GameWords.gw = WB.allWords[7]
    return

def checkMousePosition(mousePosition, button):
    if (button.isOver(mousePosition)):
        button.color = S.btnHoverColor
        button.textColor = S.btnTextColor
        button.hovering = True
        if (button.playSound):
            S.menuBtnHover.play()
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
    userInput = P.TextInput()
    buttons = P.initializeGameButtons()
    playerInput = None
    words = [""]
    S.Time.running = True
    music = pygame.mixer.music.load("Media/gameMusic1.mp3")
    pygame.mixer.music.play(-1) 
    while(S.Time.running):
        events = pygame.event.get()
        checkEvents(events, buttons)
        if userInput.update(events):
            playerInput = updateInputVars(userInput)
        words = W.wordObjects(words, playerInput)
        words = W.checkCount(words, wordbank, S.numWords)
        if (W.Word.falling):
            if (S.Time.updateSeconds()):
                words.append(random.choice(wordbank))
            W.fallingWords(words)
            S.drawScreen(
                screen, 
                words, 
                W.Word.charsTyped, 
                userInput.get_surface(), 
                W.Player.score, 
                buttons
            )
    return

def main():
    MM.titleScreen()
    #MM.menu(WB.allWords)
    playGame(WB.GameWords.gw)
    pygame.quit()
        

if __name__ == "__main__":
    main()