import pygame
import pygame.locals as pl
pygame.init()
from Variables import *
from Classes import *
import random


def main():
    Menu.titleScreen()
    userInput = TextInput()
    buttons = Button.initializeGameButtons()
    Events.playMusic(gameMusic)
    while(Time.running):
        events = Get.events()
        Events.checkEvents(events, buttons)
        if userInput.update(events):
            Words.playerInput = Events.updateInputVars(userInput)
        Words.updateWords()
        if (Word.falling):
            if (Time.updateSeconds()):
                Words.words.append(random.choice(Words.gameWords))
            Words.fallingWords(Words.words)
            Draw.gameScreen(
                Get.screen(), 
                Words.words, 
                Word.charsTyped, 
                userInput.get_surface(), 
                Words.score, 
                buttons)
    pygame.quit()
        

if __name__ == "__main__":
    main()