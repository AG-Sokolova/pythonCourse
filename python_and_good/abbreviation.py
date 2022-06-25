def get_abbreviation_alph(string):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ'
    new_string = ''

    for letter in string:
        for char in alphabet:
            if letter == char:
                new_string = new_string + letter
    return print(new_string)


def get_abbreviation_sp(string):
    space = ' '
    new_string = string[0]

    for num, letter in enumerate(string):
        if letter == space:
            new_string = new_string + string[num+1]
    return print(new_string.upper())


def get_abbreviation_spl(string):
    list_string = string.split()
    result = ''

    for i in range(0, len(list_string)):
        result = result + list_string[i][0]
    return print(result.upper())


get_abbreviation_alph('Поселковый Инициативный Заграничный Детский Единый Центр')
get_abbreviation_sp('Поселковый Инициативный Заграничный Детский Единый Центр')
get_abbreviation_spl('Поселковый инициативный Заграничный Детский Единый Центр')
