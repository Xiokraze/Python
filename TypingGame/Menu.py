from WordBanks import allWords
from os import system
class Screen:
    clear = lambda: system('cls')

def printMenu():
    wordsByGrade = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
    wordsByLength = ("3", "4", "5", "6", "7", "8", "9+")
    num = 1
    print("Wordbank Menu")
    for word in wordsByGrade:
        print(f" {num}) {word} Grade Vocabulary")
        num += 1
    for word in wordsByLength:
        print(f" {num}) {word} Letter Words")
        num += 1
    return num

def getInput():
    while (True):
        try:
            numChoices = printMenu()
            userInput = int(input("Enter Menu Number: "))
            if (userInput > 0 and userInput <= numChoices):
                break
        except ValueError:
            Screen.clear()
    Screen.clear()
    return userInput

def menu():

    playerInput = getInput()
    wordbank = allWords[playerInput - 1]

    return wordbank
