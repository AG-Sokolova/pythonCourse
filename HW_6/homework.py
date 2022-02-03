import random
import string


import csv

list_names = []
list_file = ['file/empty.csv',  # => 0
             'file/digits.csv',  # => 1
             'file/names.csv',  # => 2
             'file/emals.csv', # => 3
             'file/nne.csv',  # => 4
             'file/digits_2.csv',  # => 5
             'file/names_2.csv',  # => 6
             'file/emals_2.csv'  # => 7
             'file/nne_2.csv'  # => 8
             ]


# 1
with open(list_file[0], 'w', newline='') as empty_csv:
    # empty
    pass  # or write
empty_csv.close()

# 2
with open(list_file[1], 'w', newline='') as digits_csv:
    col = ['number']
    write = csv.DictWriter(digits_csv, fieldnames=col)
    write.writeheader()
    for i in range(0, 150):
        num = {'number': i}
        write.writerow(num)
digits_csv.close()

# 3
file = 'file/gen_names.txt'
with open(file, 'r') as gen_names_txt:
    lines = gen_names_txt.read().splitlines()
    for line in lines:
        list_names.append({'name': line})
gen_names_txt.close()

with open(list_file[2], 'w', newline='') as names_csv:
    col = ['name']
    write = csv.DictWriter(names_csv, fieldnames=col)
    write.writeheader()
    write.writerows(list_names)
names_csv.close()


# 4
def rnd_name_mail(length, bol=True):
    letters = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


with open(list_file[3], 'w', newline='') as email_csv:
    col = ['email']
    write = csv.DictWriter(email_csv, fieldnames=col)
    write.writeheader()
    i = 0
    while i < 100:
        mail = {'email': f'{rnd_name_mail(8)}@gmail.com'}
        write.writerow(mail)
        i += 1
email_csv.close()


# 5
