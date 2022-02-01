def create_user(email, name, password, phone, users_emails, users_storage):

    user_info = [email, name, password, phone]
    print(f'create_user: {user_info}')

    users_emails.append(email)
    users_storage[email] = {
        'name': name,
        'password': password,
        'phone': phone
    }
    return user_info, users_emails, users_storage
