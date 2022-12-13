import numpy as np
import time
from colorama import Fore, Back, Style
import re

inp = []

f = open("input", "r")

while 1:
    pair =  []
    pair.append(eval(f.readline()))
    pair.append(eval(f.readline()))
    inp.append(pair)

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
total = 0
for pair in inp:
    i += 1

    print(pair[0], "vs", pair[1])
    result = compare(pair[0], pair[1])
    print(result)
    if result:
        total += i

    print()

print(total)


