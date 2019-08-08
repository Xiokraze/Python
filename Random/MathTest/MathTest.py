import random
from os import system

class Screen:
    clear = lambda: system('cls')

def getUserInput(prompt):
    while(True):
        try:
            userInput = int(input(prompt))
            break
        except ValueError:
            Screen.clear()
    return userInput

def getAnswer(num1, symbol, num2):
    if (symbol == '+'): return num1 + num2
    if (symbol == '-'): return num1 - num2
    else: return num1 * num2

def askQuestion(maxNum):
    num1 = random.randint(1,maxNum)
    num2 = random.randint(1,maxNum)
    symbol = random.choice(['+', '-', '*'])
    print(f"{num1} {symbol} {num2}")
    userAnswer = getUserInput("Answer: ")
    answer = getAnswer(num1, symbol, num2)
    if (userAnswer == answer):
        return True
    return False

def testAgain(prompt):
    userInput = input(prompt)
    if (userInput[0].lower() == 'n'):
        return False
    return True

def main():
    prompt1 = "How many questions would you like to be asked? "
    prompt2 = "What is the maximum number to be included in questions? "
    prompt3 = "Would you like to take another test? y/n "

    while(True):
        amount = getUserInput(prompt1)
        maxNum = getUserInput(prompt2)
        Screen.clear()
        correct = 0
        for i in range(amount):
            if (askQuestion(maxNum)):
                correct += 1
            Screen.clear()
        print(f"Score: {correct} out of {amount}.")
        if not (testAgain(prompt3)):
            break
        Screen.clear()

if (__name__ == "__main__"):
    main()