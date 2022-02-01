def delete_user(email, users_emails, users_storage):
    if email in users_emails:
        del users_storage[email]
        users_emails.remove(email)
        massage = f'Email {email} - deleted'
    else:
        massage = f'It is impossible to delete. Email {email} - does not exist.'
    print(massage)
