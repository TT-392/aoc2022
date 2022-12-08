import numpy as np
from colorama import Fore, Back, Style
import re

def look(direction, grid, x, y):
    size = grid[y][x]
    visible = 1

    if direction == "up":
        for Y in range(y - 1, -1, -1):
            if grid[Y][x] >= size:
                return False

    elif direction == "down":
        for Y in range(y + 1, len(grid), 1):
            if grid[Y][x] >= size:
                return False

    elif direction == "right":
        for X in range(x - 1, -1, -1):
            if grid[y][X] >= size:
                return False

    elif direction == "left":
        for X in range(x + 1, len(grid[y]), 1):
            if grid[y][X] >= size:
                return False

    return True


f = open("input")

path = ""

grid = []

for line in f.readlines():
    gridline = []

    for c in line[:-1]:
        gridline.append([int(c), True])

    grid.append(gridline)



total = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        grid[y][x][1] = look("up", grid, x, y) | look("down", grid, x, y) | look("left", grid, x, y) | look("right", grid, x, y)

        if grid[y][x][1]:
            print(Style.RESET_ALL + str(grid[y][x][0]), end=" ")

            total += 1
        else:
            print(Fore.RED + str(grid[y][x][0]), end=" ")

    print()
print(total)
        







