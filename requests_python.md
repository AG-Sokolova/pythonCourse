# Requests в Python

[Requests в Python – Примеры выполнения HTTP запросов](https://python-scripts.com/requests)

[Использование модуля Requests в Python](https://code.tutsplus.com/ru/tutorials/using-the-requests-module-in-python--cms-28204)

[Библиотека Requests](https://smartiqa.ru/blog/python-requests)



**Rrequests** - это модуль Python, который можно использовать для отправки всех видов HTTP-запросов.

Что бы уставновить модуль, необходимо в командной строке ввести команду `pip install requests`

После установки модуля можно проверит, установлен ли модуль успешно, импортировав его с помощью команды `import requests`

#### Метод OPTIONS 

С помощью данного метода можно увидеть принимаемые ресурсом или конкретным  его разделом HTTP-запросы (просмотр опций включен не у всех ресурсов). 

```python
>>> response = requests.options('https://httpbin.org/')
>>> response.headers['Access-Control-Allow-Methods']
GET, POST, PUT, DELETE, PATCH, OPTIONS
```

В данном примере на сайте имеется возможность протестировать практически все виды HTTP-запросов. 

#### Метод GET

У GET-запросов могут присутствовать параметры, которыми легко управлять. 

```python
>>> get_params = {'page': 11, 'product': 'car'}
>>> response = requests.get('https://httpbin.org/', params=get_params)
>>> response.url
'https://httpbin.org/?page=11&product=car'
```

#### Метод POST

Для отправки данных (например, форм) применяют метод POST библиотеки Requests. В аргументе data указываются все требуемые поля. Ответом будет json-объект с переданными данными, а также ряд иных сведений (заголовки, ip-адрес, ссылка). 

```python
>>> post_params = {'user': 'admin', 'password': 'admin_pass1'}
>>> response = requests.post('https://httpbin.org/post', data=post_params)
>>> response.json()['form']
{'password': 'admin_pass1', 'user': 'admin'}
```

#### Метод HEAD 

Аналогичен запросу GET по своей сути, но может служить предварительным тестом ресурса, с которого планируется скачивать файл большого размера. Если заголовки получены,  то все хорошо и можно приступать к загрузке. 

```python
>>> response = requests.head('https://httpbin.org/')
>>> response.headers
{'Date': 'Sat, 06 Mar 2021 11:40:49 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '9593', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
```

#### Метод PUT

Представленный метод является идемпотентным. Это значит, что повторная  отправка идентичных данных никак не повлияет на работу ресурса. Если  использовать метод POST, то возможны ошибки. 

```python
>>> put_params = {'user': 'admin', 'password': 'admin_pass1'}
>>> response = requests.put('https://httpbin.org/put', data=put_params)
>>> response.status_code
200
```

#### Метод PATCH 

Предполагает частичное обновление данных на сервере. 

```python
>>> patch_params = {'user': 'new_admin', 'password': 'new_pass'}
>>> response = requests.patch('https://httpbin.org/patch', data=patch_params)
>>> response.status_code
200
```

Чаще всего применяется для изменения содержимого конфигурационных файлов (например, вы поменяли токен для доступа к API).

#### Метод DELETE 

Когда требуется удаление некоего ресурса. 

```python
>>> del_params = {"name": "Николай", "job": "Повар"}
>>> response = requests.delete('https://httpbin.org/delete', data=del_params)
>>> response.json()['form']
{'job': 'Повар', 'name': 'Николай'}
```

#### Отправка файлов cookie и заголовков

Чтобы добавить HTTP-заголовки в запрос, необходимо просто передать их в dict для параметра headers. Аналогично,  также можно отправлять собственные файлы cookie на сервер, используя dict, переданный в параметр cookie.

```python
>>> url = 'http://some-domain.com/set/cookies/headers'
>>> headers = {'user-agent': 'your-own-user-agent/0.0.1'}
>>> cookies = {'visit-month': 'February'}
>>> response = requests.get(url, headers=headers, cookies=cookies)
```

Cookies также может быть передано в Cookie Jar. Они предоставляют более  полный интерфейс, позволяющий использовать эти файлы cookie на  нескольких путях.

#### Пример:

- [lesson_9](https://github.com/AG-Sokolova/pythonCourse/blob/lecture/lesson_9.py)
