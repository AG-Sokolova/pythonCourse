from func import create_u
from func import read_u
from func import delete_u
from func import update_u
from func import valid_u
from func import help

users_emails = []
users_storage = {}

while True:
    action = input('Enter [create, update, delete, read]: ')
    action = action.lower()  # нижний регистр

    match action:
        case 'create':

            email = input('Enter e-mail: ')
            name = input('Enter name: ')
            password = input('Enter password: ')
            phone = input('Enter phone: ')

            print(create_u.create_user(email, name, password, phone, users_emails, users_storage))

        case 'read':

            read_email = input('Enter email user or all: ')

            if read_email == 'all':  # все юзеры
                print(read_u.all_users_info(users_storage))
            elif valid_u.valid_mail(read_email):  # проверка ввода корректного email
                print(read_u.user_info(read_email, users_emails, users_storage))
            else:
                print("Invalid email.")

        case 'delete':

            delete_email = input('Enter email user: ')

            print(delete_u.delete_user(delete_email, users_emails, users_storage))

        case 'update':
            print('action =', action)

        case 'help':
            print('action =', action)

            help.help_command()

        case 'stop':
            break

        case _:
            print('Please, enter [create, update, delete, read]. Enter [help] if you need help.')
