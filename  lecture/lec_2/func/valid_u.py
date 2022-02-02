import re


def valid_mail(email):
    pattern_mail = r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$'
    if re.match(pattern_mail, email) is not None:
        return True
    else:
        return False


def unique_email(email, users_emails):
    if email in users_emails:
        print(f'This mail {email} already exists!')
        bol = False
    else:
        bol = True
    return bol


def valid_data(**kwargs):
    print(kwargs)
    bol = True

    pattern_phone = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    pattern_name = r'^[a-zA-Z]'

    for key, value in kwargs.items():
        match key:
            case 'email':
                bol = valid_mail(value)
            case 'phone':
                if re.match(pattern_phone, value) is None:
                    bol = False
            case 'name':
                if re.match(pattern_name, value) is None:
                    bol = False
            case 'password':
                if len(value) < 4:
                    bol = False
            case _:
                bol = False

        if not bol:
            print(f'Inviled {key}')
    return bol
