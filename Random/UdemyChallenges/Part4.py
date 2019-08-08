

def sumDiagonals(list1):
    total = 0
    index = 0
    for row in list1:
        total += list1[index][index]
        total += list1[index][-1-index]
        index += 1
    return total

def dictionaryMinMax(dictionary):
    keys = dictionary.keys()
    return [min(keys), max(keys)]

def findGreaterNumbers(list1):
    count = 0
    for i in range(len(list1)):
        remaining = list1[i:]
        for num in remaining:
            if (list1[i] < num):
                count += 1
    return count

def twoOldest(ages):
    #max1 = max(ages)
    #ages.remove(max1)
    #max2 = max(ages)
    #if (max1 > max2):
    #    return [max2, max1]
    #return [max1, max2]
    return sorted(ages)[-2:]

def isOddString(word):
    total = 0
    for char in word:
        total += ord(char) - 96     # Start at index 1, not 0
    if (total % 2 == 0):
        return False
    return True

def validParentheses(parentheses):
    count = 0
    for p in parentheses:
        if (p == '('):
            count += 1
        if (p == ')'):
            count -= 1
        if (count < 0):
            return False
    if (count != 0):
        return False
    return True

def reverseVowels(words):
    newWords = ""
    vowelsIndex = []
    for i in range(len(words)):
        if (words[i] in "aeiouAEIOU"):
            vowelsIndex.append(i)
    endIndex = -1
    for i in range(len(words)):
        if (i in vowelsIndex):
            newWords = newWords + words[vowelsIndex[endIndex]]
            endIndex -= 1
        else:
            newWords = newWords + words[i]
    return newWords

def threeOddNumbers(numList):
    for i in range(len(numList)):
        if (i + 2 >= len(numList)):
            return False
        else:
            total = numList[i] + numList[i+1] + numList[i+2]
            if (total % 2 != 0):
                return True
    return False

def mode(numList):
    numList.sort()
    dict1 = {num:numList.count(num) for num in numList}
    return max(dict1, key=dict1.get)

def runningAverage():
    runningAverage.accumulator = 0
    runningAverage.size = 0 
    def inner(number):
        runningAverage.accumulator += number
        runningAverage.size += 1
        return runningAverage.accumulator / runningAverage.size   
    return inner