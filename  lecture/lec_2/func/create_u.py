def create_user(email, name, password, phone, users_emails, users_storage):

    user_info = [email, name, password, phone]
    print('\033[32m'+f'User is successfully created - {user_info}'+'\033[0m')

    users_emails.append(email)
    users_storage[email] = {
        'name': name,
        'password': password,
        'phone': phone
    }
    return user_info, users_emails, users_storage
