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
            valid_data = valid_u.valid_data(email=email, name=name, phone=phone)
            # if valid_data:
            #     unique_email = unique_email(email, users_emails)
            #     if unique_email:
            create_u.create_user(email, name, password, phone, users_emails, users_storage)

        case 'read':
            read_email = input('Enter email user or all: ')
            if read_email == 'all':  # все юзеры
                read_u.all_users_info(users_storage)
            elif valid_u.valid_mail(read_email):  # проверка ввода корректного email
                read_u.user_info(read_email, users_emails, users_storage)
            else:
                print("Invalid email.")

        case 'delete':
            delete_email = input('Enter email user: ')
            if valid_u.valid_mail(delete_email):  # проверка ввода корректного email
                delete_u.delete_user(delete_email, users_emails, users_storage)
            else:
                print("Invalid email.")

        case 'update':
            print('action =', action)

            update_email = input('Enter email user: ')
            update_key = input('Enter key [email, name, password, phone]: ').lower()
            update_val = input('Enter update data: ')
            update_data = {update_key: update_val}

            if valid_u.valid_data(update_data):
                if update_key == 'email':
                    update_u.update_user_email(update_email, users_emails, users_storage, update_data)
                else:
                    update_u.update_user_info(update_email, users_emails, users_storage, update_data)

        case 'help':
            help.help_command()

        case 'stop':
            break

        case _:
            print('Please, enter [create, update, delete, read]. Enter [help] if you need help.')
