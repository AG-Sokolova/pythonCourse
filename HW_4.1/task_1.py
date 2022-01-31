# https://cash.rbc.ru/converter.html?from=RUR&to=CNY&sum=5000&date=&rate=cbrf

print('\033[44m' + '\033[30m' + 'Конвертер российского рубля к доллару США' + '\033[0m')

item_usd = 0.0129

amount_money = input('\033[1m' + 'Введите количество денег: ' + '\033[m')
amount_money = int(amount_money)

converter = item_usd * amount_money

print(f'Конвертированная сумма {amount_money} рублей = {converter} долларов')
