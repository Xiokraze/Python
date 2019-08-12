import pygame
pygame.init()
from Screen import *
from Words import *
import PlayerInput as P
from WordBanks import startGame
import Menu


def checkPlayerQuit(events):
    for event in events:
        if event.type == pygame.QUIT:
            Time.running = False
    return

def updateInputVars(userInput):
    playerInput = userInput.get_text()
    if (playerInput == startGame[0]):
        Word.falling = True
    userInput.input_string = ""
    userInput.cursor_position = 0
    return playerInput

def playGame(wordbank):
    screen = getScreen()
    userInput = P.TextInput()
    playerInput = ""
    words = startGame
    while(Time.running):
        events = pygame.event.get()
        checkPlayerQuit(events)
        if userInput.update(events):
            playerInput = updateInputVars(userInput)
        words = wordObjects(words, playerInput)
        if (Word.falling):
            if (Screen.Time.started):
                words.append(choice(wordbank))
                Screen.Time.started = False
            if (Screen.Time.updateSeconds()):
                words.append(choice(wordbank))
            fallingWords(words)
        drawScreen(screen, words, userInput.get_surface())
    return

def main():
    wordbank = Menu.menu()
    playGame(wordbank)
    pygame.quit()
        

if __name__ == "__main__":
    main()