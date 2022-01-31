import re


def valid_mail(email):
    pattern = r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$'
    if re.match(pattern, email) is not None:
        return True
    else:
        return False


def valid_phone(phone):
    pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    if re.match(pattern, phone) is not None:
        return True
    else:
        return False


def valid_name(name):
    pattern = r'^([а-яё]+|[a-z]+)$'
    if re.match(pattern, name) is not None:
        return True
    else:
        return False
