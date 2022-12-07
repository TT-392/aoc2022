import numpy as np
import re


f = open("input", "r");

stacks = [[] for i in range(9)]

while 1:
    line = f.readline()
    if len(re.findall("[0-9]", line)) > 0:
        break

    for i in list(range(1, len(line), 4)):
        if line[i] != " ":
            stacks[(i-1)//4].append(line[i])

f.readline()
print(stacks)
print()

for line in f.readlines():
    retval = re.findall("[0-9][0-9]*", line)
    amount, From, to = [int(retval[i]) for i in range(3)]
    print(amount, From, to)

    crane = stacks[From - 1][:amount]
    stacks[From - 1] = stacks[From - 1][amount:]

    stacks[to - 1] = crane[::-1] + stacks[to - 1]

    print(stacks)

print()
print(''.join([stack[:1][0] for stack in stacks]))




