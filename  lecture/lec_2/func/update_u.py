def update_user_info(email, update_key, update_val, users_storage, users_emails):
    update_data = {update_key: update_val}
    users_storage[email].update(update_data)
    print('\033[32m' + f'The data change was successful. Info: {users_storage[email]}' + '\033[0m')


def update_user_email(email, update_val, users_emails, users_storage):
    if update_val in users_emails:
        print('\033[31m' + f'The user {update_val} exists' + '\033[0m')
    else:
        for item, value in enumerate(users_emails):
            if value == email:
                users_emails[item] = update_val

        users_storage[update_val] = users_storage.pop(email)
        print('\033[32m' + f'Email {email} successfully changed to {update_val}' + '\033[0m')

