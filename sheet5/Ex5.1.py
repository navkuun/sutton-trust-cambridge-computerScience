import math
import numpy as np
import os

readfile = open("data.txt", "r")
mylist = []
mean = 0
for line in readfile:
    value = int(line)
    mean += value
    mylist.append(value)

mean = mean / len(mylist)

summ = 0
for x in mylist:
    summ += x - mean

std = np.std(mylist)
print(f"mean={mean}")
print(f"sd={std}")
