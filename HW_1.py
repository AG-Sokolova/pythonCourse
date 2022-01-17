import math
# 1) Создать переменную типа String
type_str = 'Hello, world'

# 2) Создать переменную типа Integer
type_int = 32

# 3) Создать переменную типа Float
type_float = 3.14

# 4) Создать переменную типа Bytes
type_bytes = bytes(6)

# 5) Создать переменную типа List
type_list = [type_str, type_float, 76, 5.5, ['python', type_int, [type_bytes]]]  # изменяемый тип
# print('Вывести элемент из переменной typeList:', type_list[4][2][0], end="\n\n")

# 6) Создать переменную типа Tuple
type_tuple = (type_int, 'python', type_float, 56, type_str)  # не изменяемый тип

# 7) Создать переменную типа Set
type_set = set('python')  # изменяемый тип

# 8. Создать переменную типа Frozen set
type_frozenSet = frozenset('python')  # не изменяемый тип

# 9) Создать переменную типа Dict
type_dict = {'name': 'Vsevolod',
             'age': 3,
             'sex': 'm',
             'preferences': {
                 "hobby": "run after the red dot from the laser pointer",
                 "favorite_movie": "Tom and Jerry",
                 "jubilee_season": "autumn"
             }
             }
# print('вывести элемент из переменной type_dict:', type_dict['preferences']['hobby'], end='\n \n')

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print('type_str:', '\n', type(type_str), type_str)
print('type_int:', '\n', type(type_int),  type_int)
print('type_float:', '\n', type(type_float), type_float)
print('type_list:', '\n', type(type_list), type_list)
print('type_bytes:', '\n', type(type_bytes), type_bytes)
print('type_tuple:', '\n', type(type_tuple), type_tuple)
print('type_dict:', '\n', type(type_dict), type_dict)
print('type_set', '\n', type(type_set), type_set)
print('type_frozenSet:', '\n', type(type_frozenSet), type_frozenSet)

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
str1 = 'Вис'
str2 = 'коза'
res = str1 + str2
print('\n', 'first line:', str1, '\n', 'second line:', str2, '\n', 'sum lines:', res)

# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
numb1 = 125
numb2 = 45
res = numb1 + numb2
print('\n', 'first number:', numb1, '\n', 'second number:', numb2)
print('sum:', res)

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
res = numb1 / numb2
print('divided:', res)

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
res = numb1 * numb2
print('multiply:', res)

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
res = round(numb1 / numb2)
print('round:', res)

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
res = numb1 % numb2
print('remainder of the division:', res)
print()

# 17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
res = (7 + 12)**3 + 7 * 4 - 44 / 2**4
print('Возвдение в степень:', res)

# 18) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print('\n', 'string:', str1, type(str1), '\n', 'number:', numb1, type(numb1))
print('string, integer:', str1, numb1)

# 19) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print('string + integer:', str1 + str(numb1))
