import csv
import json

users = {}
users = {
    1: 'Vadim',
    2: 'Irina',
    'name': 'Alex',
}
users_2 = {
    1: 'Vadim',
    2: 'Irina',
    3: ['Alex', 'Olga', 'Victor']
}
users_3 ={
    1: 'Vadim',
    2: 'Irina',
    3: users
}
users_4 = {
    1: 'Vadim',
    2: 'Irina',
    3: {'name': 'George',
        'age': 30,
        'hight': 178,
        'family': {'children': ['Anna', 'Alex']}
        }
}
# aa = {True: {'name': 'George'}}
# print('aa = ', aa)

# print('users', users)
# print('users_2', users_2)
# print('users_3', users_3)
# print('users_4', users_4)

# item_1 = users_4[3]['name']  # => George
# print(item_1)

# item_1 = users_4[3]['family']['children'][0]  # => Anna
# print(item_1)

# users_4[3]['age'] = 40
# print(users_4[3]['age'])  # => 40

# users_4.pop(2)  # => удаляет 2: 'Irina'
# print(users_4)

# users_4.pop(2)  # => удаляет 2: 'Irina'
# users_4[2] = 'Ignat'   # => добавляет 2: 'Ignat'
# print(users_4)

# users_4[2] = users_4.pop(2)  # =>  в конце dict заново получем 2: 'Irina'
# print(users_4)

# users_4.update({2: 'Ignat'})  # => 'Irina' заменяется на 'Ignat'
# print(users_4)

# print(len(users_4))  # => 3

# for k in users_4:
#     print(k)

# for k, v in users_4.items():
#     if k == 2:
#         print(k, v)

# name = ['Vadim', 'Misha']
# age = [30]
# users_4_1 = dict.fromkeys(name, age)  # => {'Vadim': [30, 4], 'Misha': [30, 4]}
# print(users_4_1)

name = ['Vadim', 'Misha']
age = [30, 20]
u_4 = {}
for i in range(0, len(name)):
    u_4[name[i]] = age[i]  # => {'Vadim': 30, 'Misha': 20}
print(u_4)

title = 'json_1.json'
with open(title, 'w') as file_write:
    json.dump(u_4, file_write)

with open(title, 'r') as file_read:
    read = file_read.read()
    js_obj = json.loads(read)
    print(js_obj['Vadim'])

