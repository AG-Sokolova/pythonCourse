import json
import requests


# / --> Hello
url = 'http://162.55.220.72:5005'

resp_hellow = requests.get(url)
print('response =', resp_hellow, ', status_code =', resp_hellow.status_code, ', body =', resp_hellow.text)

resp_hellow_headers = resp_hellow.headers
print('headers =', resp_hellow_headers)

for key, value in resp_hellow_headers.items():
    print('------ key =', key, ', value =', value)

print('-------------------')

# / ---> first
end_point_1 = '/first'
resp_first = requests.get(url + end_point_1)
print('url =', url + end_point_1, 'response = ', resp_first.text)


# / ---> get_method
end_point_2 = '/get_method'
get_method_params = {'name': 'Nata',
                     'age': 18}
resp_get_method = requests.get(url + end_point_2, params=get_method_params)

resp_get_method_text = resp_get_method.text
resp_get_method_json = resp_get_method.json()

print('url =', url + end_point_2, 'response_text =', resp_get_method_text, type(resp_get_method_text))
print('url =', url + end_point_2, 'response_json =', resp_get_method_json, type(resp_get_method_json))


# / ---> user_info_1
end_point_3 = '/user_info_1'
user_info1_data = {'name': 'Alex',
                   'age': 34,
                   'weight': 90}

resp_user_info1 = requests.post(url + end_point_3, data=user_info1_data)
resp_user_info1_json = resp_user_info1.json()
print('url =', url + end_point_2, 'response =', resp_user_info1_json)


# / ---> login
end_point_login = '/login'
login_data = {'login': 'Alexey',
              'password': '123'}
user_token = requests.post(url + end_point_login).json()['token']


# / ---> user_info
end_point_4 = '/user_info'

user_info_data = {'name': 'Alexey',
                  'age': 56,
                  'salary': 30000,
                  'auth_token': user_token}
json_data = json.dumps(user_info_data)

req_headers = {'Content-type': 'application/json'}

resp_user_info = requests.post(url + end_point_4, data=json_data, headers=req_headers).json()

print('url =', url + end_point_4, 'response =')
for key, value in resp_user_info.items():
    print('key =', key)
    print('value =', value)
    print('----------------')

