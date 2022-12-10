import numpy as np
from colorama import Fore, Back, Style
import re

f = open("input")

head = [0, 0]
tail = [0, 0]
path = set()

for line in f.readlines():
    amount = int(line[2:])

    if line[0] == 'U':
        vector = (0, 1)
    elif line[0] == 'D':
        vector = (0, -1)
    elif line[0] == 'R':
        vector = (1, 0)
    elif line[0] == 'L':
        vector = (-1, 0)

    for i in range(0, amount):
        head[0] += vector[0]
        head[1] += vector[1]

        if tail[0] < head[0] - 1:
            tail = [head[0] - 1, head[1]]
        if tail[0] > head[0] + 1:
            tail = [head[0] + 1, head[1]]
        if tail[1] < head[1] - 1:
            tail = [head[0], head[1] - 1]
        if tail[1] > head[1] + 1:
            tail = [head[0], head[1] + 1]


        print(tail)
        path.add(tuple(tail))

print()

print(head)
print(path)
print(len(path))
        







