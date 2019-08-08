
def example1():
    list1 = ["Video Games", "Puzzles", "Programming"]
    list2 = ["Indiana", "Florida", "Colorado"]
    answer = {list1[i]: list2[i] for i in range(3)}
    print("Example 1")
    print(answer)
    print()
    return

def example2():
    person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
    answer = {x:y for x,y in person}
    print("Example 2")
    print(answer)
    print()
    return

def example3():
    answer = {char:0 for char in 'aeiou'}
    print("Example 3")
    print(answer)
    print()
    return

def example4():
    answer = {char:chr(char) for char in range(65,91)}
    print("Example 4")
    print(answer)
    print()
    return

def return_day(day):
    week = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
    if day in week: return week[day]
    else: return None

def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}

def main():
    #example1()
    #example2()
    #example3()
    #example4()
    #print(return_day(41))
    #print(return_day(3))
    #print(multiple_letter_count("Joshua James Worthington"))

if __name__ == "__main__":
        main()