# получает из txt файла данные и записывает в новый лист
def get_file_txt(title_file, new_list):
    with open(title_file, 'r') as get_txt:
        lines = get_txt.read().splitlines()
        for line in lines:
            new_list.append(line)
    get_txt.close()
