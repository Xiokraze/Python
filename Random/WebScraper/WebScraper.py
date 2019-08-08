# http://quotes.toscrape.com                                            
from os import system
import Quotes
import Author

class Screen:
    clear = lambda: system('cls')

def printIntro(quote):
    print("Who said...\n")
    print(f"{quote}\n")
    return

def printClue1(bday, location):
    if (bday and location):
        print(f"Clue 1: The author was born {bday} {location}\n")
    return

def printClue2(author):
    initials = Author.getAuthorInitials(author)
    print(f"Clue 2: The author's initials are {initials}\n")
    return

def printClue3(author):
    clue = Author.printNameClue(author)
    print(f"Clue 3: {clue}\n")
    return

def main():
    quoteList = Quotes.getQuotes()
    guessNum = 1
    maxGuesses = 4
    getMoreQuotes = True
    while(getMoreQuotes):
        quote = Quotes.getAQuote(quoteList)
        authorBday, authorLocation = Author.getAuthorBio(quote.link)
        while(True):
            printIntro(quote.quote)
            if (guessNum >= 2):
                printClue1(authorBday, authorLocation)
            if (guessNum >= 3):
                printClue2(quote.author)
            if (guessNum == 4):
                printClue3(quote.author)
            guess = input(f"Guess {guessNum} of {maxGuesses}: ")
            print
            if (guess == quote.author):
                print(f"That's correct! {quote.author} said that!\n")
                guessNum = 1
                break
            if (guessNum == maxGuesses):
                print(f"Game Over! The author was {quote.author}\n")
                guessNum = 1
                break
            guessNum += 1
            Screen.clear()
        if not (Quotes.anotherQuote()):
            getMoreQuotes = False
        Screen.clear()

if __name__ == "__main__":
    main()
