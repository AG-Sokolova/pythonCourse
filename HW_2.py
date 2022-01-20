import math

# Arithmetic
print('\033[1m' + '\033[94m' + 'Arithmetic' + '\033[94m' + '\033[0m')

#  1. Создать переменную item_1 типа integer.
item_1 = 5
print("item_1:", item_1)

#  2. Создать переменную item_2 типа integer.
item_2 = 4
print("item_2:", item_2)

#  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1 + item_2

#  4. Вывести result_sum в консоль.
print('result_sum:', result_sum)

#  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
if item_1 < item_2:
    result_subtr = item_2-item_1
else:
    result_subtr = item_1-item_2

#  6. Вывести result_subtr в консоль.
print('result_subtr:', result_subtr)

#  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
result_multi = item_1*item_2

#  8. Вывести result_multi в консоль.
print('result_multi:', result_multi)

#  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_exp = item_1**item_2

#  10. Вывести result_exp в консоль.
print('result_exp:', result_exp)

#  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_exp = math.pow(item_1, item_2)

#  12. Вывести result_m_exp в консоль.
print('result_m_exp:', result_m_exp)

#  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = item_2 ** (1/2)

#  14. Вывести result_s_root в консоль.
print('result_s_root:', result_s_root)

#  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
result_m_s_root = math.sqrt(item_2)

#  16. Вывести result_m_s_root в консоль.
print('result_m_s_root:', result_m_s_root)

#  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
result_mp_s_root = math.pow(item_2, 1/2)

#  18. Вывести result_mp_s_root в консоль.
print('result_mp_s_root', result_mp_s_root, '\n')

#  19. Присвоить переменной item_1 odd значение
item_1 = 5
if item_1 % 2 != 0:
    print('item_1:', item_1, ' - odd')
else:
    print(item_1, ' - item_1 должно быть нечетным! Введите новое число.')

#  20. Присвоить переменной item_2 even значение
item_2 = 4
if item_2 % 2 == 0:
    print('item_1:', item_2, ' - even')
else:
    print(item_2, ' - item_2 должно быть четным! Введите новое число.')

#  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
result_division = item_1/item_2

#  22. Вывести result_division в консоль.
print('result_division:', result_division)

#  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)

#  24. Вывести result_m_floor в консоль.
print('result_m_floor:', result_m_floor)

#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_division)

#  26. Вывести result_m_ceil в консоль.
print('result_m_ceil:', result_m_ceil)

#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = round(result_division)
# result_int = int(round(result_division))

#  28. Вывести result_int в консоль.
print('result_int:', result_int)

#  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1//item_2

#  30. Вывести result_no_division_loss в консоль.
print('result_no_division_loss:', result_no_division_loss)

#  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2

#  32. Вывести result_division_loss в консоль.
print('result_division_loss:', result_division_loss)



# Дальше будет реализация через арифметические действия с присваиванием.
print('\033[1m' + '\033[94m' + 'Aрифметические действия с присваиванием' + '\033[94m' + '\033[0m')

#  33. Создать переменную item_3 и присвоить ей целое число
item_3 = 50
print('item_3:', item_3)

#  34. Прибавить 10 к item_3 с присвоением.
item_3 += 10

#  35. Вывести item_3 в консоль.
print('item_3 + 10 =', item_3)

#  36. Отнять 5 от item_3 с присвоением.
item_3 -= 5

#  37. Вывести item_3 в консоль.
print('item_3 - 5 =', item_3)

#  38. Умножить item_3 на 3 с присвоением.
item_3 *= 3

#  39. Вывести item_3 в консоль.
print('item_3 * 3 =', item_3)

#  40. Разделить item_3 на 2 с присвоением.
item_3 /= 2

#  41. Вывести item_3 в консоль.
print('item_3 / 2 =', item_3)

#  42. Возвести в степень 2 item_3 с присвоением.
item_3 **= 2

#  43. Вывести item_3 в консоль.
print('item_3 pow 2 =', item_3)

#  44. Найти квадратный корень item_3 с присвоением.
item_3 **= 0.5

#  45. Вывести item_3 в консоль.
print('item_3 sqrt 2 =', item_3)

#  46. Присвоить остаток от деления item_3
item_3 %= item_3

#  47. Вывести item_3 в консоль.
print('item_3 % item_3 =', item_3)


# Boolean
print('\033[1m' + '\033[94m' + 'Boolean' + '\033[94m' + '\033[0m')
#  48. Создать переменную b_item_t и присвоить True
b_item_t = True
print('b_item_t:', b_item_t)

#  49. Создать переменную b_item_f и присвоить False
b_item_f = False
print('b_item_f:', b_item_f)

#  50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_relult_sum = b_item_t + b_item_f

#  51. Вывести b_item_relult_sum в консоль.
print('b_item_relult_sum:', b_item_relult_sum)

#  52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_relult_subtr = b_item_t - b_item_f

#  53. Вывести b_item_relult_subtr в консоль.
print('b_item_relult_subtr:', b_item_relult_subtr)

#  54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
b_item_relult_multi = b_item_t * b_item_f

#  55. Вывести b_item_relult_multi в консоль.
print('b_item_relult_multi:', b_item_relult_multi)

#  56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
# b_item_relult_division = b_item_t / b_item_f

#  57. Вывести b_item_relult_division в консоль. (Получить ошибку)
# print('b_item_relult_division:', b_item_relult_division)
print('55 и 56 пункт - комментарии')

#  58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_t_int = int(b_item_t)

#  59. Вывести b_item_1_int в консоль.
print('b_item_t_int:', b_item_t_int)

#  60. Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int
b_item_f_int = int(b_item_f)

#  61. Вывести b_item_2_int в консоль.
print('b_item_f_int:', b_item_f_int)
