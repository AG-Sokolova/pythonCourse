import random

array = []

n = random.randint(5, 9)
print('Рандомное число =', n)


for i in range(n, n**2):
    if i % 2 != 0:
        array.append(i)
print('Список нечетных чисел =', array)

# for value in array:
#     print(value, end='*')

delimiter = '*'
n_str = delimiter.join(map(str, array))
print(n_str)
