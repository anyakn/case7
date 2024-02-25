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


"""print(time)
print('')
print(howmuch)
print('')
print(type)"""
print('')
print(howmuch)
import math
for i in range(len(howmuch)):
    t = math.ceil(int(howmuch[i]) / 10)
    howmuch[i] = t
print('')
print(howmuch)