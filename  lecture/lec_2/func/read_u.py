def user_info(email, users_emails, users_storage):
    if email in users_emails:
        massage = f'User_email: {email} \n User_info: {users_storage[email]}'
    else:
        massage = f'New user with email {email}'
    print(massage)


def all_users_info(users_storage):
    count = 0
    for key, value in users_storage.items():
        count += 1
        print(f'{count}. User email: {key} \n   User_info: {value}')

