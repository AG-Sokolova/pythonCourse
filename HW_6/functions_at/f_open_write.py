import csv
from additionally import gen_email


# создает пустой файл
def empty_file(file_title):
    with open(file_title, 'w', newline='') as empty:
        # empty
        pass  # or write
    empty.close()


# создает в csv файл целые числа [от from_num до to_num]
def add_int_numb_csv(file_title, from_num, to_num):
    with open(file_title, 'w', newline='') as digits_csv:
        col = ['number']
        write = csv.DictWriter(digits_csv, fieldnames=col)
        write.writeheader()
        for i in range(from_num, to_num):
            num = {'number': i}
            write.writerow(num)
    digits_csv.close()


# создает в csv файл имен, полученных из списка имен (можно ограничить количество добавленных строк num_lines)
def add_names_csv(file_title, num_lines, list_names):
    with open(file_title, 'w', newline='') as names_csv:
        col = ['name']
        write = csv.DictWriter(names_csv, fieldnames=col)
        write.writeheader()
        for items, value in enumerate(list_names):  # дописать
            if items < num_lines:
                write.writerow({'name': value})
    names_csv.close()


# # создает в csv файл c рандомными именами email (можно ограничить количество добавленных строк num_lines)
# def add_rnd_name_emails_csv(file_title, num_lines, name_length=8):
#     with open(file_title, 'w', newline='') as email_csv:
#         col = ['email']
#         write = csv.DictWriter(email_csv, fieldnames=col)
#         write.writeheader()
#         i = 0
#         while i < num_lines:
#             mail = {'email': f'{rnd_name_mail(name_length)}@gmail.com'}
#             write.writerow(mail)
#             i += 1
#     email_csv.close()


# def add_emails_csv(file_title, list_name):
#     with open(file_title, 'w', newline=''):
#         col = ['email']


def add_emails_csv(file_title, num_lines, list_names, i=0):
    with open(file_title, 'w', newline='') as email_csv:
        col = ['email']
        write = csv.DictWriter(email_csv, fieldnames=col)
        write.writeheader()

        for items, value in enumerate(list_names):
            if items < num_lines:
                mail = gen_email(value)
                write.writerow({'email': mail})
    email_csv.close()
