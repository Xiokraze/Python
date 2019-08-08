import Part1
import Part2
import Part3
import Part4
import Part5

def part1Challenges():
    Part1.reverseString("hello world")
    Part1.listCheck([[],[1],[2,3]])
    Part1.listCheck("hi")
    Part1.removeEveryOther([1,2,3,4,5])
    Part1.sumListPairs([4,2,10,5,1], 6)
    Part1.vowelCount("Joshua Worthington")
    return

def part2Challenges():
    Part2.capitalizeFirst("Joshua wOrThInGtOn")
    Part2.findFactors(111)
    print(Part2.includes([1, 2, 3], 1))
    print(Part2.includes({ 'a': 1, 'b': 2 }, 1))
    print(Part2.includes({ 'a': 1, 'b': 2 }, 'a'))
    Part2.repeat('*', 3)
    Part2.repeat('abc', 2)
    Part2.truncate("Joshua Worthington", 2)
    Part2.truncate("Joshua Worthington", 6)
    return

def part3Challenges():
    Part3.twoListDictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
    Part3.rangeInList([1,2,3,4],0,2)
    Part3.sameFrequency(551122,221515)
    Part3.sameFrequency(321142,3212215)
    print(Part3.nth(['a', 'b', 'c', 'd'], 1))
    print(Part3.nth(['a', 'b', 'c', 'd'], -4))
    print(Part3.findDuplicate([1,2,1,4,3,12]))
    print(Part3.findDuplicate([2,1,3,4]))
    return

def part4Challenges():
    print(Part4.sumDiagonals([[1,2], [3,4]]))
    print(Part4.sumDiagonals([[1,2,3], [4,5,6], [7,8,9]]))
    print(Part4.dictionaryMinMax({2:'a', 7:'b', 1:'c',10:'d',4:'e'}))
    print(Part4.dictionaryMinMax({1: "Elie", 4:"Matt", 2: "Tim"}))
    print(Part4.findGreaterNumbers([1,2,3]))
    print(Part4.findGreaterNumbers([5,4,3,2,1]))
    print(Part4.twoOldest([1, 2, 10, 8]))
    print(Part4.twoOldest([4,25,3,20,19,5]))
    print(Part4.isOddString("veryfun"))
    print(Part4.isOddString("a"))
    print(Part4.validParentheses("(())((()())())"))
    print(Part4.validParentheses("))(("))
    print(Part4.reverseVowels("Reverse Vowels In A String"))
    print(Part4.threeOddNumbers([1,2,3,4,5]))
    print(Part4.threeOddNumbers([1,2,3,3,2]))
    print(Part4.mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))
    print(Part4.runningAverage())
    return

def part5Challenges():
    #counter = Part5.letterCounter("Amazing")
    #print(counter('a'))
    #oneAddition = Part5.once(add)
    #print(oneAddition(2,2))
    #print(oneAddition(2,2))
    primes = Part5.nextPrime()
    print([next(primes) for i in range(25)])
    return

def main():
    #part1Challenges()
    #part2Challenges()
    #part3Challenges()
    #part4Challenges()
    part5Challenges()


if __name__ == "__main__":
    main()
