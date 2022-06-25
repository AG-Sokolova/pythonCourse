import string
from random import randint


# 1
def print_initials(name, surname, middlename):
    print(f'{surname} {name[0]}.{middlename[0]}.'.title())

print_initials('ксеНия','мелНнИкова','ВиталЬевна')  # => Мельникова К.В.



# 2
def split_text(st):
    for sing in string.punctuation:
        if sing in st:
            st = st.replace(sing, '')
    list_word = st.split()
    return list_word

# 3
def middle_character(word):
    if len(word) % 2 != 0 and len(word) > 1:
        middle_character(word[1:-1])
    elif len(word) % 2 == 0 and len(word) > 2:
        middle_character(word[1:-1])
    else:
        print(word)

# 4
def uppercase_index(st):
    list_index = []
    for index, letter in enumerate(st):
        if letter.isupper():
            list_index.append(index)
    return list_index

# 5
def sum_of_digits(num):
    if len(num) == 1:
        return int(num)
    return int(num[0]) + sum_of_digits(num[1:])

# 6
def random_digits(a, b):
    def random_sum_of_digits(num):
        if num == 0:
            return num
        else:
            return num + random_sum_of_digits(num-1)
    return random_sum_of_digits(randint(a, b))

# 8
def info(**kwargs):
    sorted_list = sorted(kwargs.items(), key=lambda k: k[0])
    print(sorted_list)
    for key_value in sorted_list:
        key_value = [str(i) for i in key_value]
        print(' = '.join(key_value))
    return {k: v for k, v in sorted_list}  # сортированный словарь


# 1
# print_initials('Мельникова', 'Ксения', 'Витальевна')  # => Мельникова К.В.

# 2
print(split_text('I love arrays they are my favorite'))  # => ["I", "love", "arrays", "they", "are", "my", "favorite"]

# 3
# middle_character('testing')  # => "t"
# middle_character('middle')  # => "dd"

# 4
# print(uppercase_index('We LoVe PytHoN'))  # => [0, 3, 5, 8, 11, 13]

# 5
# print(sum_of_digits('13'))  # => 4

# 6
# print(random_digits(25, 30))

# # 8
# info(first_name="John",
#      last_name="Doe",
#      age=33,
#      country='Belarus',
#      mobile_phone='Android')