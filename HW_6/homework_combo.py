import pandas
from func import read_txt_names, unique_email, gen_email, random_date, random_salary, random_phone

list_name = []
list_email = []
list_number = []
list_date = []
list_phone = []
list_salary = []

df_nne = pandas.read_csv('generated_data/nne_2.csv')
print(df_nne)

# получаем список имен из txt файла
read_txt_names(list_name)

# удаляем имена которые уже есть в nne_2
count_row_nne = len(df_nne.index)  # количество строк в nne_2

for i in range(0, count_row_nne):
    str_name = df_nne.at[i, 'name']
    for value in list_name:
        if str_name == value:
            list_name.remove(value)

# генерируем email, для новых имен
for value in list_name:
    mail = email = unique_email(gen_email(value), list_email)

# удаляем строку number
del df_nne['number']

count_row_add = len(list_name)  # количество добавляемых строк
count_row = count_row_nne + count_row_add  # общее количество строк

# генерируем date, для новых имен
random_date(count_row_add, 2000, 2021, list_date)

# генерируем столбец phone
random_phone(count_row, list_phone)

# генерируем столбец salary
random_salary(count_row, list_salary)

# добавляем строки в столбцы (name, email, date)
count = count_row_nne + 1

for i in range(0, count_row_add):
    df_nne.loc[count] = [list_name[i], list_email[i], list_date[i]]
    count += 1

# добавляем столбцы (phone, salary)
df_nne['phone'] = list_phone
df_nne['salary'] = list_salary

# сортировка по столбцу имя в алфавитном порядке
df_nne = df_nne.sort_values(by=['name'])
print(df_nne)
# создаем новый csv файл combo
df_nne.to_csv(r"generated_data/combo.csv", index=False)
