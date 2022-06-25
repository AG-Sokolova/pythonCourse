# 1
reg_year_days = 365  # => integer
leap_year_days = 366  # => integer
real_year_days = 365.25  # => float
is_leap_year = True  # => boolean
reg = "Regular year"  # => string
leap = "Leap year"  # => string

# 2
year_2021 = (2021, False, reg_year_days)
year_2022 = (2022, False, reg_year_days)
year_2023 = (2023, False, reg_year_days)
year_2024 = (2024, is_leap_year, leap_year_days)

# 3
# кортеж изменять нельзя, можно перезаписать заново
# list_year_2022 = list(year_2022)
# list_year_2024 = list(year_2024)
# list_year_2022[1], list_year_2022[2] = list_year_2024[1], list_year_2024[2]

# 4
list_years = [year_2021, year_2022, year_2023, year_2024]

# 5
print('=== task_5')
for items in list_years:
    year = items[0]  # => год
    days = items[2]  # => количество дней в году
    if year % 4 == 0:
        print(str(year) + ' is leap year and has '.upper() + str(days) + ' days '.upper())
    else:
        print(year, 'is regular year and has'.lower(), days, 'days'.lower())

# 6
print('=== task_6')
add_year_2025 = (2025, False, reg_year_days)
list_years.append(add_year_2025)

print(f'в листе years {len(list_years)} элементов')

# 7
print('=== task_7')
for items in list_years:
    year = items[0]  # => год
    days = items[2]  # => количество дней в году
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'{year} IS {leap.upper()} AND HAS {days} DAYS')
    else:
        print('{} is {} and has {} days'.format(year, reg.lower(), days))


# 8
print('=== task_8')
dict_years = {}

for i in range(2020, 2031):
    if i % 4 == 0:
        dict_years.setdefault(i, leap_year_days)   # => добавить в словарь високосные года
    else:
        dict_years.setdefault(i, reg_year_days)   # => добавить в словарь не високосные года

print("словарь с годами:", dict_years)

# 9
print('=== task_9')
for key, value in dict_years.items():
    if key % 4 != 0:
        print(f'Не високосный год {key}, так как количество дней {value}')