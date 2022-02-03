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
    print()