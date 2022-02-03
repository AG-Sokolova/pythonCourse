from random import random, randint, shuffle
from HW_5_1.func import plit_list, lists_even_odd, list_100


list_int_numb = []  # => целые числа
list_even_numb = []  # => четные числа
list_odd_numb = []  # => нечетные числа
list_rnd_int_num = []  # => рандомные числа

list_result = []  # => результат вычислений

stars_5 = []
list_sum = []  # => сумма каждого внутреннего списка из 5_stars

# 1
for item in range(1, 30):
    list_int_numb.append(item)
print('1. создаст список целых чисел:', list_int_numb)

# 2
for item in range(1, 20):
    if item % 2 == 0:
        list_even_numb.append(item)
print('2. создаст список целых чётных чисел:', list_even_numb)

# 3
for item in range(1, 20):
    if item % 2 != 0:
        list_odd_numb.append(item)
print('3. создаст список целых нечётных чисел:', list_odd_numb)

# 4
for item in list_int_numb:
    if item % 2 == 0:
        list_result.append(item)
print('4. из списка целых чисел выведет чётные числа:', list_result)

# 5
list_result.clear()  # очистить список результатов
for item in list_int_numb:
    if item % 2 != 0:
        list_result.append(item)
print('5. из списка целых чисел выведет нечётные числа:', list_result)

# 6
list_result.clear()  # очистить список результатов
for item in list_int_numb:
    if item % 2 == 0:
        if item % 5 == 0:
            list_result.append(item)
print('6. из списка целых чисел выведет чётные числа которые делятся на 5 без остатка:', list_result)

# 7
count = 0  # количество
for item in list_int_numb:
    if item % 2 == 0:
        if item % 5 == 0:
            count += 1
print('7. из списка целых чисел выведет количество чётных чисел которые делятся на 5 без остатка', count)

# 8
# Вариант 1
list_rnd_int_num = [randint(0, 10) for i in range(1, 10)]
# Вариант 2
# for item in range(10):
#     num = int(random()*(10-1)+1)
#     list_rnd_int_num.append(num)
# Вариант 3
# for item in range(1, 10):
#     list_rnd_int_num.append(item)
# shuffle(list_rnd_int_num)
print('8. cоздаст список целых рандомных чисел:', list_rnd_int_num)

# 9
list_result.clear()  # очистить список результатов
print('9. получив любой из созданных списков, разобьёт его на списки по 5 элементов:')
list_result = plit_list(list_int_numb, 5)
for key, value in enumerate(list_result):
    print(f'---- список {key+1}: {value}')

# 10
print('10. получив любой из созданных списков,  вернёт 2 списка')
print('---- cписок четных чисел:', lists_even_odd(list_int_numb)[0])
print('---- cписок нечетных чисел:', lists_even_odd(list_int_numb)[1])
#
# 11
while len(stars_5) < 5:
    list_new = [randint(0, 200) for i in range(1, 6)]
    stars_5.append(list_new)

print('11. список под названием 5_stars из списков по 5 элементов целых чисел:', stars_5)

# 12
for items, value in enumerate(stars_5):
    count = 0
    for i in value:
        count += i
    list_sum.append(count)
print('12. список из сумм каждого внутреннего списка из 5_stars: ', list_sum)

# 13
print('13. получив список stars_5,  вернёт 2 списка:')
print('---- сумма чисел которых >= 100:', list_100(stars_5)[2])
print('---- сумма чисел которых < 100:', list_100(stars_5)[3])
