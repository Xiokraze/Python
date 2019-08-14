import pygame
import Screen as S
import pygame.locals as pl
import os


class Button:
    def __init__(self, x, y, text, width, height, isVisible):
        self.x = x + S.borderW
        self.y = y + S.borderW
        self.width = width
        self.height = height
        self.text = text
        self.textColor = S.textColor
        self.color = S.btnColor
        self.isVisible = isVisible
        self.hovering = False
        self.playSound = True
        self.buttonBorder = (self.x-2, self.y-2, self.width+4, self.height+4)

    def draw(self, screen, hover=None):
        if (self.isVisible):
            pygame.draw.rect(screen, self.color, self.buttonBorder, S.borderW)
            if (self.hovering):
                pygame.draw.rect(screen, S.textColor, self.buttonBorder, S.borderW)
            text = S.wordFont.render(self.text, 1, self.textColor)
            fontSizePixels = S.font.getsize(self.text)
            fontWidth = fontSizePixels[0]
            fontHeight = fontSizePixels[1] + S.fontSize / 2
            screen.blit(text, (self.x + (self.width/2 - fontWidth/2), self.y + (self.height/2 - fontHeight/2)))
        return

    def isOver(self, pos):
        #Pos is the mouse position (x,y) coordinates
        if (pos[0] > self.x and pos[0] < self.x + self.width):
            if (pos[1] > self.y and pos[1] < self.y + self.height):
                return True         
        return False

def initializeGameButtons():
    x = S.screenW - S.buttonW - S.borderW*2
    y = S.getBottomOffset() - S.buttonH - S.borderW * 3

    pauseButton = Button(x, y, "Pause", S.buttonW, S.buttonH, True)
    muteButton = Button(x, y-S.buttonH-S.borderW*2, "Mute", S.buttonW, S.buttonH, True)
    return [pauseButton, muteButton]

def shiftKey(self):
    self.inputString = (
        self.inputString[:self.cursorPosition]
            + event.unicode
            + self.inputString[self.cursorPosition:]
        ).upper()
    return

def backspace(self):
    self.inputString = (
        self.inputString[:max(self.cursorPosition - 1, 0)]
        + self.inputString[self.cursorPosition:]
    )
    return

def addKeyToInput(self, event):
    self.inputString = (
        self.inputString[:self.cursorPosition]
        + event.unicode
        + self.inputString[self.cursorPosition:]
    )
    self.cursorPosition += len(event.unicode)  # Some are empty, e.g. K_UP
    return

def resetInputTextBox(userInput):
    userInput.inputString = ""
    userInput.cursorPosition = 0
    return



#################################################################################
# Modified code from the follow source to handle pygame text input from players #
#################################################################################
"""
Copyright 2017, Silas Gyger, silasgyger@gmail.com, All rights reserved.
Modified from https://github.com/Nearoo/pygame-text-input under the MIT license.
"""
class TextInput:
    def __init__(
            self,
            initialString="",
            fontFamily=S.masterFont,
            fontSize=S.fontSize,
            antialias=True,
            text_color = S.textColor,
            cursor_color=S.textColor,
            ):


        # Text related vars:
        self.antialias = antialias
        self.textColor = text_color
        self.font_size = fontSize
        self.inputString = initialString  # Inputted text
        self.fontObject = pygame.font.Font(fontFamily, fontSize)

        # Cursor related vars:
        self.cursorSurface = pygame.Surface((2, S.fontSize))
        self.cursorSurface.fill(cursor_color)
        self.cursorPosition = len(initialString)  # Inside text
        self.cursorVisible = True  # Switches every self.cursor_switch_ms ms
        self.cursorMS = 400
        self.cursorMSCounter = 0
        self.clock = S.clock

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursorVisible = True
                if event.key == pl.K_BACKSPACE:
                    backspace(self)
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursorPosition = max(self.cursorPosition - 1, 0)
                elif (event.key == pl.KMOD_LSHIFT or event.key == pl.KMOD_RSHIFT):
                    if(False):
                        pass
                    else:
                        shiftKey(self)
                elif event.key == pl.K_RETURN:
                    return True
                else:
                    addKeyToInput(self, event) # TODO FIX

        # Re-render text surface:
        self.surface = self.fontObject.render(self.inputString, self.antialias, self.textColor)

        # Update self.cursor_visible
        self.cursorMSCounter += self.clock.get_time()
        if self.cursorMSCounter >= self.cursorMS:
            self.cursorMSCounter %= self.cursorMS
            self.cursorVisible = not self.cursorVisible

        if self.cursorVisible:
            cursor_y_pos = self.fontObject.size(self.inputString[:self.cursorPosition])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursorPosition > 0:
                cursor_y_pos -= self.cursorSurface.get_width()
            #self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))
            self.surface.blit(self.cursorSurface, (cursor_y_pos, 5))

        self.clock.tick()
        return False

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.inputString

    def get_cursor_position(self):
        return self.cursorPosition

    def set_text_color(self, color):
        self.textColor = color

    def set_cursor_color(self, color):
        self.cursorSurface.fill(color)

    def clear_text(self):
        self.inputString = ""
        self.cursorPosition = 0