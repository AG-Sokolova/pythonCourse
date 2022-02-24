import psycopg2

conn = psycopg2.connect(dbname='qa_students_1',
                        user='qa_student_1_u_1',
                        password='123',
                        host='159.69.151.133',
                        port='5056')

cursor = conn.cursor()

if conn:
    print('connected ----!')
    select_query = 'select * from students;'
    sql_select = '''select * from students;'''

    # cursor.execute(select_query)
    # print(cursor.description[1][0])  # -> name

    exeq_query = cursor.execute(select_query)
    f_query = cursor.fetchall()
    # print(f_query)

    # for i in f_query:
    #     print(i)  # получает все данные из таблицы students

    for i in f_query:
        u_name = 'Name = ' + i[1]
        u_email = 'Email = ' + i[2]
        u_reg_time = 'Registration_time = ' + str(i[4])
        print(u_name, u_email, u_reg_time)

    conn.commit()
    conn.close()
