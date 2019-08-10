import pygame
pygame.init()
from Screen import *
from Words import *
from random import choice
import PlayerInput

def main():
    screen = getScreen()
    wordbank = getWordBank()
    words = ["begin"]
    frameCount = 0
    userInput = PlayerInput.TextInput()
    playerInput = ""
    running = True

    while(running):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if userInput.update(events):
            playerInput = userInput.get_text()
            userInput.input_string = ""
            userInput.cursor_position = 0

        words = wordObjects(words) 
        words = removeWords(words, playerInput)

        inputTextBox = userInput.get_surface()
        drawScreen(screen, words, inputTextBox)
        fallingWords(words)
        frameCount += .5
        if (frameCount == maxFPS):
            words.append(choice(wordbank))
            frameCount = 0

        
        
        
    


if __name__ == "__main__":
    main()