a = 'python is good'
b = 'hello all'

def print_phrase(string, letter):
    string = string.replace(' ', '')
    length = len(string)

    i = 0
    while i < length:
        if string[i] == letter:
            print('«Ага! Нашлась»')
            break
        print(f'>>>>>  «Текущая буква: {string[i]}»')
        if i == length - 1:
            print('«Распечатали все буквы»')
        i += 1


print_phrase(a, 'a')
print_phrase(b, 'a')
