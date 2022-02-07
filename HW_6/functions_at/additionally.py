import random


# генерирует рандомно имя email
def rnd_name_mail(length):
    letters = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


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
