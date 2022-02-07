from functions_at import f_open_read, f_open_write


list_names = []  # лист сгенерированных имен

file_patch = 'generated_data'
dict_file_title = {'empty': file_patch + '/empty.csv',
                   'digits': file_patch + '/digits.csv',
                   'names': file_patch + '/names.csv',
                   'emals': file_patch + '/emals.csv',
                   'nne': file_patch + '/nne.csv',
                   'digits_2': file_patch + '/digits_2.csv',
                   'names_2': file_patch + '/names_2.csv',
                   'emals_2': file_patch + '/emals_2.csv',
                   'nne_2.csv': file_patch + '/nne_2.csv'}

# 1
f_open_write.empty_file(dict_file_title['empty'])

# 2
f_open_write.add_int_numb_csv(dict_file_title['digits'], 0, 150)

# 3
f_open_read.get_file_txt('initial_data/initial_names.txt', list_names)
print('list_names =', list_names)
f_open_write.add_names_csv(dict_file_title['names'], 100, list_names)

# 4
f_open_write.add_emails_csv(dict_file_title['emals'], 100, list_names)
