import numpy as np
import time
from colorama import Fore, Back, Style
import re

# created by chatgpt
def get_color_code(index):
    # Define a list of ANSI escape codes for text and background colors
    color_codes = [
        "\033[31m",  # Red (text)
        "\033[32m",  # Green (text)
        "\033[33m",  # Yellow (text)
        "\033[34m",  # Blue (text)
        "\033[35m",  # Magenta (text)
        "\033[36m",  # Cyan (text)
        "\033[37m",  # White (text)
    ]

    # Loop around to the beginning of the list if the index is too large
    index = index % len(color_codes)

    # Return the escape code at the given index
    return color_codes[index]


f = open("input", "r")

def get(hmap, x, y):
    if x < 0:
        return None 
    elif y < 0:
        return None 
    elif y >= len(hmap):
        return None 
    elif x >= len(hmap[y]):
        return None 

    return hmap[y][x]

hmap = []

class Square:
    def __init__(self, height, location):
        self.height = height
        self.pathlength = 99999999999
        self.location = location

    def get_neighbours(self, updown):
        neighbours = []

        for coord in [(self.location[0] + 1, self.location[1]), (self.location[0] - 1, self.location[1]), (self.location[0], self.location[1] - 1), (self.location[0], self.location[1] + 1)]:
            neighbour = get(hmap, coord[0], coord[1])
            if neighbour != None:
                neighbours.append(neighbour)
                        
        return neighbours

    def get_viable_neighbours(self, updown):
        neighbours = []

        for coord in [(self.location[0] + 1, self.location[1]), (self.location[0] - 1, self.location[1]), (self.location[0], self.location[1] - 1), (self.location[0], self.location[1] + 1)]:
            neighbour = get(hmap, coord[0], coord[1])
            if neighbour != None:
                if updown == "down":
                    if neighbour.height >= self.height - 1:
                        neighbours.append(neighbour)
                else:
                    if neighbour.height <= self.height + 1:
                        neighbours.append(neighbour)
                        
        return neighbours

    def calc_length(self):
        for neighbour in self.get_viable_neighbours("up"):
            if neighbour.pathlength < self.pathlength - 1:
                self.pathlength = neighbour.pathlength + 1

    def __str__(self):
        if self.pathlength < 999:
            if self.pathlength < 10:
                return "  " + str(self.pathlength)
            elif self.pathlength < 100:
                return " " + str(self.pathlength)
            else:
                return str(self.pathlength)
        else:
            return "000"




y = 0
for line in f.readlines():
    mapline = []
    x = 0
    for c in line[:-1]:
        if c == "S":
            height = 0
            start = (x, y)
        elif c == "E":
            height = ord('z') - ord('a')
            end = (x, y)
        else:
            height = ord(c) - ord('a')
            
        mapline.append(Square(height, (x, y)))


        x += 1
    hmap.append(mapline)

    y += 1

end_square = get(hmap, end[0], end[1])
end_square.pathlength = 0
print(end_square.height)

squares = set([end_square])

i = 0
while(len(squares) != 0):
    print("len:", len(squares))
    print(i)

    newsquares = set([])
    for square in squares:

        for neighbour in square.get_neighbours("down"):
            old_length = neighbour.pathlength
            neighbour.calc_length()
            
            if old_length != neighbour.pathlength:
                newsquares.add(neighbour)

    squares = newsquares
    i += 1



for y in range(len(hmap)):
    for x in range(len(hmap[y])):
        height = hmap[y][x].height
        print(get_color_code(height), end='')
        print(hmap[y][x], end='')
        print("\033[37m", end='')
    print()

    for x in range(len(hmap[y])):
        height = hmap[y][x].height
        print(get_color_code(height), end='  ')
        print(chr(ord('a') + height), end='')
        print("\033[37m", end='')
    print()

start_square = get(hmap, start[0], start[1])
print(start_square)
