def count_time(line, minute):
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


with open('start.txt', encoding='utf-8') as f_in:
    line = f_in.readline().strip().split()
    column = {}
    max_queue = {}
    current_queue = {}
    end_time = {}
    cars = {}
    while line:
        column[int(line[0])] = line[2:]
        max_queue[int(line[0])] = int(line[1])
        current_queue[int(line[0])] = 0
        end_time[int(line[0])] = '00:00'
        cars[int(line[0])] = []
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

howlong = []
for i in range(len(howmuch)):
    t = math.ceil(int(howmuch[i]) / 10)
    if t == 1:
        t = t + random.randint(0, 1)
    else:
        t = t + random.randint(-1, 1)
    howlong.append(t)

print(time)
print('')
print(howmuch)
print('')
print(howlong)
print('')
print(gas_type)


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

        if end_time[gas_station] < time[i]:
            end_time[gas_station] = count_time(time[i], howlong[i])
        else:
            end_time[gas_station] = count_time(end_time[gas_station], howlong[i])

        # client_data = f'{time[i]} {gas_type[i]} {howmuch[i]} {howlong[i]} {gas_station}'
        print(f'В {time[i]} новый клиент:  {time[i]} {gas_type[i]} {howmuch[i]} {howlong[i]} '
              f'встал в очередь к автомату №{gas_station}')
        for col, m in max_queue.items():
            benz_str = ' '.join(column[col])
            num = '*' * current_queue[col]
            print(f'Автомат №{col} максимальная очередь: {m} Марки бензина {benz_str} ->{num}')

    # выводим когда кто то заехал



