import numpy as np
import re


f = open("input", "r");


line = f.readline()

for i in range(0, len(line) - 4):
    chars = line[i:i+14]

    if len(set(chars)) == 14:
        print(chars)
        print(i+14)
        break



