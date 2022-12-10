import numpy as np
from colorama import Fore, Back, Style
import re

total = 0
checks = [20, 60, 100, 140, 180, 220]

def process_cycle(cycle, x):
    global total

    if cycle in checks:
        total += cycle * x
        print(cycle * x)
    #print("cycle:", cycle, "x:", x)

f = open("input")

x = 1
cycle = 0
cycle += 1
process_cycle(cycle, x)
cycle += 1
process_cycle(cycle, x)

while 1:
    line = f.readline()
    if line == "":
        break
    elif line[:-1] == "noop":
        pass
    else:
        process_cycle(cycle, x)
        cycle += 1
        x += int(line[5:-1])

    process_cycle(cycle, x)
    cycle += 1

print(total)
