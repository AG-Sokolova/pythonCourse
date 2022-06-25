def valid_input(str):
    if len(str) != 0 and str.isdigit():
        return True
    return False

def calc(a, b, oper):
    a, b = int(a), int(b)
    if len(oper) != 0:
        match oper:
            case '+':
                print(a+b)
                return True
            case '-':
                print(a-b)
                return True
            case _: return True
    else:
        return False


flag = True
while flag:
    num_1 = input('Введите число a = ')
    num_2 = input('Введите число b = ')
    operat = input('Введите операцию = ')
    if valid_input(num_1) and valid_input(num_2):
            flag = calc(num_1, num_2, operat)
    else:
        flag = False