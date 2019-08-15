import PlayerInput as P # need to move classes to here
import Screen as S
import random

class Bubble:
    bubbles = []
    def __init__(self):
        self.img = S.bubble
        size = self.img.get_size()
        self.width = size[0]
        self.height = size[1]
        self.x = random.randint(0, S.screenW - self.width)
        self.startX = self.x
        self.y = S.screenH + self.height
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
            if (self.y <= 0 - S.fontSize - S.borderW):
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
            S.menuButtonW, 
            S.menuButtonH, 
            True)
        )
        return

class TextBlink:
    textOn = True
