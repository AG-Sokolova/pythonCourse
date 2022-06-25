piece_div = 1

n = input('Введите натуральное число: ')

def number_divisors(num, i=1):
    array = []
    while i <= num:
        if num % i == 0:
            array.append(i)
        i += 1
    return array


if n.isdigit():
    n = int(n)
    # 1
    list_div = number_divisors(n)
    print(f'Список всех делителей числа {n} =', list_div)  # =>  список всех делителей
    # 2
    sum_div = sum(list_div)
    print(f'Cумму делителей числа {n} =', sum_div)  # =>  сумма делителей
    # 3
    for val in list_div:
        piece_div *= val
    print(f'Произведение делителей числа {n} =', piece_div)  # => произведение делителей
else:
    print('Неизвестно!')


# def number_divisors(num, i=1):
#     arr = []
#     while i * i <= num:
#         if num % i == 0:
#             arr.append(i)
#             if i != num//i:
#                 arr.append(num//i)
#         i += 1
#     arr.sort()
#     return arr

# try:
#     n = int(n)  # => строку преобразовать в число
#     n = n if n > 0 else abs(n)  # => возвращает положительное число
#     # 1
#     list_div = number_divisors(n)
#     print(f'Список всех делителей числа {n} =', list_div)  # =>  список всех делителей
#     # 2
#     sum_div = sum(list_div)
#     print(f'Cумму делителей числа {n} =', sum_div)  # =>  сумма делителей
#     # 3
#     for val in list_div:
#         piece_div *= val
#     print(f'Произведение делителей числа {n} =', piece_div)  # => произведение делителей
# except ValueError:
#     print('Неизвестно!')