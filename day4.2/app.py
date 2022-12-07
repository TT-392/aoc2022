import numpy as np
import re


f = open("input", "r");

def check_if_contains(r11, r12, r21, r22):
    print()
    print("r11", r11);
    print("r12", r12);
    print("r21", r21);
    print("r22", r22);

    if r11 >= r21 and r11 <= r22:
        print(True)
        return True
    elif r12 >= r21 and r12 <= r22:
        print(True)
        return True
    if r21 >= r11 and r21 <= r12:
        print(True)
        return True
    elif r22 >= r11 and r22 <= r12:
        print(True)
        return True
    else:
        print(False)
        return False

total = 0;

for line in f.readlines():
    r11, r12, r21, r22 = re.findall("[0-9][0-9]*", line)
    total += check_if_contains(int(r11), int(r12), int(r21), int(r22))

print(total)




