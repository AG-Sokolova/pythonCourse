def delete_user(email, users_emails, users_storage):
    if email in users_emails:
        del users_storage[email]
        users_emails.remove(email)
        massage = '\033[32m'+f'User {email} - deleted'+'\033[0m'
    else:
        massage = '\033[31m'+f'It is impossible to delete. Email {email} - does not exist.'+'\033[0m'
    print(massage)
