# https://cash.rbc.ru/converter.html?from=RUR&to=CNY&sum=5000&date=&rate=cbrf
print('\033[44m' + '\033[30m' + 'Конвертер российского рубля' + '\033[0m')

amount_money = input('\033[1m' + 'Введите количество денег: ' + '\033[m')  # российский рубль

dict_cur = {
    'item_usd': 'долларов',
    'item_eur': 'евро',
    'item_chf': 'франков',
    'item_gbr': 'стерлингов',
    'item_cny': 'юань'
}
dict_items = {
    'item_usd': 0.0129,  # => Доллар США
    'item_eur': 0.0114,  # => ЕВРО
    'item_chf': 0.0118,  # => Швейцарский франк
    'item_gbr': 0.0095,  # => Фунт стерлингов
    'item_cny': 0.0818  # => Китайский юань
}


def currency_converter(money, d_cur, d_items):
    for k_item, v_item in d_items.items():
        for k_cur, v_cur in d_cur.items():
            if k_item == k_cur:
                converter = round(money * v_item, 2)
                print(f'Конвертированная сумма {money} рублей = {converter} {v_cur}')


try:
    amount_money = int(amount_money)
    if amount_money > 0:
        currency_converter(amount_money, dict_cur, dict_items)
    else:
        print("Введите положительное число.")
except ValueError:
    if not amount_money:
        print("Вы ввели пустое поле. Введите число.")
    else:
        print("Вы ввели не число. Введите число.")
