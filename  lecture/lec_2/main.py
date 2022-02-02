from func import create_u
from func import read_u
from func import delete_u
from func import update_u
from func import valid_u
from func import help

users_emails = []
users_storage = {}

while True:
    action = input('\033[1m\033[47m\033[30m'+'Enter [create, update, delete, read]: '+'\033[0m').lower()

    match action:
        case 'create':
            email = input('\033[1m'+'Enter e-mail: '+'\033[0m')
            name = input('\033[1m'+'Enter name: '+'\033[0m')
            password = input('\033[1m'+'Enter password: '+'\033[0m')
            phone = input('\033[1m'+'Enter phone: '+'\033[0m')

            if valid_u.valid_data(email=email, name=name, phone=phone, password=password):  # валидация входных данных
                if valid_u.unique_email(email, users_emails):  # проверка на уникальность email
                    create_u.create_user(email, name, password, phone, users_emails, users_storage)  # создание юзера
                else:
                    print('\033[31m' + f'This mail {email} already exists!' + '\033[0m')

        case 'read':
            read_email = input('\033[1m'+'Enter [email user] or [all]: '+'\033[0m')

            if read_email.lower() == 'all':  # все юзеры
                read_u.all_users_info(users_storage)
            elif valid_u.valid_mail(read_email):  # проверка ввода корректного email
                read_u.user_info(read_email, users_emails, users_storage)  # просмотр информации юзера
            else:
                print('\033[31m'+"Invalid email."+'\033[0m')

        case 'delete':
            delete_email = input('\033[1m'+'Enter email user: '+'\033[0m')

            if valid_u.valid_mail(delete_email):  # проверка ввода корректного email
                delete_u.delete_user(delete_email, users_emails, users_storage)  # удаление юзера
            else:
                print('\033[31m'+"Invalid email."+'\033[0m')

        case 'update':
            update_email = input('\033[1m'+'Enter email user: '+'\033[0m')
            update_key = input('\033[1m'+'Enter key [email, name, password, phone]: '+'\033[0m').lower()
            update_val = input('\033[1m'+'Enter update data: '+'\033[0m')

            if valid_u.valid_data(**{update_key: update_val}):   # валидация входных данных
                if not valid_u.unique_email(update_email, users_emails):  # проверка на существование email
                    if update_key == 'email':
                        update_u.update_user_email(update_email, update_val, users_emails, users_storage)
                    else:
                        update_u.update_user_info(update_email, update_key, update_val, users_storage, users_emails)
                else:
                    print('\033[31m' + f'This mail {email} already exists!' + '\033[0m')

        case 'help':
            help.help_command()

        case 'stop':
            break

        case _:
            print('\033[1m\033[31m'+'Please, Enter [create, update, delete, read] '
                                    'or Enter [help] if you need help.'+'\033[0m')
