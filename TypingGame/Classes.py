import Screen as S
import random
import Variables as V
import pygame
import pygame.locals as pl

class Bubble:
    bubbles = []
    def __init__(self):
        self.img = S.bubble
        size = self.img.get_size()
        self.width = size[0]
        self.height = size[1]
        self.x = random.randint(0, V.screenW - self.width)
        self.startX = self.x
        self.y = V.screenH + self.height
        self.speed = random.uniform(.5, 1.5)
        self.maxWobble = 6
        direction = random.choice(["right", "left"])
        self.direction = direction
        self.popCount = 1
        self.popping = False
        self.popFPS = 5

    def draw(self, screen):
        if not (self.popping):
            screen.blit(self.img, (self.x, self.y))
            self.y -= self.speed
            if (self.y <= 0 - S.fontSize - V.borderW):
                self.popping = True
        return

    def updateWobble(self):
        if not (self.popping):
            if (self.direction == "right"):
                self.x += .2
                if (self.x >= 0 + self.startX + self.maxWobble):
                    self.direction = "left"
            else:
                self.x -= .2
                if (self.x <= self.startX - self.maxWobble):
                    self.direction = "right"
        return

    def popBubble(self, screen):
        if (self.popping):
            screen.blit(S.bubblePop[self.popCount // self.popFPS], (self.x, self.y))
            self.popCount += 1
            if (self.popCount > len(S.bubblePop) + 1):
                return True
        return False

class Button:
    def __init__(self, x, y, text, width, height, isVisible):
        self.x = x + V.borderW
        self.y = y + V.borderW
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
            # Border around visible buttonus
            #pygame.draw.rect(screen, self.color, self.buttonBorder, V.borderW)
            if (self.hovering):
                pygame.draw.rect(screen, S.textColor, self.buttonBorder, V.borderW)
            text = S.wordFont.render(self.text, 1, self.textColor)
            fontSizePixels = S.font.getsize(self.text)
            fontWidth = fontSizePixels[0]
            fontHeight = fontSizePixels[1] + S.fontSize / 2
            if (self.text == "Pause"):
                heightMultiplier = V.buttonH
                S.drawGameMenuButton(screen, S.pauseText, heightMultiplier)
            elif (self.text == "Mute"):
                heightMultiplier = V.buttonH * 2 + V.borderW * 2
                S.drawGameMenuButton(screen, S.muteText, heightMultiplier)
            else:
                screen.blit(text, (self.x + (self.width/2 - fontWidth/2), self.y + (self.height/2 - fontHeight/2)))
        return
    
    def isOver(self, pos):
        #Pos is the mouse position (x,y) coordinates
        if (pos[0] > self.x and pos[0] < self.x + self.width):
            if (pos[1] > self.y and pos[1] < self.y + self.height):
                return True         
        return False


class Buttons:
    buttons = []
    numButtons = 0
    def addButton(y, index):
        Buttons.numButtons += 1
        Buttons.buttons.append(Button(
            S.gradeVocabX, 
            y, 
            S.wordsByGrade[index], 
            V.menuButtonW, 
            V.menuButtonH, 
            True)
        )
        return

    def initializeGameButtons():
        x = V.screenW - V.buttonW - V.borderW*2
        y = S.getBottomOffset() - V.buttonH - V.borderW * 3
        pauseButton = Button(x, y, "Pause", V.buttonW, V.buttonH, True)
        muteButton = Button(x, y-V.buttonH-V.borderW*2, "Mute", V.buttonW, V.buttonH, True)
        return [pauseButton, muteButton]

class GameWords:
    gw = None

class Player:
    score = 0

class TextBlink:
    textOn = True

class TextInput:
    def __init__(
            self,
            initialString="",
            fontFamily=V.masterFont,
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


class Time:
    frameTracker = 0
    seconds = 0
    running = True
    playBGMusic = True
    def updateSeconds(delaySeconds=1): # changes seconds interval for printing words
        Time.frameTracker += 1
        if (Time.frameTracker == S.maxFPS * delaySeconds):
            Time.frameTracker = 0
            Time.seconds += 1
            return True
        return False

class Word(object):
    falling = False
    maxCharHeight = 0
    charsTyped = 0
    def __init__(self, value):
        self.value = value
        self.textColor = S.textColor
        self.fallSpeed = Words.getFallSpeed(len(value))

        # Calculate px value for word width and height
        fontSizePx = S.getFontSizePixels(self.value)
        self.width = fontSizePx[0]
        self.height = fontSizePx[1]

        # Get px offset from right border to keep the word on the screen
        xOffset = V.screenW - self.width - V.borderW * 4 - V.buttonW
        self.x = random.randint(0, xOffset)
        self.y = 0

        Word.maxCharHeight = max(self.height, Word.maxCharHeight)

class Words:
    def getFallSpeed(wordLength):
        maxSpeed = S.maxFallSpeed
        if (wordLength == 2): return maxSpeed 
        elif (wordLength == 3): return maxSpeed * .8
        elif (wordLength == 4): return maxSpeed * .6
        elif (wordLength == 5): return maxSpeed * .5
        elif (wordLength == 6): return maxSpeed * .3
        elif (wordLength == 7): return maxSpeed * .3
        else: return maxSpeed * .2

    def removeWords(words, playerInput):
        if (playerInput):
            playerInput = playerInput.split(' ')
            for word in words:
                for p in playerInput:
                    if (p == word.value):
                        words.remove(word)
                        Player.score += len(word.value)
                        Word.charsTyped += len(word.value) + 1
                        break
        return words

    def wordObjects(words, playerInput):
        newWords = []
        for word in words:
            if (type(word) is str):
                newWords.append(Word(word))
            else:
                newWords.append(word)
        return Words.removeWords(newWords, playerInput)

    
    def checkCount(words, wordbank, numWords):
        if (len(words) < numWords):
            for i in range(numWords):
                words.append(random.choice(wordbank))
        return words

    def fallingWords(words):
        for word in words:
            try:
                fall = word.y + word.fallSpeed
                if (fall < V.screenGameH - word.height):
                    word.y += word.fallSpeed
                else:
                    Player.score -= len(word.value)
                    words.remove(word)
            except AttributeError:
                break
        return