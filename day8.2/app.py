import numpy as np
from colorama import Fore, Back, Style
import re

def look(direction, grid, x, y):
    size = grid[y][x][0]
    minsize = 0
    visible = 1

    score = 0

    if direction == "up":
        for Y in range(y - 1, -1, -1):
            score += 1

            if grid[Y][x][0] >= size:
                break

        return score

    elif direction == "down":
        for Y in range(y + 1, len(grid), 1):
            score += 1

            if grid[Y][x][0] >= size:
                break

        return score

    elif direction == "left":
        for X in range(x - 1, -1, -1):
            score += 1

            if grid[y][X][0] >= size:
                break

        return score

    elif direction == "right":
        for X in range(x + 1, len(grid[y]), 1):
            score += 1

            if grid[y][X][0] >= size:
                break

        return score


f = open("input")

path = ""

grid = []

for line in f.readlines():
    gridline = []

    for c in line[:-1]:
        gridline.append([int(c), True])

    grid.append(gridline)


Max = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        total = look("up", grid, x, y)
        total *= look("down", grid, x, y)
        total *= look("left", grid, x, y)
        total *= look("right", grid, x, y)

        print(grid[y][x][0], end="")
        print(total, end=" ")


        if total > Max:
            Max = total
    print()




print(Max)
        







