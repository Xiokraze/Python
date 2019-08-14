import pygame
from PIL import ImageFont

#Screen
screenW = 950
screenH = 600
center = screenW // 2
bottomBoxH = 35
borderW = 2
buttonW = 150
buttonH = 75
screenGameH = screenH - bottomBoxH
windowBGColor = (0,0,0)
windowBGImg = pygame.image.load('underwater.jpg')           # Load background
maxFPS = 40
maxFallSpeed = 2
clock = pygame.time.Clock()

#Fonts
masterFont = "ariblk.ttf"
fontSize = 20
wordFont = pygame.font.Font(masterFont, fontSize)
font = ImageFont.truetype(masterFont, fontSize)
textColor = (255,255,255)
btnTextColor = (255,255,255)
btnColor = (44, 150, 199)
btnHoverColor = (194,178,128)

#Input Box
inputPrompt = "Input: "
scorePrompt = "Score: "
gwpmPrompt = "gwpm: "
inputLeftPadding = 20

class Time:
    frameTracker = 0
    seconds = 0
    started = True
    running = True
    delaySeconds = 1                                                    # changes seconds interval for printing words
    def updateSeconds():
        Time.frameTracker += 1
        if (Time.frameTracker == maxFPS * Time.delaySeconds):
            Time.frameTracker = 0
            Time.seconds += 1
            return True
        return False

def getScreen():
    pygame.display.set_caption("TypingGame")
    return (pygame.display.set_mode((screenW, screenH)))

def drawWords(screen, words):
    for word in words:
        try:
            wordText = wordFont.render(word.value, 1, word.textColor)
            screen.blit(wordText, (word.x, word.y))
        except:
            break
    return

def drawWordsPerMin(screen, chars, playerScore):
    gwpm = 0
    if (chars != 0 and Time.seconds != 0):
        gwpm = (chars/5) / (Time.seconds/60)
    gwpm = round(gwpm)
    fontSizePixels = font.getsize(gwpmPrompt + str(gwpm))
    positionX =  center - (fontSizePixels[0] / 2)
    text = wordFont.render(gwpmPrompt + str(gwpm), 1, textColor)
    screen.blit(text, (positionX, getBottomOffset(playerScore)))
    return

def drawButtons(screen, buttons):
    for button in buttons:
        button.draw(screen)


def drawBottomBox(screen):
    height = screenH - bottomBoxH
    leftBorder = 0
    topBorder = height - borderW
    rightBorder = screenW - borderW + 1
    bottomBorder = bottomBoxH
    bottomBox = (leftBorder, topBorder, rightBorder, bottomBorder)
    pygame.draw.rect(screen, textColor, bottomBox, borderW)

def getBottomOffset(playerScore=""):
    fontSizePixels = font.getsize(scorePrompt + str(playerScore) + str(borderW))
    fontHeight = fontSizePixels[1]
    return screenH - fontHeight - borderW * 3 - ((bottomBoxH - fontHeight) // 2)

def getRightOffset(playerScore):
    fontSizePixels = font.getsize(scorePrompt + str(playerScore) + str(borderW))
    return screenW - buttonW - fontSizePixels[0]

def getInputOffset():
    fontSizePixels = font.getsize(inputPrompt)
    return inputLeftPadding + fontSizePixels[0]

def drawInputText(screen, playerScore):
    text = wordFont.render(inputPrompt, 1, textColor)
    screen.blit(text, (inputLeftPadding, getBottomOffset(playerScore)))
    return

def drawScoreText(screen, playerScore):
    text = wordFont.render(scorePrompt + str(playerScore), 1, textColor)
    screen.blit(text, (getRightOffset(playerScore) + buttonW, getBottomOffset(playerScore)))
    return

def drawScreen(screen, words, chars, inputTextBox, playerScore, buttons):
    clock.tick(maxFPS)
    #screen.fill(windowBGColor)
    screen.blit(windowBGImg, (0,0))
    drawWords(screen, words)
    drawButtons(screen, buttons)
    drawBottomBox(screen)
    drawInputText(screen, playerScore)
    drawScoreText(screen, playerScore)
    drawWordsPerMin(screen, chars, playerScore)
    screen.blit(inputTextBox, (getInputOffset(), getBottomOffset(playerScore)))
    pygame.display.update()
    return