import re


def valid_mail(email):
    pattern_mail = r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$'
    if re.match(pattern_mail, email) is not None:
        return True
    else:
        return False


def unique_email(email, users_emails):
    if email in users_emails:
        bol = True
    else:
        print(f'This mail {email} already exists!')
        bol = False
    return bol


def valid_data(**kwargs):

    pattern_phone = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    pattern_name = r'^[a-zA-Z]'

    for key, value in kwargs.items():
        match key:
            case 'email':
                bol = valid_mail(value)
            case 'phone':
                bol = True if re.match(pattern_phone, value) is not None else False
            case 'name':
                bol = True if re.match(pattern_name, value) is not None else False
            case _:
                bol = False

        if not bol:
            print(f'Inviled {key}')
    return bol




