import math
import random
import ru_local as ru


def count_time(ln, minute):
    hours, minutes = ln.split(':')
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


client_left = 0
gas_lost = 0
type_of_gas = 0
money_lost = 0

price = dict.fromkeys([ru.gas_80, ru.gas_92, ru.gas_95, ru.gas_98], 0)
price[ru.gas_98] = 67
price[ru.gas_95] = 52
price[ru.gas_92] = 49
price[ru.gas_80] = 25

sold = dict.fromkeys([ru.gas_80, ru.gas_92, ru.gas_95, ru.gas_98], 0)

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

howlong = []
for i in range(len(howmuch)):
    t = math.ceil(int(howmuch[i]) / 10)
    if t == 1:
        t = t + random.randint(0, 1)
    else:
        t = t + random.randint(-1, 1)
    howlong.append(t)

for i in range(len(time)):
    times_out = []
    for key, values in cars.items():
        for car in values:
            if car[-1] < time[i]:
                times_out.append(car[-1])
    times_out.sort()

    for t in times_out:
        for key, values in cars.items():
            for car in values:
                if car[-1] == t:
                    current_queue[key] -= 1
                    x = values.pop(values.index(car))
                    final = ''
                    for s in x[:-2]:
                        final += str(s) + ' '
                    print(ru.out_1, t, ru.out_2, final, ru.out_3)
                    for col, m in max_queue.items():
                        benz_str = ' '.join(column[col])
                        num = '*' * current_queue[col]
                        print(ru.situation_1, col, ru.situation_2, m, ru.situation_3, benz_str, ru.situation_4+num)

    min_gas = float('inf')
    gas_station = 0
    for col, gas in column.items():
        if gas_type[i] in gas:
            if current_queue[col] < max_queue[col] and current_queue[col] < min_gas:
                min_gas = current_queue[col]
                gas_station = col

    if gas_station != 0:
        current_queue[gas_station] += 1
        if end_time[gas_station] < time[i]:
            end_time[gas_station] = count_time(time[i], howlong[i])
        else:
            end_time[gas_station] = count_time(end_time[gas_station], howlong[i])
        print(ru.in_1, time[i], ru.in_2, time[i], gas_type[i], howmuch[i], howlong[i],
              ru.in_3, gas_station)
        for col, m in max_queue.items():
            benz_str = ' '.join(column[col])
            num = '*' * current_queue[col]
            print(ru.situation_1, col, ru.situation_2, m, ru.situation_3, benz_str, ru.situation_4+num)
        sold[gas_type[i]] += int(howmuch[i])

        cars[gas_station].append([time[i], gas_type[i], howmuch[i], howlong[i], gas_station, end_time[gas_station]])

    else:
        client_left += 1
        gas_lost += int(howmuch[i])
        money_lost += int(howmuch[i]) * price.get(gas_type[i])


with open('output.txt', 'w', encoding='utf-8') as f_out:
    print(ru.report_1, file=f_out)
    print(ru.report_2, file=f_out)
    overall = 0
    for key, value in sold.items():
        print(key, ': ', value, ru.report_3, sep='', file=f_out)
        overall += value * price[key]
    print(ru.report_4, overall, ru.report_5, file=f_out)
    print(ru.report_6, client_left, ru.report_7, file=f_out)
    print(ru.report_8, money_lost, ru.report_5, file=f_out)
    print(ru.report_9, gas_lost, ru.report_10, file=f_out)
