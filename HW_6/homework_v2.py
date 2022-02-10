import csv
from func import read_txt_names, unique_email, gen_email

file_patch = 'generated_data'
dict_file_title = {'digits_2': file_patch + '/digits_2.csv',
                   'names_2': file_patch + '/names_2.csv',
                   'emals_2': file_patch + '/emals_2.csv',
                   'nne_2': file_patch + '/nne_2.csv'}

list_names = []  # лист сгенерированных имен
list_emals = []  # лист сгенерированных email

# получить уникальный список имен
read_txt_names(list_names)

# 6 - digits_2.csv файл с 1-м полем number, 300 строк [от 10 до 310]
with open(dict_file_title['digits_2'], 'w', newline='') as f_digits2_csv:
    col = ['number']
    write = csv.DictWriter(f_digits2_csv, fieldnames=col)
    write.writeheader()

    for i in range(10, 311):
        number = {'number': i}
        write.writerow(number)
f_digits2_csv.close()

# 7 - names_2.csv файл с 1-м полем name, 400 строк с разными именами
with open(dict_file_title['names_2'], 'w', newline='') as f_names2_csv:
    col = ['name']
    write = csv.DictWriter(f_names2_csv, fieldnames=col)
    write.writeheader()

    for items, value in enumerate(list_names):
        if items < 400:
            name = {'name': value}
            write.writerow(name)
f_names2_csv.close()

# 8 - emals_2.csv файл с 1-м полем email, 400 строк уникальных email [...@gmail.com]
with open(dict_file_title['emals_2'], 'w', newline='') as f_emails2_csv:
    col = ['email']
    write = csv.DictWriter(f_emails2_csv, fieldnames=col)
    write.writeheader()

    for items, value in enumerate(list_names):
        if items < 400:  # ограничение добавляемых строк
            email = unique_email(gen_email(value), list_emals)
            write.writerow({'email': email})
f_emails2_csv.close()

# 9 -  nne_2.csv файл с 3-мя полями(Number, Name, Email ), 450 строк
list_emals.clear()  # очистить список emails

with open(dict_file_title['nne_2'], 'w', newline='') as f_nne2_csv:
    cols = ['number', 'name', 'email']
    write = csv.DictWriter(f_nne2_csv, fieldnames=cols)
    write.writeheader()

    for item, value in enumerate(list_names):
        if item < 450:
            mail = unique_email(gen_email(value), list_emals)
            user = {'number': item+1,
                    'name': value,
                    'email': mail}
            write.writerow(user)
f_nne2_csv.close()
