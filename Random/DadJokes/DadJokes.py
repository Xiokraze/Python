import pyfiglet
import termcolor
import os
import requests
import random


class Screen:
    clear = lambda: os.system('cls')

def printHeader():
    color = "green"
    header = "Dad Jokes!"
    headerArt = pyfiglet.figlet_format(header)
    coloredArt = termcolor.colored(headerArt, color)
    print(coloredArt)
    return


def getTopic():
    while(True):
        topic = input("Enter a topic: ")
        if (len(topic) > 0):
            break
    print()
    return topic


def getResponse(url):
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
    )
    return response


def getJoke(topic):
    searchTerm = "?term=" + topic
    url = "https://icanhazdadjoke.com/search" + searchTerm
    response = getResponse(url)
    data = response.json()
    return data["results"]


def printJoke(jokeRequest, topic):
    numJokes = len(jokeRequest)
    if (not numJokes):
        print(f"I'm sorry, I don't have a joke about {topic}!\n")
    else:
        if (numJokes == 1):
            print(f"I've got {numJokes} joke about {topic}, here's one!")
        else:
            print(f"I've got {numJokes} jokes about {topic}, here's one!")
        randomJoke = random.randint(1, len(jokeRequest))
        print(jokeRequest[randomJoke - 1]['joke'] + "\n")
    return


def anotherJoke():
    while(True):
        choice = input("Enter N to quit, anything else for another joke! ")
        if (len(choice) > 0):
            break
    if (choice[0].upper() == 'N'):
        return False
    return True
                

def main():
    os.system('color')
    while(True):
        Screen.clear()
        printHeader()
        topic = getTopic()
        jokeRequest = getJoke(topic)
        printJoke(jokeRequest, topic)
        if (not anotherJoke()):
            break


if __name__ == "__main__":
    main()
