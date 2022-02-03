from random import random, randint, shuffle
import func


list_int_numb = []  # => целые числа
list_even_numb = []  # => четные числа
list_odd_numb = []  # => нечетные числа
list_rnd_int_num = []  # => рандомные числа

list_result = []  # => результат вычислений

# 1
for item in range(1, 30):
    list_int_numb.append(item)
print('создаст список целых чисел:', list_int_numb)

# 2
for item in range(1, 20):
    if item % 2 == 0:
        list_even_numb.append(item)
print('создаст список целых чётных чисел:', list_even_numb)

# 3
for item in range(1, 20):
    if item % 2 != 0:
        list_odd_numb.append(item)
print('создаст список целых нечётных чисел:', list_odd_numb)

# 4
for item in list_int_numb:
    if item % 2 == 0:
        list_result.append(item)
print('из списка целых чисел выведет чётные числа:', list_result)

# 5
list_result.clear()  # очистить список результатов
for item in list_int_numb:
    if item % 2 != 0:
        list_result.append(item)
print('из списка целых чисел выведет нечётные числа:', list_result)

# 6
list_result.clear()  # очистить список результатов
for item in list_int_numb:
    if item % 2 == 0:
        if item % 5 == 0:
            list_result.append(item)
print('из списка целых чисел выведет чётные числа которые делятся на 5 без остатка:', list_result)

# 7
list_result.clear()  # очистить список результатов
count = 0  # количество
for item in list_int_numb:
    if item % 2 == 0:
        if item % 5 == 0:
            count += 1
print('из списка целых чисел выведет количество чётных чисел которые делятся на 5 без остатка', count)

# 8
# Вариант 1
# for item in range(10):
#     num = int(random()*(10-1)+1)
#     list_rnd_int_num.append(num)
# Вариант 2
for item in range(10):
    list_rnd_int_num.append(randint(1, 20))
# Вариант 3
# for item in range(1, 10):
#     list_rnd_int_num.append(item)
# shuffle(list_rnd_int_num)
print('cоздаст список целых рандомных чисел:', list_rnd_int_num)

# 9

# 10
