with open('start.txt', encoding='utf-8') as f_in:
    line = f_in.readline().strip().split()
    column = {}
    max_queue = {}
    current_queue = {}
    end_time = {}
    while line:
        column[int(line[0])] = line[2:]
        max_queue[int(line[0])] = int(line[1])
        current_queue[int(line[0])] = 0
        end_time[int(line[0])] = 0
        line = f_in.readline().strip().split()


print(column)
print(max_queue)

with open('input.txt', encoding='utf-8') as f:
    time = []
    howmuch = []
    gas_type = []
    line = f.readline().strip()
    line = line.split()
    while line != []:
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

final = []
for i in range(len(time)):
    s = [time[i], howmuch[i], gas_type[i]]
    s = tuple(s)
    final.append(s)

print(final)

"""
line = dict.fromkeys([1, 2, 3], 0)

for j in range(len(final)):
    possible = []
    for key, value in column.items():
        if final[j][-1] in value and max_queue[key] > line[key]:
            possible.append(key)
    if
    if len(possible) > 1:
        howlong = []
        for one in possible:
            howlong.append(line.get(one))
        mx = max(howlong)
        chosen_one = possible[howlong.index(mx)]
    elif len(possible) == 1:
        for one in possible:
            chosen_one = one
    line[chosen_one] += 1
    print(final[j][-1], end=' ')
    print(line)
"""
client_left = 0
gas_lost = 0
type_of_gas = 0
money_lost = 0

for i in range(len(time)):

    min_gas = float('inf')
    gas_station = 0
    for col, gas in column.items():
        if gas_type[i] in gas:
            if current_queue[col] < max_queue[col] and current_queue[col] < min_gas:
                min_gas = current_queue[col]
                gas_station = col

    # gas_station нашли в какую колонку поедет заправляться машина
    if gas_station != 0:
        current_queue[gas_station] += 1

    # Словарь с ценами на бензин
    price = dict.fromkeys(['АИ-80', 'АИ-92', 'АИ-95', 'АИ-98'], 0)
    price['АИ-98'] = 67
    price['АИ-95'] = 52
    price['АИ-92'] = 49
    price['АИ-80'] = 25


    # Проверяем, какой тип бензина могли купить, сколько литров и сколько всего клиентов уехали
    if gas_station == 0:
        client_left += 1
        gas_lost += int(howmuch[i])
        money_lost += int(howmuch[i]) * price.get(gas_type[i])

print('По итогам дня, АЗС:')
print('потеряла', client_left, 'клиентов')
print('возможную прибыль в размере', money_lost, 'рублей')
print('в общем не продав', gas_lost, 'литров бензина')


def time(line, minute):
    hours, minutes = line.split(':')
    hours, minutes = int(hours), int(minutes)
    if hours == 23 and minutes + minute >= 60:
        hours = 0
        minutes = (minutes + minute) % 60
    elif minutes + minute >= 60:
        hours += minute//60 + 1
        minutes = (minutes + minute) % 60
    else:
        minutes += minute
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    return hours + ':' + minutes

print(time('23:59', 1))