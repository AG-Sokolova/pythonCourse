from copy import deepcopy


# 9
def plit_list(array, size):
    bol = True
    copy_array = deepcopy(array)
    new_array = []

    while bol:
        if len(copy_array) % size != 0:
            copy_array.append('none')
        else:
            bol = False

    while len(copy_array) > size:
        size_items = copy_array[:size]
        new_array.append(size_items)
        copy_array = copy_array[size:]
    new_array.append(copy_array)

    return new_array


# 10
def lists_even_odd(array):
    new_arr_even = []
    new_arr_odd = []

    for items in array:
        if items % 2 == 0:
            new_arr_even.append(items)
        elif items % 2 != 0:
            new_arr_odd.append(items)
    return new_arr_even, new_arr_odd


# 13
def list_100(array):
    list_less_100 = []  # => меньше 100
    list_more_100 = []  # => больше или равно 100

    count_less = 0
    count_more = 0

    for i in array:
        for j in i:
            if j >= 100:
                list_more_100.append(j)
                count_more += j
            else:
                list_less_100.append(j)
                count_less += j

    if len(list_more_100) == 0:
        list_more_100.append('No lists')
        count_more = 'No lists'
    if len(list_less_100) == 0:
        list_less_100.append('No lists')
        count_less = 'No lists'

    return list_less_100, list_more_100, count_less, count_more

# 16
