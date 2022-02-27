from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test_method_get', methods=['GET'])
def test_method_get():
    parm_1 = int(request.args.get('salary'))
    parm_2 = request.args.get('name')

    resp = {'name': parm_2,
            'salary': parm_1,
            'salary_4years': parm_1 * 5}
    return jsonify(resp)

@app.route('/test_method_post', methods=['POST'])
def test_method_post():
    parm_1 = int(request.form.get('salary'))
    parm_2 = request.form.get('name')
    parm_3 = request.form.get('age')

    parm_4 = request.args.get('salary')

    resp = {'name': parm_2,
            'salary': parm_1,
            'age': parm_3,
            'salary_4years': parm_1 * 5,
            'url_salary': parm_4}
    return jsonify(resp)

@app.route('/test_method_yo', methods=['YOLOCHKA', 'POST'])
def test_method_yo():
    if request.method == 'POST':
        parm_1 = int(request.form.get('salary'))
        parm_2 = request.form.get('name')
        resp = {'name': parm_2,
                'salary': parm_1}
        return jsonify(resp), 200
    elif request.method == 'YOLOCHKA':
        return 'Method Yolochka', 500


# lesson_7 подключение к postgreSQL
conn = psycopg2.connect(dbname='qa_ddl_25_63',
                        user='user_25_63',
                        password='123',
                        host='159.69.151.133',
                        port='5056')

@app.route('/select_bd', methods=['GET'])
def select_bd():
    cursor = conn.cursor()
    select_query = 'SELECT * FROM users_python;'
    cursor.execute(select_query)
    data_bd = cursor.fetchall()

    result_json = {}

    for i in data_bd:
        profile_info = {}
        profile_info['name'] = i[1]
        profile_info['email'] = i[2]
        profile_info['phone'] = i[3]
        profile_info['country'] = i[4]
        profile_info['city'] = i[5]
        profile_info['salary'] = i[6]

        result_json[str(i[0])] = profile_info

    return jsonify(result_json)

@app.route('/add_bd', methods=['POST'])
def add_bd():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    country = request.form.get('country')
    city = request.form.get('city')
    salary = request.form.get('salary')

    insert_query = f''' 
            insert into public.users_python(name, email, phone, country, city, salary)
            values ('{name}','{email}','{phone}','{country}','{city}','{salary}');
            '''

    cursor = conn.cursor()
    cursor.execute(insert_query)
    conn.commit()
    return 'ok'
