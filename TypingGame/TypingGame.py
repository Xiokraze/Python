import pygame
pygame.init()
from Screen import *
from Words import *
import PlayerInput
from WordBanks import startGame


def checkPlayerQuit(events):
    for event in events:
        if event.type == pygame.QUIT:
            Time.running = False
    return

def updateInputVars(userInput):
    playerInput = userInput.get_text()
    if (playerInput == "begin"):
        Frames.fall = True
    userInput.input_string = ""
    userInput.cursor_position = 0
    return playerInput

def playGame():
    screen = getScreen()
    userInput = PlayerInput.TextInput()
    playerInput = ""
    words = startGame
    wordbank = getWordBank() #TODO pass difficulty parameter to return appripriate word bank

    while(Time.running):
        events = pygame.event.get()
        checkPlayerQuit(events)
        if userInput.update(events):
            playerInput = updateInputVars(userInput)
        words = wordObjects(words, playerInput)
        if (Frames.fall):
            words = drawUpdateWords(words, wordbank)
            fallingWords(words)
        drawScreen(screen, words, userInput.get_surface())
    return

def main():
    playGame()
    pygame.quit()
        

if __name__ == "__main__":
    main()