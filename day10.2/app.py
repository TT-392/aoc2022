import numpy as np
from colorama import Fore, Back, Style
import re

total = 0
checks = [20, 60, 100, 140, 180, 220]
display = [["."]*40 for i in range(6)]

def print_display(display):
    for row in display:
        for c in row:
            print(c, end="")
        print()

def process_cycle(cycle, x):
    if cycle == 40*6:
        return
    global total

    #if cycle in checks:
    #    total += cycle * x
    #    print(cycle * x)
    X = cycle % 40
    Y = cycle // 40
    print("x:", X, "y:", Y)
    sprite = render_sprite(x)
    print(sprite)
    display[Y][X] = sprite[X]
    print_display(display)
    print("cycle:", cycle, "x:", x)

f = open("input")

def render_sprite(x):
    line = ["."]*40
    if x < 40 and x >= 0:
        line[x] = "#"
    if x+1 < 40 and x+1 >= 0:
        line[x+1] = "#"
    if x-1 < 40 and x-1 >= 0:
        line[x-1] = "#"
    return "".join(line)

x = 1
cycle = 0
process_cycle(cycle, x)
cycle += 1

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

print_display(display)
