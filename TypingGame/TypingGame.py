import pygame
pygame.init()
from Screen import *
from Words import *
from random import choice
import PlayerInput

def main():
    screen = getScreen()
    words = wordbank
    frameCount = 0
    playerInput = PlayerInput.TextInput()
    pInput = ""
    running = True
    while(running):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        if playerInput.update(events):
            pInput = playerInput.get_text()
            playerInput.input_string = ""
            playerInput.cursor_position = 0
        words = wordObjects(words) 
        words = removeWords(words, pInput)

        inputTextBox = playerInput.get_surface()
        drawScreen(screen, words, inputTextBox)
        fallingWords(words)
        frameCount += .5
        if (frameCount == maxFPS):
            words.append(choice(wordbank))
            frameCount = 0

        
        
        
    


if __name__ == "__main__":
    main()