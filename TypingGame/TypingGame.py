import pygame
import pygame.locals as pl
pygame.init()
from Variables import *
from Classes import *
import random

def playGame(wordbank):
    screen = Get.screen()
    userInput = TextInput()
    buttons = Button.initializeGameButtons()
    playerInput = None
    words = [""]
    Time.running = True
    music = pygame.mixer.music.load(gameMusic)
    pygame.mixer.music.play(-1) 
    while(Time.running):
        events = pygame.event.get()
        Events.checkEvents(events, buttons)
        if userInput.update(events):
            playerInput = Events.updateInputVars(userInput)
        words = Words.wordObjects(words, playerInput)
        words = Words.checkCount(words, wordbank, addWordsTrigger)
        if (Word.falling):
            if (Time.updateSeconds()):
                words.append(random.choice(wordbank))
            Words.fallingWords(words)
            Draw.gameScreen(
                screen, 
                words, 
                Word.charsTyped, 
                userInput.get_surface(), 
                Words.score, 
                buttons
            )
    return

def main():
    Menu.titleScreen()
    playGame( Words.gameWords)
    pygame.quit()
        

if __name__ == "__main__":
    main()