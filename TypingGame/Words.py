from Screen import screenW, screenGameH, maxFallSpeed, textColor
from random import randint

wordbank = ["at", "lol", "Link", "Zelda", "Bowser", "Charizard"]

class Word(object):
    def __init__(self, value):
        self.value = value
        xOffset = screenW - 50
        self.x = randint(0, xOffset)
        self.y = 0
        self.fallSpeed = self.getFallSpeed(len(value))
        self.textColor = textColor

    def getFallSpeed(self, wordLength):
        if (wordLength == 2):
            return maxFallSpeed
        if (wordLength == 3):
            return maxFallSpeed - 1
        if (wordLength == 4 or wordLength == 5):
            return maxFallSpeed - 2
        if (wordLength == 6 or wordLength == 7):
            return maxFallSpeed - 3
        else:
            return maxFallSpeed - 4

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
            if (fall < screenGameH):
                word.y += word.fallSpeed
            else:
                words.remove(word)
    return

def removeWords(words, playerInput):
    for word in words:
        if (playerInput == word.value):
            words.remove(word)
    return words