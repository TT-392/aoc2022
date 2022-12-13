import numpy as np
import re

needed_space = 30000000
total_size = 70000000

dirsizes = []

class Tree:
    def __init__(self):
        self.tree = {"/":
            {}
        }
        self.location = "/"

    def get_size_subtree(self, subtree):
        size = 0
        for i in subtree:
            if type(subtree[i]) == dict:
                size += self.get_size_subtree(subtree[i])
            else:
                size += subtree[i]

        return size
    
    def print_subtree(self, subtree, depth):
        for i in subtree:
            print(depth * " ", end="")

            if type(subtree[i]) == dict:
                size = self.get_size_subtree(subtree[i])
                print(i, "size =", size)
                global dirsizes
                dirsizes.append(size)

                if size <= 100000:
                    self.total += size

                self.print_subtree(subtree[i], depth+1)
            else:
                print(i, subtree[i])


    def print(self):
        self.total = 0
        self.print_subtree(self.tree, 0)
        global used_space
        used_space = self.total
        print(self.total)


    def put(self, path, size):
        # size -1 = dir
        location = self.tree["/"]

        for Dir in path.split("/")[1:-1]:
            if Dir in location:
                location = location[Dir]
            else:
                location[Dir] = {}
                location = location[Dir]

        file = path.split("/")[-1]
        if size != -1:
            location[file] = size
        else:
            location[file] = {}



tree = Tree()

f = open("input")

path = ""

for line in f.readlines():
    if line[0] == "$":
        command = line[2:-1]
        if command[:2] == "cd":
            args = command[3:]

            if args == "/":
                path = ""
            elif args == "..":
                path = "/".join(path.split("/")[:-1])
            else:
                path += "/" + args



    else:
        line = line[:-1].split(" ")
        filename = line[1]
        filetype = line[0]

        if filetype == "dir":
            filetype = -1
        else:
            filetype = int(filetype)

        tree.put(path + "/" + filename, filetype)

tree.print()

used_space = max(dirsizes)
print(dirsizes)
print(total_size - used_space)
need_to_free = needed_space - (total_size - used_space)

sufficient_dirs = []
for dirsize in dirsizes:
    if dirsize >= need_to_free:
        sufficient_dirs.append(dirsize)
print(min(sufficient_dirs))







