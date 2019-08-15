import Screen as S
import Classes as C
from random import randint, choice
from PIL import ImageFont


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
                    C.Player.score += len(word.value)
                    C.Word.charsTyped += len(word.value) + 1
                    break
    return words

def checkCount(words, wordbank, numWords):
    if (len(words) < numWords):
        for i in range(numWords):
            words.append(choice(wordbank))
    return words

def wordObjects(words, playerInput):
    newWords = []
    for word in words:
        if (type(word) is str):
            newWords.append(C.Word(word))
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
                C.Player.score -= len(word.value)
                words.remove(word)
        except AttributeError:
            break
    return