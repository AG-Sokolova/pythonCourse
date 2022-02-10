import random
from datetime import datetime, timezone


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


# генерирует даты по годам, row_count строк (рандомно: from_date -  to_date) => [dd-mm-yyyy, hh:mm]
def random_date(row_count, from_date, to_date, list_date):
    current_day_month = datetime.now().strftime("%d-%m")
    current_time = datetime.now().strftime("%H:%M")

    counter = 0
    while counter < row_count:
        current_year = random.randint(from_date, to_date)
        list_date.append(f'{current_day_month}-{current_year}, {current_time}')
        counter += 1
    return list_date


# генерирует номера телефонов, row_count строк [+7 990 990-90-90]
def random_phone(row_count, list_phone):
    counter = 0
    while counter < row_count:
        part_1 = random.randint(900, 999)
        part_2 = random.randint(100, 999)
        part_3 = random.randint(10, 99)
        part_4 = random.randint(10, 99)
        phone = f'+7 {part_1} {part_2}-{part_3}-{part_4}'
        if phone not in list_phone:
            list_phone.append(phone)
            counter += 1
    return list_phone


# генерирует зарплаты, row_count строк
def random_salary(row_count, list_salary):
    counter = 0
    while counter < row_count:
        salary = random.randint(10000, 120000)
        list_salary.append(salary)
        counter += 1
    return list_salary
