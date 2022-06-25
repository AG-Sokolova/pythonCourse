n = 56742

# list_n = []
# while n > 0:
#     list_n.append(n % 10)  # => получить самую правую цифру числа n
#     n //= 10  # => удалить самую правую цифру из числа n.
# list_n = list_n[::-1]  # => поменять порядок цифр на [5, 6, 7, 4, 2]


list_n = [int(x) for x in str(n)]  # => [5, 6, 7, 4, 2]

# 1
i, while_sum = 0, 0
while i < len(list_n):
    while_sum += list_n[i]
    i += 1
print('while_sum =', while_sum)

# 2
for_sum = 0
for val in list_n:
    for_sum += val
print('for_sum =', for_sum)

# 3
i, while_piece = 0, 1
while i < len(list_n):
    while_piece *= list_n[i]
    i += 1
print('while_piece =', while_piece)

# 4
for_piece = 1
for val in list_n:
    for_piece *= val
print('for_piece =', for_piece)