


def capitalizeFirst(words):
    print(' '.join(char[0].upper() + char[1:] for char in words.split(' ')))
    return

def findFactors(num):
    factors = []
    for i in range(1, num):
        if (num % i == 0):
            factors.append(i)
    factors.append(num)
    print(factors)
    return

def includes(collection, value, index=None):
    if (type(collection) == dict):
        return value in collection.values()
    if (index == None):
        return value in collection
    return value in collection[index:]

def repeat(value, num):
    newValue = ""
    for i in range(num):
        newValue = newValue + value
    print(newValue)
    return

def truncate(data, num):
    if (num < 3):
        return "Truncation must be at least 3 characters."
    elif (len(data) < 3):
        return data
    elif(num > len(data)):
        return data
    else:
        return data[:num-3:] + "..."
