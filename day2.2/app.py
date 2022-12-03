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

def choose_hand(opponent, result):
    print("opponent:", opponent, "result:", result)
    if result == "draw":
        return opponent
    if result == "win":
        if opponent == "rock":
            return "paper"
        if opponent == "paper":
            return "scissors"
        if opponent == "scissors":
            return "rock"
    if result == "lose":
        if opponent == "rock":
            return "scissors"
        if opponent == "paper":
            return "rock"
        if opponent == "scissors":
            return "paper"


f = open("input", "r");

elves = []
elf = []

rps = {"A": "rock", "B": "paper", "C": "scissors", "X": "lose", "Y": "draw", "Z": "win"}

total = 0
for line in f.readlines():
    c1 = rps[line[0]]
    c2 = choose_hand(c1, rps[line[2]])
    print(calc_score(c1, c2))
    total += calc_score(c1, c2)

print(total)



