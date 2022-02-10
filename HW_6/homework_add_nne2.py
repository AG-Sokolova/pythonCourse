import pandas
from func import random_date


list_date = []  # список дат

# даты по годам, 50 строк[рандомно: 1980 - 1990]
random_date(50, 1980, 1990, list_date)

# даты по годам, 100 строк[рандомно: 1991 - 2000]
random_date(100, 1991, 2000, list_date)

# даты по годам, 150 строк[рандомно: 2001 - 2010]
random_date(150, 2001, 2010, list_date)

# даты по годам, 150 строк[рандомно: 2011 - 2021]
random_date(150, 2011, 2021, list_date)


# добавить в файл nne_2.csv столбец Date
df = pandas.read_csv('generated_data/nne_2.csv')
df['date'] = list_date
df.to_csv(r"generated_data/nne_2.csv", index=False)

