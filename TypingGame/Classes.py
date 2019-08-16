import PlayerInput as P # need to move classes to here
import Screen as S
import random
import Words as W
import Variables as V

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

class Buttons:
    buttons = []
    numButtons = 0
    def addButton(y, index):
        Buttons.numButtons += 1
        Buttons.buttons.append(P.Button(
            S.gradeVocabX, 
            y, 
            S.wordsByGrade[index], 
            V.menuButtonW, 
            V.menuButtonH, 
            True)
        )
        return

class Player:
    score = 0

class TextBlink:
    textOn = True

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
        self.fallSpeed = W.getFallSpeed(len(value))

        # Calculate px value for word width and height
        fontSizePx = S.getFontSizePixels(self.value)
        self.width = fontSizePx[0]
        self.height = fontSizePx[1]

        # Get px offset from right border to keep the word on the screen
        xOffset = V.screenW - self.width - V.borderW * 4 - V.buttonW
        self.x = random.randint(0, xOffset)
        self.y = 0

        Word.maxCharHeight = max(self.height, Word.maxCharHeight)