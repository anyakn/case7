import math
import random


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


client_left = 0
gas_lost = 0
type_of_gas = 0
money_lost = 0

# Словарь с ценами на бензин
price = dict.fromkeys(['АИ-80', 'АИ-92', 'АИ-95', 'АИ-98'], 0)
price['АИ-98'] = 67
price['АИ-95'] = 52
price['АИ-92'] = 49
price['АИ-80'] = 25

# Словарь с подсчётам проданых литров
sold = dict.fromkeys(['АИ-80', 'АИ-92', 'АИ-95', 'АИ-98'], 0)

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
                    print(f'В {t} клиент: {final} заправил свой автомобиль и покинул АЗС.')
                    for col, m in max_queue.items():
                        benz_str = ' '.join(column[col])
                        num = '*' * current_queue[col]
                        print(f'Автомат №{col} максимальная очередь: {m} Марки бензина {benz_str} ->{num}')

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
        # client_data = f'{time[i]} {gas_type[i]} {howmuch[i]} {howlong[i]} {gas_station} {end_time[gas_station]}'
        print(f'В {time[i]} новый клиент:  {time[i]} {gas_type[i]} {howmuch[i]} {howlong[i]} '
              f'встал в очередь к автомату №{gas_station}')
        for col, m in max_queue.items():
            benz_str = ' '.join(column[col])
            num = '*' * current_queue[col]
            print(f'Автомат №{col} максимальная очередь: {m} Марки бензина {benz_str} ->{num}')
        sold[gas_type[i]] += int(howmuch[i])

    # выводим когда кто то заехал
        cars[gas_station].append([time[i], gas_type[i], howmuch[i], howlong[i], gas_station, end_time[gas_station]])

    # Проверяем, какой тип бензина могли купить, сколько литров и сколько всего клиентов уехали
    else:
        client_left += 1
        gas_lost += int(howmuch[i])
        money_lost += int(howmuch[i]) * price.get(gas_type[i])


with open('output.txt', 'w', encoding='utf-8') as f_out:
    print('По итогам дня, АЗС:', file=f_out)
    print('Кол-во литров, проданное за сутки по каждой марке бензина:', file=f_out)
    overall = 0
    for key, value in sold.items():
        print(key, ': ', value, ' литров', sep='', file=f_out)
        overall += value * price[key]
    print('Общая сумма продаж за сутки:', overall, 'рублей', file=f_out)
    print('"Потеряно"', client_left, 'клиентов', file=f_out)
    print('Упущена возможная прибыль в размере', money_lost, 'рублей', file=f_out)
    print('Могли продать на', gas_lost, 'литров бензина больше.', file=f_out)
