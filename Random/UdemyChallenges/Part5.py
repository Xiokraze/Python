



def letterCounter(word):
    letterCounter.val = word
    def inner(char):
        lowerWord = letterCounter.val.lower()
        return len(list(c for c in lowerWord if c == char))
    return inner


def once(fn):
    fn.is_called = False
    def inner(*args):
        if not(fn.is_called):
            fn.is_called = True
            return fn(*args)
    return inner

def nextPrime():
    num = 2
    allPrimes = set()
    while True:
        for prime in allPrimes:
            if num % prime == 0:
                break
        else:
            allPrimes.add(num)
            yield num
        num += num % 2 + 1