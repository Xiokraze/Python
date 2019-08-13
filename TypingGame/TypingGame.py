import pygame
pygame.init()
import Screen as S
import Words as W
import PlayerInput as P
import WordBanks as WB
import random

def checkEvents(events, buttons):
    mousePosition = pygame.mouse.get_pos()
    for event in events:
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            for button in buttons:
                if (button.isOver(mousePosition)):
                    print("Clicked")
        elif (event.type == pygame.MOUSEMOTION):
            for button in buttons:
                if (button.isOver(mousePosition)):
                    button.color = S.btnColor
                    button.textColor = S.textColor
                else:
                    button.color = S.textColor
                    button.textColor = S.btnColor
    return

def updateInputVars(userInput):
    playerInput = userInput.get_text()
    if (playerInput == WB.startGame[0]):
        W.Word.falling = True
    userInput.input_string = ""
    userInput.cursor_position = 0
    return playerInput

def playGame(wordbank):
    screen = S.getScreen()
    userInput = P.TextInput()
    buttons = P.initializeButtons()
    playerInput = ""
    words = WB.startGame
    while(True):
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
    return

def main():
    wordbank = P.menu(WB.allWords)
    playGame(wordbank)
    pygame.quit()
        

if __name__ == "__main__":
    main()