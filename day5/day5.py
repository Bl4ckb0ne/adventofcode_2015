import re

def vowels(s):
    return (s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')) >= 3

def double(s):
    for i in range(0, len(s)):
        if i < len(s) - 1:
            if s[i] == s[i + 1]:
                return True
    return False

def bad_double(s):
    return ('ab' in s) or ('cd' in s) or ('pq' in s) or ('xy' in s)

def pair(s):
    return re.search(r'(.)(.).*\1\2', s)

def repeat(s):
    return re.search(r'(.).\1', s)

with open("input") as file:
    lines = file.readlines()
    nice = 0
    nicer = 0
    for line in lines:
        if(line == '\n'):
            break

        line = line[:-1]

        if(vowels(line) and double(line) and not bad_double(line)):
            nice += 1

        if(pair(line) and repeat(line)):
            nicer += 1

    print(nice)
    print(nicer)

