import re
import numpy as np
from helper import *

rock_color = (125, 125, 125)
sky_color = (0, 0, 0)
source_color = (255, 0, 0)
sand_color = (255, 255, 0)

source = [500, 0]

f = open("input", "r")

paths = []
for line in f.readlines():
    path = []
    splitline = re.findall("[0-9]+,[0-9]+", line)
    
    for coord in splitline:
        path.append([int(number) for number in coord.split(",")])

    paths.append(path)

print(paths)

minX = 9999999
minY = 9999999
maxX = 0
maxY = 0

for path in paths:
    for coord in path:
        if coord[0] < minX:
            minX = coord[0]
        if coord[1] < minY:
            minY = coord[1]
        if coord[0] > maxX:
            maxX = coord[0]
        if coord[1] > maxY:
            maxY = coord[1]

print(minX, minY, maxX, maxY)

xOffset = minX - 1
width = (maxX + 1) - (minX - 1) + 1
height = maxY + 1
print(width, height)

for path in paths:
    for coord in path:
        coord[0] -= xOffset


print(paths)

grid = [["." for i in range(0, width)] for j in range(0, height)]


for path in paths:
    for i in range(len(path) - 1):
        print(path[i], path[i + 1])
        coord1 = path[i]
        coord2 = path[i+1]

        diff = np.array(coord2) - np.array(coord1)

        print("diff:", diff)
        
        if diff[0] == 0:
            Dir = 1 if diff[1] > 0 else -1

            coord = coord1
            grid[coord[1]][coord[0]] = "#"
            while coord != coord2:
                coord[1] += Dir
                grid[coord[1]][coord[0]] = "#"

        if diff[1] == 0:
            Dir = 1 if diff[0] > 0 else -1

            coord = coord1
            grid[coord[1]][coord[0]] = "#"

            while coord != coord2:
                coord[0] += Dir
                grid[coord[1]][coord[0]] = "#"


    print()

grid[source[1]][source[0] - xOffset] = "+"

pixels = []
for line in grid:
    pixLine = []
    for pixel in line:
        if pixel == "#":
            pixLine.append(rock_color)
        elif pixel == "+":
            pixLine.append(source_color)
        else:
            pixLine.append(sky_color)
    pixels.append(pixLine)


genImage(pixels, "test.png")

novoid = True
i = 0
while novoid:
    sand = [source[0] - xOffset, source[1] + 1]
    while True:
        print(height)
        print(sand)
        if sand[1] == height - 1:
            print("aaa")
            novoid = False
            break
        if grid[sand[1] + 1][sand[0]] == ".":
            sand[1] += 1
        elif grid[sand[1] + 1][sand[0] - 1] == ".":
            sand[1] += 1
            sand[0] -= 1
        elif grid[sand[1] + 1][sand[0] + 1] == ".":
            sand[1] += 1
            sand[0] += 1
        else:
            grid[sand[1]][sand[0]] = "o"
            break

    pixels = []
    for line in grid:
        pixLine = []
        for pixel in line:
            if pixel == "#":
                pixLine.append(rock_color)
            elif pixel == "+":
                pixLine.append(source_color)
            elif pixel == "o":
                pixLine.append(sand_color)
            else:
                pixLine.append(sky_color)

        pixels.append(pixLine)

    fname = "sequence/frame%05d.png" % i
    genImage(pixels, fname)
    i += 1
print(i-1)
