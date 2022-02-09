import random


# из строки "Name Lastname" получает email "n.lastname@gmail.com
def gen_email(user):
    name, last_name = "", ""
    full_name = user.split()

    for item, value in enumerate(full_name):
        if item == 0:
            name = value[0]
        elif item == 1:
            last_name = value
    email_name = f'{name}.{last_name}@gmail.com'
    return email_name.lower()


# рандомное имя email
def rnd_name_mail(length):
    letters = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


#  проверка что еще нет такого email в списке
def unique_email(mail, list_mail):
    while True:
        if mail in list_mail:  # проверка что такой email еще нет
            mail = f'{rnd_name_mail(8)}@gmail.com'  # если есть, то генерируем новый => [текст@gmail.com]
        else:
            list_mail.append(mail)
            break
    return mail


# из txt файла получает в переменную list_names уникальные имена
def read_txt_names(list_names):
    # из txt файла получает в переменную list_names имена и фамилии
    with open('initial_names.txt', 'r') as get_names:
        lines = get_names.read().splitlines()
        for line in lines:
            if line not in list_names:
                list_names.append(line)
    get_names.close()
    return list_names

