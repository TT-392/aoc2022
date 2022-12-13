import numpy as np
from colorama import Fore, Back, Style
import re

class Monkey:
    def __init__(self, start_items, operation, divisible, truemonkey, falsemonkey):
        self.items = start_items
        self.operation = operation
        self.divisible = divisible
        self.truemonkey = truemonkey
        self.falsemonkey = falsemonkey
        self.total_inspections = 0

    def inspect(self):
        items = []

        for item in self.items:
            old = item
            item = eval(self.operation)
            item = item // 3
            items.append(item)

            self.total_inspections += 1

        self.items = items

    def __str__(self):
        return str(self.items)


f = open("input", "r")
monkeys = []

while 1:
    monkeyNr = int(re.findall("[0-9][0-9]*", f.readline())[0])
    start_items = [int(x) for x in re.findall("[0-9][0-9]*", f.readline())]
    operation = re.findall("new = .*$", f.readline())[0][6:]
    divisible = int(re.findall("[0-9][0-9]*", f.readline())[0])
    truemonkey = int(re.findall("[0-9][0-9]*", f.readline())[0])
    falsemonkey = int(re.findall("[0-9][0-9]*", f.readline())[0])

    monkeys.append(Monkey(start_items, operation, divisible, truemonkey, falsemonkey))

    if f.readline() == "":
        break

for Round in range(0, 20):

    for monkey in monkeys:
        monkey.inspect()

        for i in range(0, len(monkey.items)):
            item = monkey.items[i]

            if item % monkey.divisible == 0:
                monkeys[monkey.truemonkey].items.append(item)
            else:
                monkeys[monkey.falsemonkey].items.append(item)

        monkey.items = []

    print("Round:", Round + 1)
    for monkey in monkeys:
        print(monkey.items)


    print()


totals = []
for monkey in monkeys:
    print(monkey.total_inspections)
    totals.append(monkey.total_inspections)

totals.sort(reverse=True)

print(totals[0], "*", totals[1], "=", totals[0] * totals[1])

    
