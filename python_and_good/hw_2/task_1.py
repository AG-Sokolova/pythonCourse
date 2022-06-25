a = 3
b = 4

operation = input('Введите математическую операцию (+, -, * или /): ')

match operation:
    case '+':
        result = a+b
        print(result)
    case '-':
        result = a-b
        print(result)
    case '/':
        result = 'Деление на ноль!' if b == 0 else a/b
        print(result)
    case '*':
        result = a*b
        print(result)
    case _:
        print('Неизвестно!')
