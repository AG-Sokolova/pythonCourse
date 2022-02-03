import csv
from csv import writer

file_path = 'file/'
csv_file_title = 'csv_1.csv'

file_title = file_path + csv_file_title

users_list = [['Maksim', 30],
              ['Artem', 32],
              ['Alexey', 35]
              ]

users_dict = [{'name': 'Maksim', 'age': 31},
              {'name': 'Artem', 'age': 32},
              {'name': 'Alexey', 'age': 35}
              ]

# with open(file_title, 'w', newline='') as csv_f:
#     writer = writer(csv_f)
#     row = ['Elena', 20]
#     row_2 = ['Anna', 23]
#     writer.writerow(row)
#     writer.writerow(row_2)

# with open(file_title, 'w', newline='') as csv_f:
#     writer = csv.writer(csv_f)
#     writer.writerows(users_list)

# with open(file_title, 'r', newline='') as csv_f:
#     reader = csv.reader(csv_f)
#     # print(*reader)
#
#     for i in reader:
#         print(i[0])

# with open(file_title, 'w', newline='') as csv_f:
#     col = ['name', 'age']
#     write = csv.DictWriter(csv_f, fieldnames=col)
#     write.writeheader()
#     write.writerows(users_dict)

# with open(file_title, 'a', newline='') as csv_f:
#     col = ['name', 'age']
#     write = csv.DictWriter(csv_f, fieldnames=col)
#     user = {'name': 'Natasha', 'age': 10}
#     write.writerow(user)

with open(file_title, 'r', newline='') as csv_f:
    reader = csv.DictReader(csv_f)
    line_count = 0
    for i in reader:
        print(line_count, i['name'], i['age'])
        line_count += 1
