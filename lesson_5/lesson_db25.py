import psycopg2
import names
import random

conn = psycopg2.connect(dbname='qa_ddl_25_63',
                        user='user_25_63',
                        password='123',
                        host='159.69.151.133',
                        port='5056')
cursor = conn.cursor()

# if conn:
#     print('Connected ----!')
#     create_table_query = 'create table users_python(' \
#                          'id serial primary key,' \
#                          'name varchar(40),' \
#                          'email varchar(100),' \
#                          'phone varchar(16),' \
#                          'country varchar(40),' \
#                          'city varchar(40),' \
#                          'salary int' \
#                          ')'
#
#     cursor.execute(create_table_query)
#     conn.commit()
#     conn.close()


cities = ['Barnaul', 'Ivanovo', 'Lipetsk', 'Moscow', 'Penza', 'Perm', 'Rostov-on-Don', 'Saratov', 'Samara', 'Petrovsk']

for i in range(0, 10):
    if conn:
        print('Connected ---!')

        name = names.get_first_name(1)
        email = (name + '@gmail.com').lower()
        phone = f'+7{random.randint(900, 999)}{random.randint(100, 999)}{random.randint(10, 99)}{random.randint(10, 99)}'
        country = 'Russia'
        city = cities[random.randint(0, len(cities)-1)]
        salary = random.randrange(1000, 10000, 500)

        insert_query = f''' 
        insert into public.users_python(name, email, phone, country, city, salary)
        values ('{name}','{email}','{phone}','{country}','{city}','{salary}');
        '''
        cursor.execute(insert_query)
conn.commit()
conn.close()
