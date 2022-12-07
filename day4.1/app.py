import numpy as np
import re

def check_if_contains(r11, r12, r21, r22):
    if r11 >= r21 and r12 <= r22:
        return True
    elif r11 <= r21 and r12 >= r22:
        return True
    else:
        return False

f = open("input", "r");


total = 0;

for line in f.readlines():
    r11, r12, r21, r22 = re.findall("[0-9][0-9]*", line)
    total += check_if_contains(int(r11), int(r12), int(r21), int(r22))

print(total)




