# https://cash.rbc.ru/converter.html?from=RUR&to=CNY&sum=5000&date=&rate=cbrf
print('\033[44m' + '\033[30m' + 'Конвертер российского рубля к доллару США' + '\033[0m')

item_usd = 0.0129

amountMoney = int(input('\033[1m' + 'Введите количество денег: ' + '\033[m'))
converter = item_usd * amountMoney

print('Конвертированная сумма', amountMoney, 'рублей =', converter, 'долларов')
