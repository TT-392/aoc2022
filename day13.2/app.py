import numpy as np
import time
from colorama import Fore, Back, Style
import re

inp = []

f = open("input", "r")

while 1:
    inp.append(eval(f.readline()))
    inp.append(eval(f.readline()))

    if f.readline() == '':
        break

def compare(left, right):
    print("comparing", left, right)
    if type(left) == int and type(right) == int:
        print("ints")
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    else:
        if type(left) == int:
            left = [left]
        elif type(right) == int:
            right = [right]


        i = 0
        while 1:
            if len(left) == i and len(right) == i:
                return None
            elif len(left) == i:
                return True
            elif len(right) == i:
                return False
            else:
                retval = compare(left[i], right[i])
                if retval == True or retval == False:
                    return(retval)
            i += 1




i = 0
ordered = []

dividers = [[[2]], [[6]]]
inp += dividers

for packet in inp:

    for i in range(len(ordered) + 1):
        if i == len(ordered):
            ordered.append(packet)
        if compare(packet, ordered[i]):
            ordered = ordered[:i] + [packet] + ordered[i:]
            break


print()
for i in ordered:
    print(i)

print()
total = 1
for divider in dividers:
    print(ordered.index(divider) + 1)
    total *= ordered.index(divider) + 1
print()
print(total)



