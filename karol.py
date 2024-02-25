with open('input.txt', encoding='utf-8') as f:
    time = []
    howmuch = []
    type = []
    line = f.readline().strip()
    line = line.split()
    while line != []:
        time.append(line[0])
        howmuch.append(line[1])
        type.append(line[-1])
        line = f.readline().strip()
        line = line.split()

import math
import random

for i in range(len(howmuch)):
    t = math.ceil(int(howmuch[i]) / 10)
    if t == 1:
        t = t + random.randint(0, 1)
    else:
        t = t + random.randint(-1, 1)
    howmuch[i] = t

print(time)
print('')
print(howmuch)
print('')
print(type)