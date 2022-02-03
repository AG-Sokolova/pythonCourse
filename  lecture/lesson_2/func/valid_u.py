import re


def valid_mail(email):
    pattern_mail = r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$'
    if re.match(pattern_mail, email) is not None:
        bol = True
    else:
        bol = False
    return bol


def unique_email(email, users_emails):
    if email in users_emails:
        bol = False
    else:
        bol = True
    return bol


def valid_data(bol=True, **kwargs):
    pattern_phone = r"^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$"
    pattern_name = r"^[A-Z]{1}[a-z]+$"

    for key, value in kwargs.items():
        match key:
            case 'email':
                if not valid_mail(value):
                    print('\033[31m'+f'Inviled {key}'+'\033[0m')
                    bol = False
            case 'phone':
                if re.match(pattern_phone, value) is None:
                    print('\033[31m'+f'Inviled {key}'+'\033[0m')
                    bol = False
            case 'name':
                if re.match(pattern_name, value) is None:
                    print('\033[31m'+f'Inviled {key}'+'\033[0m')
                    bol = False
            case 'password':
                if len(str(value)) < 4:
                    print('\033[31m'+f'Inviled {key}, enter more than four symbols'+'\033[0m')
                    bol = False
            case _:
                print('\033[31m'+f'Inviled {key}'+'\033[0m')
                bol = False
    return bol
