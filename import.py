import random
import math

randlist = ["string", 1.234, 28]

oneToTen = list(range(10))

randlist = randlist + oneToTen

print(randlist[0])

print("List Length :", len(randlist))

first3 = randlist[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

