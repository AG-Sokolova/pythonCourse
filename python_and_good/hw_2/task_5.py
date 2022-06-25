import random

n = random.randint(5, 12)

array_num = [n]

num = n
container = 0
while container < 6:
    num = num + 2
    array_num.append(num)
    container += 1

dict_num = {
    "max": max(array_num),
    "min": min(array_num),
    "avg": sum(array_num)/len(array_num),
    "sum": sum(array_num)
}

print('Random number =', n)
print('List =', array_num)
print('Dict =', dict_num)