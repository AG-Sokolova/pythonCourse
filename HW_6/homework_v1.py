import csv
from func import gen_email, unique_email, read_txt_names


file_patch = 'generated_data'
dict_file_title = {'empty': file_patch + '/empty.csv',
                   'digits': file_patch + '/digits.csv',
                   'names': file_patch + '/names.csv',
                   'emals': file_patch + '/emals.csv',
                   'nne': file_patch + '/nne.csv',
                   'digits_2': file_patch + '/digits_2.csv',
                   'names_2': file_patch + '/names_2.csv',
                   'emals_2': file_patch + '/emals_2.csv',
                   'nne_2.csv': file_patch + '/nne_2.csv'}

list_names = []  # лист сгенерированных имен
list_emals = []  # лист сгенерированных email

# получить уникальный список имен
read_txt_names(list_names)
print('Список имен полученный из txt файла:', len(list_names), list_names)


# 1 - пустой empty.csv файл
with open(dict_file_title['empty'], 'w', newline='') as f_empty_csv:
    # empty
    pass  # or write
f_empty_csv.close()

# 2 - digits.csv файл с 1-м полем, 150 строк [от 0 до 150]
with open(dict_file_title['digits'], 'w', newline='') as f_digits_csv:
    col = ['number']
    write = csv.DictWriter(f_digits_csv, fieldnames=col)
    write.writeheader()
    for i in range(0, 150):
        number = {'number': i}
        write.writerow(number)
f_digits_csv.close()

# 3 - names.csv файл с 1-м полем, 100 строк уникальных имен
with open(dict_file_title['names'], 'w', newline='') as f_names_csv:
    col = ['name']
    write = csv.DictWriter(f_names_csv, fieldnames=col)
    write.writeheader()
    for items, value in enumerate(list_names):  # дописать
        if items < 100:
            name = {'name': value}
            write.writerow(name)
f_names_csv.close()


# 4 - emals.csv файл с 1-м полем, 100 строк уникальных email [...@gmail.com]
with open(dict_file_title['emals'], 'w', newline='') as f_emails_csv:
    col = ['email']
    write = csv.DictWriter(f_emails_csv, fieldnames=col)
    write.writeheader()

    for items, value in enumerate(list_names):
        if items < 100:  # ограничение добавляемых строк
            email = unique_email(gen_email(value), list_emals)
            write.writerow({'email': email})
f_emails_csv.close()


# 5 -  nne.csv файл с 3-мя полями(Number, Name, Email ), 100 строк
list_emals.clear()  # очистить список emails

with open(dict_file_title['nne'], 'w', newline='') as f_nne_csv:
    cols = ['number', 'name', 'email']
    write = csv.DictWriter(f_nne_csv, fieldnames=cols)
    write.writeheader()

    for item, value in enumerate(list_names):
        if item < 100:
            mail = email = unique_email(gen_email(value), list_emals)
            user = {'number': item,
                    'name': value,
                    'email': mail}
            write.writerow(user)
f_nne_csv.close()
