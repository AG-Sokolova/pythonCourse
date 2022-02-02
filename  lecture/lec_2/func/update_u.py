def update_user_info(email, update_key, update_val, users_storage):
    update_data = {update_key: update_val}
    users_storage[email].update(update_data)
    print('' + f'The data change was successful. Info: {users_storage[email]}' + '')


def update_user_email(email, update_val, users_emails, users_storage):

    for item, value in enumerate(users_emails):
        if value == email:
            users_emails[item] = update_val

    users_storage[update_val] = users_storage.pop(email)
    print('' + f'Email {email} successfully changed to {update_val}' + '')




