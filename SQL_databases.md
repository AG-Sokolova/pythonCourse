# PostgreSQL в Python
[Как подружить Python и базы данных SQL. Подробное руководство](https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27)

  

**Psycopg2** - это адаптер для PostgreSQL, который просто реализует протокол для обмена с СУБД. 

Установить модуль psycopg2 для PostgreSQL для взаимодействия с базой данных , с помощью команды`pip install psycopg2`

Определим функцию для подключения к базе данных:

```python
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to DB successful")
    except OperationalError as e:
        print(f"The error '{e}' ")
    return connection
```

Подключение осуществляется через интерфейс `psycopg2.connect()`.



Для выполнения запросов используется метод  cursor:

```python
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
```

Эту функцию можно использовать для организации таблиц, вставки, изменения и удаления записей в базе двнных. 

Далее создаем переменную в которой пишем SQL запрос и ниже вызываем функцию выполнения запроса.

**Создаем таблицу:**

```
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id SERIAL PRIMARY KEY, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER REFERENCES users(id)
)
"""

execute_query(connection, create_posts_table)
```

**Вставка записей:**

```python
posts = [
    ("Happy", "I am feeling very happy today", 'James'),
    ("Hot Weather", "The weather is very hot today", 'Leila'),
    ("Help", "I need some help with my work", 'Leila'),
    ("Great News", "I am getting married", 'James'),
    ("Interesting Game", "It was a fantastic game of tennis", 'Elizabeth'),
    ("Party", "Anyone up for a late-night party today?", 'Brigitte'),
]

post_records = ", ".join(["%s"] * len(posts))

insert_query = (
    f"INSERT INTO posts (title, description, user_id) VALUES {post_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, posts)
```

**Извлечение данных из записей:**

```python
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

select_posts = "SELECT * FROM posts"
posts = execute_read_query(connection, select_posts)

for i in posts:
    print(i)
```

#### Пример

- [lesson_db25](https://github.com/AG-Sokolova/pythonCourse/blob/lecture/lesson_5/lesson_db25.py)
- [lesson_students](https://github.com/AG-Sokolova/pythonCourse/blob/lecture/lesson_5/lesson_students.py)
