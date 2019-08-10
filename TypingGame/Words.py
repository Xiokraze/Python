import Screen
from random import randint
import WordBanks
from PIL import ImageFont

class Player:
    score = 0

class Word(object):
    maxCharHeight = 0
    def __init__(self, value):
        self.value = value
        self.textColor = Screen.textColor
        self.fallSpeed = self.getFallSpeed(len(value))
        self.width, self.height = self.getWidthHeight()
        xOffset = Screen.screenW - self.width - Screen.borderWidth
        self.x = randint(0, xOffset)
        self.y = 0
        Word.maxCharHeight = max(self.height, Word.maxCharHeight)

    def getFallSpeed(self, wordLength):
        if (wordLength == 2):
            return Screen.maxFallSpeed
        if (wordLength == 3):
            return Screen.maxFallSpeed - 1
        if (wordLength == 4 or wordLength == 5):
            return Screen.maxFallSpeed - 2
        if (wordLength == 6 or wordLength == 7):
            return Screen.maxFallSpeed - 3
        else:
            return Screen.maxFallSpeed - 4

    def getWidthHeight(self):
        font = ImageFont.truetype(Screen.masterFont, Screen.fontSize)
        fontSizePixels = font.getsize(self.value)
        return fontSizePixels[0], fontSizePixels[1]

def getWordBank():
    return WordBanks.kindergarten
    #TODO add functionality for different word banks

def wordObjects(words):
    newWords = []
    for word in words:
        if (type(word) is str):
            newWords.append(Word(word))
        else:
            newWords.append(word)
    return newWords

def fallingWords(words):
    if (len(words) > 0):
        for word in words:
            fall = word.y + word.fallSpeed
            if (fall < Screen.screenGameH - word.height):
                word.y += word.fallSpeed
            else:
                Player.score -= len(word.value)
                words.remove(word)
    return

def removeWords(words, playerInput):
    for word in words:
        if (playerInput == word.value):
            words.remove(word)
            Player.score += len(word.value)
            break
    return words