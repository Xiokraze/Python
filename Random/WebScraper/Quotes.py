import requests
from bs4 import BeautifulSoup
from os import system
from random import randint

class Screen:
    clear = lambda: system('cls')

class Quote:
    quoteCount = 0
    def __init__(self, quote, author, link):
        self.quote = quote
        self.author = author
        self.link = link
        Quote.quoteCount += 1

def findData(url, findThis):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all(class_ = findThis)
    except ValueError as error:
        print(error)
    return False

def getQuotes():
    websiteURL = "http://quotes.toscrape.com"
    pageNumber = ""
    quoteList = []
    pageCounter = 1
    working = "Gathering jokes"
    while(True):
        print(working)
        quotes = findData(websiteURL + pageNumber, "quote")
        if (quotes):
            for quote in quotes:
                quoteText = quote.find(class_="text").text
                author = quote.find(class_="author").text
                aTag = quote.find("a")
                bioLink = websiteURL + aTag["href"]
                quoteList.append(Quote(quoteText, author, bioLink))
        try:
            nextPage = findData(websiteURL + pageNumber, "next")
            nextText = nextPage[0].find("a")
            pageNumber = nextText["href"]
        except IndexError:
            break
        if (pageCounter == 4):
            working = "Gathering jokes"
            pageCounter = 1
        else:
            working = working + "."
            pageCounter += 1
        Screen.clear()
    Screen.clear()
    return quoteList

def getAQuote(quotes):
    numQuotes = Quote.quoteCount
    index = randint(0, numQuotes - 1)
    return quotes[index]

def anotherQuote():
    choice = input("Try another quote(y/n)? ")
    if (choice == 'n'): return False
    return True