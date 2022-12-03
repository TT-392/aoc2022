import numpy as np

def calcScore(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return 1 + ord(c) - ord('a')

    elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return 27 + ord(c) - ord('A')
    

f = open("input", "r");

total = 0

for line in f.readlines():
    length = len(line) - 1

    comp1 = line[length//2:-1]
    comp2 = line[:length//2]

    for c in comp1:
        if c in comp2:
            print(c)
            total += calcScore(c)
            break

print(total)



