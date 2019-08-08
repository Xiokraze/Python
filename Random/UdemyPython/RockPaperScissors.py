import os
from random import choice

class Screen:
    clear = lambda: os.system("cls")

def playerVsPlayer():
    while(1):
        try:
            print("1) Player VS Player")
            print("2) Player VS CPU")
            opponent = int(input("1 or 2: "))
            if (opponent == 1 or opponent == 2):
                break
            else:
                Screen.clear()
        except ValueError:
            Screen.clear()
    Screen.clear()
    if (opponent == 1): 
        return True
    else: 
        return False

def printIntro():
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    return

def getChoice(playerNum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    if (playerNum == 2): 
        player = "Player 2"
    else: 
        player = "Player 1"
    while(1):
        try:
            printIntro()
            choice = input(player + " Input: ")
            print(choice)
            if (choice == rock or choice == paper or choice == scissors):
                break
            else:
                Screen.clear()
        except ValueError:
            Screen.clear()
    Screen.clear()
    return choice

def getWinner(p1, p2):
    player1 = "Player 1"
    player2 = "Player 2"
    draw = "Draw"
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    if (p1 == p2):
        return draw
    elif (p1 == rock and p2 == paper):
        return player2
    elif (p1 == rock and p2 == scissors):
        return player1
    elif (p1 == paper and p2 == rock):
        return player1
    elif (p1 == paper and p2 == scissors):
        return player2
    elif (p1 == scissors and p2 == rock):
        return player2
    elif (p1 == scissors and p2 == paper):
        return player1
    else:
        return ""

def printGameStatus(winner, p1, p2):
    print("SHOOT!")
    print("Player 1: " + p1)
    print("Player 2: " + p2)
    print("Winner: " + winner)
    return

def playAgain():
    play = input("Play Again? Y/N: ")
    if (play == 'n' or play  == 'N'):
        return False
    else:
        return True

def main():
    pvp = playerVsPlayer()
    while(1):
        player1Choice = getChoice(1)
        if (pvp): 
            player2Choice = getChoice(2)
        else: 
            player2Choice = choice(['rock', 'paper', 'scissors'])
        winner = getWinner(player1Choice, player2Choice)
        printGameStatus(winner, player1Choice, player2Choice)
        if (playAgain() == False):
            break
        Screen.clear()

if __name__ == "__main__":
    main()