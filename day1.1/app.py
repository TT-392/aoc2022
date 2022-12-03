import numpy as np

f = open("input", "r");

elves = []
elf = []

for line in f.readlines():
    if not line == "\n":
        elf.append(int(line))
    else:
        elves.append(elf)
        elf = []


MAX = 0
for elf in elves:
    total = sum(elf)
    if total > MAX:
        MAX = total
print(MAX)

