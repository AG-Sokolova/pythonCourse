import string

def alphabet_position(text):
    alphabet_uppercase = [i for i in string.ascii_uppercase]
    alphabet_lowercase = [i for i in string.ascii_lowercase]
    list_position = []

    for p in string.punctuation + ' ':
        if p in text:
            text = text.replace(p, '')
    text = list(text)

    for letter in text:
        if letter in alphabet_uppercase:
            list_position.append(str(alphabet_uppercase.index(letter) + 1))
        elif letter in alphabet_lowercase:
            list_position.append(str(alphabet_lowercase.index(letter) + 1))
    return ' '.join(list_position)


test = alphabet_position("The sunset sets at twelve o' clock.")
print(test)