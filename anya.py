with open('start.txt', encoding='utf-8') as f_in:
    line = f_in.readline().strip().split()
    column = {}
    max_queue = {}
    current_queue = {}
    end_time = {}
    while line:
        column[line[0]] = line[2:]
        max_queue[line[0]] = line[1]
        current_queue[line[0]] = 0
        end_time[line[0]] = 0
        line = f_in.readline().strip().split()


print(column)
print(max_queue)

with open('input.txt', encoding='utf-8') as f:
    time = []
    howmuch = []
    gas_type = []
    line = f.readline().strip()
    line = line.split()
    while line:
        time.append(line[0])
        howmuch.append(line[1])
        gas_type.append(line[-1])
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
print(gas_type)


for i in range(len(time)):

    min_gas = float('inf')
    for col, gas in column.items():
        if gas_type[i] in gas:
            if current_queue[col] < min_gas:
                min_gas = current_queue[col]

