from collections import Counter

def validate1(pas):
    return len(set(pas.split())) == len(pas.split())

assert validate1("aa bb cc dd ee") == True
assert validate1("aa bb cc dd aa") == False
assert validate1("aa bb cc dd aaa") == True

def validate2(pas):
    counters = []
    for word in pas.split():
        new_c = Counter(word)
        for c in counters:
            if c == new_c:
                return False
        else:
            counters.append(new_c)
    return True

assert validate2("abcde fghij") == True
assert validate2("abcde xyz ecdab") == False
assert validate2("a ab abc abd abf abj") == True
assert validate2("iiii oiii ooii oooi oooo") == True
assert validate2("oiii ioii iioi iiio") == False

with open('input.txt', 'r') as file:
    print(sum(map(validate1, file.read().splitlines())))

with open('input.txt', 'r') as file:
    print(sum(map(validate2, file.read().splitlines())))

