from operator import itemgetter
import string

def read_file():
    with open('text.txt', 'r', encoding="utf-8") as f:
        text = f.read()
    f.close()
    return text

def get_sing():
    text = read_file().lower()
    invalid_sing = []
    valid_characters = string.ascii_lowercase + 'яюэьыъщшчцхфутсрпонмлкйизжёедгвба' + ' ' + '-'
    for symbol in text:
        if (symbol not in valid_characters) and (symbol not in invalid_sing):
            invalid_sing.append(symbol)
    return invalid_sing

def split_text():
    text = read_file().lower()
    not_sing = get_sing()

    for sing in not_sing:
        text = text.replace(sing, ' ')
    array_words = text.split()
    return array_words

# def split_text():
#     text = read_file().lower()
#     for sing in string.punctuation:
#         if sing in text:
#             text = text.replace(sing, '')
#     array_words = text.split()
#     return array_words

def amount_word():
    array_words = split_text()
    dict_words = {}

    for word in array_words:
        if dict_words.get(word, None):
            dict_words[word] += 1  # если в словаре ключ есть, то увеличиваем значение на 1
        else:
            dict_words[word] = 1  # если ключа нет, то создаем его со значением 1
    return dict_words

def is_sort_amount(sort_type=False):
    dict_words = amount_word()
    sorted_amount = sorted(dict_words.items(), key=itemgetter(1), reverse=sort_type)  # => list
    sorted_amount = {k: v for k, v in sorted_amount}  # => dict
    # sorted_amount = dict(sorted(dict_words.items(), key=itemgetter(1), reverse=sort_type))  # => dict (устаревшее)
    return sorted_amount


print(f'В вашем тексте самое популярное слово «{max(amount_word(), key=amount_word().get)}»')
print('Сортировка по количеству:', is_sort_amount())
print('Количество подсчитанных слов -', len(split_text()), ',без повторений -', len(amount_word().keys()))