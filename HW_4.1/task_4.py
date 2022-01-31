print('\033[44m' + '\033[30m' + 'Russian ruble converter' + '\033[0m')

dict_cur = {
    'USD': 0.0129,  # => Доллар США
    'EUR': 0.0114,  # => ЕВРО
    'CHF': 0.0118,  # => Швейцарский франк
    'GBP': 0.0095,  # => Фунт стерлингов
    'CNY': 0.0818  # => Китайский юань
}

bol = True

stop = '\033[41m' + 'You are out of the program' + '\033[0m'
empty = '\033[31m' + 'You have entered an empty field.' + '\033[0m'


def currency_converter(currency, money, array):
    for key, value in array.items():
        if key == currency:
            converter = round(value * money, 2)
            return print(f'Converted amount {money} RUB = {converter} {key}')


while bol:
    amount_money = input('\033[1m' + 'Enter the amount of money: ' + '\033[0m')  # => российский рубль
    try:
        amount_money = int(amount_money)
        if amount_money > 0:
            while bol:
                сur_converter = input('\033[1m' + "Enter the currency ['USD','EUR','CHF','GBP','CNY']: " + '\033[0m')  # => выбор валюты
                сur_converter = сur_converter.upper()
                if dict_cur.__contains__(сur_converter):
                    currency_converter(сur_converter, amount_money, dict_cur)
                    bol = False
                elif сur_converter == 'STOP':
                    print(stop)
                    bol = False
                elif not сur_converter:
                    print(empty)
                else:
                    print('\033[31m' + 'You entered it incorrectly. Try again.' + '\033[0m')
        else:
            print('\033[31m' + 'You entered a negative number. Try again.' + '\033[0m')
    except ValueError:
        amount_money = amount_money.upper()
        if amount_money == 'STOP':
            print(stop)
            bol = False
        elif not amount_money:
            print(empty)
        else:
            print('\033[31m' + 'You have entered a string in the field. Enter a number.' + '\033[0m')
