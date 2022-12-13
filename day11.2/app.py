import numpy as np
from colorama import Fore, Back, Style
import re

class Monkey:
    def __init__(self, start_items, operation, divisible, truemonkey, falsemonkey):
        self.items = start_items
        if operation[0] == "*":
            self.operation = "mul"
        elif operation[0] == "+":
            self.operation = "add"
        if operation[2:] == "old":
            self.amount = "old"
        else:
            self.amount = int(operation[2:])


        self.divisible = divisible
        self.truemonkey = truemonkey
        self.falsemonkey = falsemonkey
        self.total_inspections = 0

    def inspect(self):
        items = []

        for item in self.items:
            old = item

            if self.operation == "mul":
                if self.amount == "old":
                    item = old ** 2
                else:
                    item = old * self.amount
            else:
                if self.amount == "old":
                    item = old + 2
                else:
                    item = old + self.amount

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
    operation = re.findall("new = .*$", f.readline())[0][6 + 4:]
    divisible = int(re.findall("[0-9][0-9]*", f.readline())[0])
    truemonkey = int(re.findall("[0-9][0-9]*", f.readline())[0])
    falsemonkey = int(re.findall("[0-9][0-9]*", f.readline())[0])

    monkeys.append(Monkey(start_items, operation, divisible, truemonkey, falsemonkey))

    if f.readline() == "":
        break

for Round in range(1000):

    for monkey in monkeys:
        monkey.inspect()

        for i in range(0, len(monkey.items)):
            item = monkey.items[i]

            if item % monkey.divisible == 0:
                monkeys[monkey.truemonkey].items.append(item)
            else:
                monkeys[monkey.falsemonkey].items.append(item)

        monkey.items = []

    if Round % 100 == 0:
        print(Round)

    #print("Round:", Round + 1)

    #for monkey in monkeys:
    #    print(monkey.items)




totals = []
for monkey in monkeys:
    print(monkey.total_inspections)
    totals.append(monkey.total_inspections)

totals.sort(reverse=True)

print(totals[0], "*", totals[1], "=", totals[0] * totals[1])

