import os

class Screen:
    clear = lambda: os.system('cls')

def getIntegerInput(min, max, text):
    while(1):      
        for i in range(len(text)):
            print(text[i])
        try:
            menuOption = int(input(" Menu Option: "))
        except ValueError:
            Screen.clear()
        else:
            if (menuOption >= min and menuOption <= max):
                break
            Screen.clear()
    Screen.clear()
    return menuOption