def user_info(email, users_emails, users_storage):
    if email in users_emails:
        massage = f'User_email: {email} \n User_info: {users_storage[email]}'
    else:
        massage = '\033[31m'+f'User does not exist {email}'+'\033[0m'
    print(massage)


def all_users_info(users_storage):
    count = 0
    if len(users_storage) == 0:
        print('\033[34m'+'The list is empty. Add a user with the [create] command.'+'\033[0m')
    else:
        for key, value in users_storage.items():
            count += 1
            print(f'{count}. User email: {key} \n   User_info: {value}')


