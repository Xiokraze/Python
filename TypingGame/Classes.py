import pygame
import pygame.locals as pl
import random
from Variables import *
import sys

class Bubble:
    bubbles = []
    def __init__(self):
        self.img = bubble
        size = self.img.get_size()
        self.width = size[0]
        self.height = size[1]
        self.x = random.randint(0, screenW - self.width)
        self.startX = self.x
        self.y = screenH + self.height
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
            if (self.y <= 0 - fontSize - borderW):
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
            screen.blit(bubblePop[self.popCount // self.popFPS], (self.x, self.y))
            self.popCount += 1
            if (self.popCount > len(bubblePop) + 1):
                return True
        return False

    def handleBubbles(screen, frameCount):
        Draw.bubbles(screen)
        pygame.display.update()
        for b in Bubble.bubbles:
            b.updateWobble()
        if (frameCount == 30):
            Bubble.bubbles.append(Bubble())
            frameCount = 0
        frameCount += 1
        return frameCount

class Button:
    buttons = []
    numButtons = 0
    def __init__(self, x, y, text, width, height, isVisible):
        self.x = x + borderW
        self.y = y + borderW
        self.width = width
        self.height = height
        self.text = text
        self.textColor = textColor
        self.color = btnColor
        self.isVisible = isVisible
        self.hovering = False
        self.playSound = True
        self.buttonBorder = (self.x-2, self.y-2, self.width+4, self.height+4)

    def draw(self, screen, hover=None):
        if (self.isVisible):
            # Border around visible buttonus
            #pygame.draw.rect(screen, self.color, self.buttonBorder, borderW)
            if (self.hovering):
                pygame.draw.rect(screen, textColor, self.buttonBorder, borderW)
            text = wordFont.render(self.text, 1, self.textColor)
            fontSizePixels = font.getsize(self.text)
            fontWidth = fontSizePixels[0]
            fontHeight = fontSizePixels[1] + fontSize / 2
            if (self.text == "Pause"):
                heightMultiplier = buttonH
                Draw.gameMenuButtons(screen, pauseText, heightMultiplier)
            elif (self.text == "Mute"):
                heightMultiplier = buttonH * 2 + borderW * 2
                Draw.gameMenuButtons(screen, muteText, heightMultiplier)
            else:
                screen.blit(text, (self.x + (self.width/2 - fontWidth/2), self.y + (self.height/2 - fontHeight/2)))
        return
    
    def isOver(self, pos):
        #Pos is the mouse position (x,y) coordinates
        if (pos[0] > self.x and pos[0] < self.x + self.width):
            if (pos[1] > self.y and pos[1] < self.y + self.height):
                return True         
        return False

    def addButton(y, index):
        Button.numButtons += 1
        Button.buttons.append(Button(
            menuX, 
            y, 
            wordsByGrade[index], 
            menuButtonW, 
            menuButtonH, 
            True)
        )
        return

    def initializeGameButtons():
        x = screenW - buttonW - borderW*2
        fontSizePixels = font.getsize(scorePrompt + str(Words.score) + str(borderW))
        fontHeight = fontSizePixels[1]
        bottomOffset = screenH - fontHeight - borderW * 3 - ((bottomBoxH - fontHeight) // 2)
        y = bottomOffset - buttonH - borderW * 3
        pauseButton = Button(x, y, "Pause", buttonW, buttonH, True)
        muteButton = Button(x, y-buttonH-borderW*2, "Mute", buttonW, buttonH, True)
        return [pauseButton, muteButton]

    def initializeMenuButtons(screen):
        fontSizePixels = font.getsize(gradeVocabPrompt)
        topPadding = fontSizePixels[1] + borderW
        btnPadding = borderW*4
        numBorders = 2   
        for index in range(len(wordsByGrade)):
            numButtons = Button.numButtons
            if (index == 0):
                y = topPadding + menuButtonH*numButtons + btnPadding*numBorders
                Button.addButton(y, index)
            else:
                y = topPadding + menuButtonH*numButtons + btnPadding*numBorders
                Button.addButton(y, index)
            numBorders += 2
        Button.numButtons = []
        return

class Draw:
    def gameMenuButtons(screen, img, heightMultiplier):
        size = img.get_size()
        width = size[0]
        height = size[1]
        x = screenW - buttonW + (buttonW - width) / 2
        y = screenH - heightMultiplier - bottomBoxH + (buttonH - height) / 2
        screen.blit(img, (x, y))
        return

    def inputText(screen, playerScore):
        text = wordFont.render(inputPrompt, 1, textColor)
        screen.blit(text, (inputLeftPadding, Get.bottomOffset(playerScore)))
        return

    def scoreText(screen, playerScore):
        text = wordFont.render(scorePrompt + str(playerScore), 1, textColor)
        screen.blit(text, (Get.rightOffset(playerScore) + buttonW, Get.bottomOffset(playerScore)))
        return

    def words(screen, words):
        for word in words:
            try:
                wordText = wordFont.render(word.value, 1, word.textColor)
                screen.blit(wordText, (word.x, word.y))
            except:
                break
        return

    def wordsPerMin(screen, chars, playerScore):
        gwpm = 0
        if (chars != 0 and Time.seconds != 0):
            gwpm = round((chars/5) / (Time.seconds/60))
        fontSizePixels = font.getsize(gwpmPrompt + str(gwpm))
        positionX =  screenW // 2 - (fontSizePixels[0] / 2)
        text = wordFont.render(gwpmPrompt + str(gwpm), 1, textColor)
        screen.blit(text, (positionX, Get.bottomOffset(playerScore)))
        return

    def buttons(screen, buttons):
        for button in buttons:
            button.draw(screen)

    def bottomBox(screen):
        height = screenH - bottomBoxH
        leftBorder = 0
        topBorder = height - borderW
        rightBorder = screenW - borderW + 1
        bottomBorder = bottomBoxH
        bottomBox = (leftBorder, topBorder, rightBorder, bottomBorder)
        pygame.draw.rect(screen, textColor, bottomBox, borderW)

    def gameScreen(screen, words, chars, inputTextBox, playerScore, buttons):
        clock.tick(maxFPS)
        screen.blit(windowBGImg, (0,0))
        Draw.words(screen, words)
        Draw.buttons(screen, buttons)
        Draw.bottomBox(screen)
        Draw.inputText(screen, playerScore)
        Draw.scoreText(screen, playerScore)
        Draw.wordsPerMin(screen, chars, playerScore)
        screen.blit(inputTextBox, (Get.inputOffset(), Get.bottomOffset(playerScore)))
        pygame.display.update()
        return

    def bubbles(screen):
        for b in Bubble.bubbles:
            if not (b.draw(screen)):
                if (b.popBubble(screen)):
                    Bubble.bubbles.remove(b)
        return

    def titleScreen(screen, x, y):
        text = wordFont.render(titleScreenPrompt, 1, textColor)
        screen.blit(text, (x, y))
        return

    def title(screen):
        size = mainScreenText.get_size()
        width = size[0]
        leftPadding = (screenW - width) / 2
        screen.blit(mainScreenText, (leftPadding, titleScreenTopPadding))
        return

    def gradeHeading(screen):
        fontSizePx = font.getsize(gradeVocabPrompt)
        xPadding = (menuButtonW - fontSizePx[0]) / 2
        text = wordFont.render(gradeVocabPrompt, 1, textColor)
        screen.blit(text, (menuX + xPadding, 0))
        return

    def menu(screen):
        screen.blit(windowBGImg, (0,0))
        Draw.gradeHeading(screen)
        for button in Button.buttons:
            button.draw(screen)
        pygame.display.update()
        return

class Events:
    def playMusic(musicFile):
        music = pygame.mixer.music.load(musicFile)
        pygame.mixer.music.play(-1) 
        return

    def quitGame():
        Time.running = False
        pygame.quit()
        sys.exit(0)

    def checkButton(button, buttons):
        if (button.text == "Pause"):
            if (Word.falling):
                Word.falling = False
            else:
                Word.falling = True
        elif (button.text == "Start"): 
            Word.falling = True
            Time.running = False
            button.isVisible = False
            for b in buttons:
                if (b.text != "Start"):
                    b.isVisible = True
        elif (button.text == "Mute"):
            if (Time.playBGMusic):
                pygame.mixer.music.pause()
                Time.playBGMusic = False
            else:
                pygame.mixer.music.unpause() 
                Time.playBGMusic = True
        elif (button.text == "1st"):
            Words.gameWords = vocab1stGrade
        elif (button.text == "2nd"):
            Words.gameWords = vocab2ndGrade
        elif (button.text == "3rd"):
            Words.gameWords = vocab3rdGrade
        elif (button.text == "4th"):
            Words.gameWords = vocab4thGrade
        elif (button.text == "5th"):
            Words.gameWords = vocab5thGrade
        elif (button.text == "6th"):
            Words.gameWords = vocab6thGrade
        elif (button.text == "7th"):
            Words.gameWords = vocab7thGrade
        elif (button.text == "8th"):
            Words.gameWords = vocab8thGrade
        return

    def checkMousePosition(mousePosition, button):
        if (button.isOver(mousePosition)):
            button.color = btnHoverColor
            button.textColor = btnTextColor
            button.hovering = True
            if (button.playSound):
                menuBtnHover.play()
                button.playSound = False
        else:
            button.color = btnColor
            button.textColor = btnTextColor
            button.hovering = False
            button.playSound = True
        return

    def checkEvents(events, buttons):
        mousePosition = pygame.mouse.get_pos()
        for event in events:
            if (buttons == []):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RETURN):
                        Time.running = False
                if (event.type == pygame.QUIT):
                    Events.quitGame()
            else:
                if (event.type == pygame.QUIT):
                    Events.quitGame()
                elif (event.type == pygame.MOUSEMOTION):
                    for button in buttons:
                        Events.checkMousePosition(mousePosition, button)
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    for button in buttons:
                        if (button.isOver(mousePosition)):
                            Events.checkButton(button, buttons)
        return

    def updateInputVars(userInput):
        playerInput = userInput.get_text()
        TextInput.resetInputTextBox(userInput)
        return playerInput

class Get:
    def screen():
        pygame.display.set_caption("TypingGame")
        return (pygame.display.set_mode((screenW, screenH)))

    def events():
        return pygame.event.get()

    def bottomOffset(playerScore=""):
        fontSizePixels = font.getsize(scorePrompt + str(playerScore) + str(borderW))
        fontHeight = fontSizePixels[1]
        return screenH - fontHeight - borderW * 3 - ((bottomBoxH - fontHeight) // 2)

    def inputOffset():
        fontSizePixels = font.getsize(inputPrompt)
        return inputLeftPadding + fontSizePixels[0]

    def rightOffset(playerScore):
        fontSizePixels = font.getsize(scorePrompt + str(playerScore) + str(borderW))
        return screenW - buttonW - fontSizePixels[0]

class Menu:
    def menu(screen, frameCount, bubbles):
        Menu.handleMenu(screen, frameCount)
        Menu.handleStartScreen(screen)
        return

    def handleMenu(screen, frameCount):
        Button.initializeMenuButtons(screen)
        while (Time.running):
            playerInput = Events.checkEvents(Get.events(), Button.buttons)
            if ( Words.gameWords != None): 
                Time.running = False
            frameCount = Bubble.handleBubbles(screen, frameCount)
            Draw.menu(screen)
        Time.running = True
        return

    def handleStartScreen(screen):
        x = screenW / 2 - buttonW / 2
        y = screenH / 2 - buttonH / 2
        buttons = [Button(x, y, startPrompt, buttonW, buttonH, True)]
        while (Time.running):
            playerInput = Events.checkEvents(Get.events(), buttons)
            screen.blit(windowBGImg, (0,0))
            buttons[0].draw(screen)
            pygame.display.update()

    def handleTitleScreen(screen):
        playerInput = Events.checkEvents(Get.events(), Button.buttons)
        screen.blit(windowBGImg, (0,0))
        Draw.title(screen)
        TextBlink.blink(screen)
        return

    def titleScreen():
        screen = Get.screen()
        Events.playMusic(titleScreenMusic) 
        frameCount = 1
        while (Time.running):
            Menu.handleTitleScreen(screen)
            frameCount = Bubble.handleBubbles(screen, frameCount)      
        frameCount = 1
        Time.running = True
        Menu.menu(screen, frameCount, Bubble.bubbles)
        Time.running = True
        return

class TextBlink: 
    textOn = True
    def blink(screen):
        if (Time.updateSeconds(blinkDelay)):
            if (TextBlink.textOn):
                TextBlink.textOn = False
            else:
                TextBlink.textOn = True
        if (TextBlink.textOn):
            fontSizePx = font.getsize(titleScreenPrompt)
            x = screenW / 2 - fontSizePx[0] / 2
            y = screenH / 2 - fontSizePx[1] / 2 + titleScreenTopPadding
            Draw.titleScreen(screen, x, y)
        return

class TextInput:
    def __init__(
            self,
            initialString="",
            fontFamily=masterFont,
            fontSize=fontSize,
            antialias=True,
            text_color = textColor,
            cursor_color=textColor,
            ):


        # Text related vars:
        self.antialias = antialias
        self.textColor = text_color
        self.font_size = fontSize
        self.inputString = initialString  # Inputted text
        self.fontObject = pygame.font.Font(fontFamily, fontSize)

        # Cursor related vars:
        self.cursorSurface = pygame.Surface((2, fontSize))
        self.cursorSurface.fill(cursor_color)
        self.cursorPosition = len(initialString)  # Inside text
        self.cursorVisible = True  # Switches every self.cursor_switch_ms ms
        self.cursorMS = 400
        self.cursorMSCounter = 0
        self.clock = clock

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursorVisible = True
                if event.key == pl.K_BACKSPACE:
                    TextInput.backspace(self)
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursorPosition = max(self.cursorPosition - 1, 0)
                elif (event.key == pl.KMOD_LSHIFT or event.key == pl.KMOD_RSHIFT):
                    if(False):
                        pass
                    else:
                        TextInput.shiftKey(self)
                elif event.key == pl.K_RETURN:
                    return True
                else:
                    TextInput.addKeyToInput(self, event) # TODO FIX

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
        if (Time.frameTracker == maxFPS * delaySeconds):
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
        self.textColor = textColor
        self.fallSpeed = Words.getFallSpeed(len(value))

        # Calculate px value for word width and height
        fontSizePx = font.getsize(self.value)
        self.width = fontSizePx[0]
        self.height = fontSizePx[1]

        # Get px offset from right border to keep the word on the screen
        xOffset = screenW - self.width - borderW * 4 - buttonW
        self.x = random.randint(0, xOffset)
        self.y = 0

        Word.maxCharHeight = max(self.height, Word.maxCharHeight)

class Words:
    gameWords = None
    score = 0
    playerInput = None
    words = [""]
    def getFallSpeed(wordLength):
        maxSpeed = maxFallSpeed
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
                        Words.score += len(word.value)
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
                if (fall < screenGameH - word.height):
                    word.y += word.fallSpeed
                else:
                    Words.score -= len(word.value)
                    words.remove(word)
            except AttributeError:
                break
        return

    def updateWords():
        Words.words = Words.wordObjects(Words.words, Words.playerInput)
        Words.words = Words.checkCount(Words.words, Words.gameWords, addWordsTrigger)
        return