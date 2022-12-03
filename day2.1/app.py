import numpy as np

def calc_score(c1, c2):
    print(c1 + " vs " + c2)
    if c2 == "rock":
        shapescore = 1
    elif c2 == "paper":
        shapescore = 2
    elif c2 == "scissors":
        shapescore = 3

    if c2 == c1:
        return shapescore + 3
    elif c2 == "rock" and c1 == "paper":
        return shapescore + 0
    elif c2 == "paper" and c1 == "rock":
        return shapescore + 6
    elif c2 == "rock" and c1 == "scissors":
        return shapescore + 6
    elif c2 == "scissors" and c1 == "rock":
        return shapescore + 0
    elif c2 == "paper" and c1 == "scissors":
        return shapescore + 0
    elif c2 == "scissors" and c1 == "paper":
        return shapescore + 6
    else:
        print(c1, c2, "aaaa")



f = open("input", "r");

elves = []
elf = []

rps = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}

total = 0
for line in f.readlines():
    print(calc_score(rps[line[0]], rps[line[2]]))
    total += calc_score(rps[line[0]], rps[line[2]])

print(total)



