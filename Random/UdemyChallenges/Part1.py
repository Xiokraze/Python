# Part 1 Challenges: https://www.udemy.com/the-modern-python3-bootcamp/learn/lecture/11339746#bookmarks

# Reverses a string
def reverseString(word):
    reverseWord = word[::-1]
    print(f"Before: {word}\nAfter: {reverseWord}")
    return

# Prints true/false if each value in the list is a list
def listCheck(data):
    value = True
    for d in data:
        if (type(d) is not list):
            value = False
    if(value): 
        print("True")
    else: 
        print("False")
    return

# Removes every other element from a list
def removeEveryOther(data):
    newData = data[::2]
    print(f"Before: {data}\nAfter: {newData}")
    return

# Finds first 2 numbers in list that sum to the given number
def sumListPairs(data, total):
    found = False
    for i in data:
        if (found):
            break
        num1 = i
        for num2 in data:
            if (num1 + num2 == total):
                found = True
                break
    if not found:
        print([])
    else:
        print([num1, num2])
    return

# Prints dictionary of vowel counts in a word
def vowelCount(word):
    word = word.lower()
    dictionary = {letter: word.count(letter) for letter in word if letter in "aeiou"}
    print(dictionary)