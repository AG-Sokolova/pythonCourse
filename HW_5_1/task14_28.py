from random import randint


# 14
# позже разобраться

# 15

# 16
list_name = ['Mark Moore', 'Mary Johnson', 'Terry McDonald', 'John Young',
             'Ellen Harris', 'Emma Jackson', 'James Jones', 'Lois Pittman',
             'Roger Williams', 'Alvin Elliott']
print('cписок имён:', list_name)

# 17
list_file = [f'file{i}.txt' for i in range(1, 10)]
print('cписок имён файлов', list_file)

# 18
list_reg = []
for items in list_name:
    random_date = f'{randint(1, 30)}.{randint(1, 12)}.2021'
    list_reg.append([items, random_date])
print('список, в котором список с элементами имя пользователя и дата регистрации:', list_reg)


