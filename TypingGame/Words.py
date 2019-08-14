import Screen as S
from random import randint, choice
from PIL import ImageFont

class Player:
    score = 0

class Word(object):
    falling = False
    maxCharHeight = 0
    charsTyped = 0
    def __init__(self, value):
        self.value = value
        self.textColor = S.textColor
        self.fallSpeed = getFallSpeed(len(value))

        # Calculate px value for word width and height
        fontSizePixels = S.font.getsize(self.value)
        self.width = fontSizePixels[0]
        self.height = fontSizePixels[1]

        # Get px offset from right border to keep the word on the screen
        xOffset = S.screenW - self.width - S.borderW * 4 - S.buttonW
        self.x = randint(0, xOffset)
        self.y = 0

        Word.maxCharHeight = max(self.height, Word.maxCharHeight)

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
    playerInput = playerInput.split(' ')
    for word in words:
        for pword in playerInput:
            if (pword == word.value):
                words.remove(word)
                Player.score += len(word.value)
                Word.charsTyped += len(word.value) + 1
                break
    return words

def checkCount(words, wordbank):
    if (len(words) < 1):
        words.append(choice(wordbank))
    return words

def wordObjects(words, playerInput):
    newWords = []
    for word in words:
        if (type(word) is str):
            newWords.append(Word(word))
        else:
            newWords.append(word)
    return removeWords(newWords, playerInput)
    
def fallingWords(words):
    for word in words:
        try:
            fall = word.y + word.fallSpeed
            if (fall < S.screenGameH - word.height):
                word.y += word.fallSpeed
            else:
                Player.score -= len(word.value)
                words.remove(word)
        except AttributeError:
            break
    return