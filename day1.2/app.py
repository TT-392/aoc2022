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
elves_total = []
for elf in elves:
    total = sum(elf)
    elves_total.append(total)
    if total > MAX:
        MAX = total

print(sum(sorted(elves_total)[-3:]))

