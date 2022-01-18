int_item = 10  # 1
comp_item = 18  # 2
mult_int = int_item * 2  # 3
item_2 = True   # 4
item_3 = False   # 5
item_4 = 0   # 6
item_5 = 1   # 7
usd_item = 'usd'   # 8
usd_usd_rate = 1   # 9
eur_item = 'eur'   # 10
usd_eur_rate = 0.86  # 11
uah_item = 'uah'  # 12
usd_uah_rate = 26.23  # 13
chf_item = 'chf'  # 14
usd_chf_rate = 0.91  # 15
rub_item = 'rub'  # 16
usd_rub_rate = 71.88  # 17
byn_item = 'byn'  # 18
usd_byn_rate = 2.46  # 19

# переменные
# print('int_item:', int_item)
# print('comp_item:', comp_item)
# print('mult_int:', mult_int)
# print('item_2:', item_2, ' | ', 'item_3:', item_3)
# print('item_4:', item_4, ' | ', 'item_5:', item_5)
# print('usd_usd_rate:', usd_usd_rate, ' - ', 'usd_item:', usd_item)
# print('usd_eur_rate:', usd_eur_rate, ' - ', 'eur_item:', eur_item)
# print('usd_uah_rate:', usd_uah_rate, ' - ', 'uah_item:', uah_item)
# print('usd_chf_rate:', usd_chf_rate, ' - ', 'chf_item:', chf_item)
# print('usd_rub_rate:', usd_rub_rate, ' - ', 'rub_item:', rub_item)
# print('usd_byn_rate:', usd_byn_rate, ' - ', 'byn_item:', byn_item)
# print()

# 20. Сделать if в котором будет условие: если mult_int больше comp_item, то вывести в консоль (“Переменная mult_int больше”, comp_item)
if mult_int > comp_item:
    print('Переменная mult_int больше', comp_item)

# 21. Создать переменную div_int в которй разделить int_item на 2
div_int = int_item / 2

# 22. Сделать if в котором будет условие: если div_int меньше comp_item, то вывести в консоль (“Переменная div_int меньше”, comp_item)
if div_int < comp_item:
    print('Переменная div_int меньше', comp_item)

# 23. Создать переменную item_1 в которй прибавить 10 к переменной int_item
item_1 = int_item + 10

# 4. Сделать if в котором будет условие: если item_1 меньше comp_item, то вывести в консоль (“Переменная item_1 меньше”, comp_item), иначе, вывести в консоль (“Переменная item_1 больше или равна”, comp_item)
if item_1 < comp_item:
    print('Переменная item_1 меньше', comp_item)
else:
    print('Переменная item_1 больше или равно', comp_item)

# 25. Сделать if в котором будет условие: если item_2, то вывести в консоль (“Переменная item_2 = ”, item_2), иначе, вывести в консоль (“Переменная item_2 = ”, item_3)
if item_2:
    print('Переменная item_2 =', item_2)
else:
    print('Переменная item_2 =', item_3)

# 26. Сделать if в котором будет условие: если item_3, то вывести в консоль (“Переменная item_3 = ”, item_2), иначе, вывести в консоль (“Переменная item_3 = ”, item_3)
if item_3:
    print('Переменная item_3 =', item_2)
else:
    print('Переменная item_3 =', item_3)

# 27. Сделать if в котором будет условие: если item_5, то вывести в консоль (“Переменная item_5 = ”, item_5), иначе, вывести в консоль (“Переменная item_5 = ”, item_4)
if item_5:
    print('Переменная item_5 =', item_5)
else:
    print('Переменная item_5 =', item_4)

# 28. Сделать if в котором будет условие: если item_4, то вывести в консоль (“Переменная item_4 = ”, item_5), иначе, вывести в консоль (“Переменная item_4 = ”, item_4)
if item_4:
    print('Переменная item_4 =', item_5)
else:
    print('Переменная item_4 =', item_4)

# 29. Создать переменную currency_convertor со значением item_2
currency_convertor = item_2
print('currency_convertor =', currency_convertor)

# 30. Сделать if в котором будет условие: если currency_convertor, то выполнять следующие шаги задания, иначе, вывести в консоль (“Переменная currency_convertor = ”, item_3)
if currency_convertor:
    currency_usd = usd_item  # 31.1 Создать переменную currency_usd со значением usd_item
    target_currency = eur_item  # 31.2 Создать переменную target_currency со значением eur_item
    target_currency_amount = 50  # 31.3 Создать переменную target_currency_amount значением 50
    currency_result = 0  # 31.4 Создать переменную currency_result со значением 0
    # 31.4 Сделать if в котором будет условие: если target_currency равен ‘eur’, то в теле этого if в значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_eur_rate. Результат вывести в консоль (target_currency_amount, eur_item, “=”, currency_result, usd_item)
    if target_currency == 'eur':
        currency_result = target_currency_amount * usd_eur_rate
        print(target_currency_amount, eur_item, '=', currency_result, usd_item)
        # 31.5 Сделать elif в котором будет условие: если target_currency равен ‘uah’, то в теле этого if в значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_uah_rate. Результат вывести в консоль (target_currency_amount, uah_item, “=”, currency_result, uah_item)
    elif target_currency == 'uah':
        currency_result = target_currency_amount * usd_uah_rate
        print(target_currency_amount, uah_item, '=', currency_result, uah_item)
        # 31.6 Сделать elif с остальными валютами…
    elif target_currency == 'chf':
        currency_result = target_currency_amount * usd_chf_rate
        print(target_currency_amount, chf_item, '=', currency_result, chf_item)
    elif target_currency == 'rub':
        currency_result = target_currency_amount * usd_rub_rate
        print(target_currency_amount, rub_item, '=', currency_result, rub_item)
    elif target_currency == 'byn':
        currency_result = target_currency_amount * usd_byn_rate
        print(target_currency_amount, byn_item, '=', currency_result, byn_item)
    # 31.7 Последним оставить else, при выполнений которого в консоль выведется (“Unknow currency”)
    else:
        print('Unknow currency')
else:
    print('Переменная urrency_convertor = ”, item_3')





