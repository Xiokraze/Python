
def twoListDictionary(keys, values):
    dictionary = {}
    index = 0
    for key in keys:
        if (index < len(values)):
            dictionary[key] = values[index]
        else:
            dictionary[key]= None
        index += 1
    print(dictionary)
    return

def rangeInList(list1, start=0, end=None):
    end = end or list1[-1]
    total = sum(list1[start:end + 1])
    print(total)
    return

def sameFrequency(num1, num2):
    dict1 = {letter:str(num1).count(letter) for letter in str(num1)}
    dict2 = {letter:str(num2).count(letter) for letter in str(num2)}

    for key,value in dict1.items():
        if not (key in dict2.keys()):
            return False
        elif dict1[key] != dict2[key]:
            return False
    return True

def nth(list1, num):
    if (num > len(list1)):
        print("Num is greater than the number of elements in the list!")
    else:
        print(list1[num])
    return

def findDuplicate(list1):
    counter = {}
    for num in list1:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)
    return None



