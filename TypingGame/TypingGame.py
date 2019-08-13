import pygame
pygame.init()
import Screen as S
import MainMenu as MM
import Words as W
import PlayerInput as P
import WordBanks as WB
import random

def checkEvents(events, buttons):
    mousePosition = pygame.mouse.get_pos()
    for event in events:
        if (event.type == pygame.QUIT):
            S.Time.running = False
            break
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            for button in buttons:
                if (button.isOver(mousePosition)):
                    if (button.text == "Start"):
                        W.Word.falling = True
                        button.isVisible = False
                        for b in buttons:
                            if (b.text != "Start"):
                                b.isVisible = True
                    if (button.text == "Pause"):
                        if (W.Word.falling):
                           W.Word.falling = False
                        else:
                            W.Word.falling = True
                    
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
    return

def updateInputVars(userInput):
    playerInput = userInput.get_text()
    P.resetInputTextBox(userInput)
    return playerInput

def playGame(wordbank):
    screen = S.getScreen()
    userInput = P.TextInput()
    buttons = P.initializeGameButtons()
    playerInput = ""
    words = WB.startGame
    while(S.Time.running):
        events = pygame.event.get()
        checkEvents(events, buttons)
        if userInput.update(events):
            playerInput = updateInputVars(userInput)
        words = W.wordObjects(words, playerInput)
        if (W.Word.falling):
            if (S.Time.started):
                words.append(random.choice(wordbank))
                S.Time.started = False
            if (S.Time.updateSeconds()):
                words.append(random.choice(wordbank))
            W.fallingWords(words)
            S.drawScreen(screen, words, W.Word.charsTyped, userInput.get_surface(), W.Player.score, buttons)
        else:
            P.drawStartButton(screen, buttons, userInput)

    return

def main():
    wordbank = MM.menu(WB.allWords)
    playGame(wordbank)
    pygame.quit()
        

if __name__ == "__main__":
    main()