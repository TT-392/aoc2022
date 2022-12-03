import numpy as np

def calcScore(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return 1 + ord(c) - ord('a')

    elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return 27 + ord(c) - ord('A')
    

f = open("input", "r");

total = 0

while True:
    lines = []
    for i in range(0, 3):
        lines.append(f.readline())

    if lines[0] == '':
        break

    for c in lines[0]:
        if c in lines[1] and c in lines[2]:
            print(c)
            total += calcScore(c)
            break;

print(total)




