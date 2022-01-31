def create_user(email, name, password, phone, users_emails, users_storage):

    user_info = [email, name, password, phone]

    users_emails.append(email)
    users_storage[email] = {
        'name': name,
        'password': password,
        'phone': phone
    }
    return f'create_user: {user_info}'
