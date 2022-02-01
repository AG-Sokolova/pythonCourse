# import valid_u
#
#
# def update_user_info(email, users_emails, users_storage, update_data):
#     if valid_u.unique_email(email, users_emails):  # уникальность email
#         users_storage[email].update(update_data)
#         print(f'Изменение данных прошло успешно. {users_storage[email]}')
#     else:
#         print(f'Такого email {email} не существует')
#
#
# def update_user_email(email, users_emails, users_storage, update_data):
#     if valid_u.unique_email(email, users_emails):  # уникальность email
#         for item, value in enumerate(users_emails):
#             if value == email:
#                 users_emails[item] = update_data[email]
#         users_storage[update_data[email]] = users_storage.pop(email)
#         print(f'Email {email} изменен успешно на {update_data[email]}')


