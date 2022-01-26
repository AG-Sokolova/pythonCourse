# https://cash.rbc.ru/converter.html?from=RUR&to=CNY&sum=5000&date=&rate=cbrf
print('\033[44m' + '\033[30m' + 'Конвертер российского рубля' + '\033[0m')

item_usd = 0.0129  # => Доллар США
item_eur = 0.0114  # => ЕВРО
item_chf = 0.0118  # => Швейцарский франк
item_gbr = 0.0095  # => Фунт стерлингов
item_cny = 0.0818  # => Китайский юань

list_item = [item_usd, item_eur, item_chf, item_gbr, item_cny]
list_currency = ['долларов', 'евро', 'франков', 'стерлингов', 'юань']

amountMoney = int(input('\033[1m' + 'Введите количество денег: ' + '\033[0m'))  # => российский рубль

for i in range(len(list_item)):
    converter = round(list_item[i] * amountMoney, 2)
    print('Конвертированная сумма', amountMoney, 'рублей =', converter, list_currency[i])
