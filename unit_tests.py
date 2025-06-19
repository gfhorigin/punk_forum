import requests

# 1. Регистрация через JSON
reg = requests.post(
    'http://127.0.0.1:8000/registration',
    params={'email': 'neww', 'password': 'wrong'}
)
print("Registration:", reg.json())

# 2. Логин через JSON
login = requests.post(
    'http://127.0.0.1:8000/login',
    json={'email': 'neww', 'password': 'wrong'}
)
print("\nLogin Status:", login.status_code)
print("Login Response:", login.json())
print("Login Cookies:", login.cookies.get_dict())

# 3. Проверка авторизации (только если логин успешен)
if login.status_code == 200:
    auth_check = requests.get(
        'http://127.0.0.1:8000/check-auth',
        cookies=login.cookies
    )
    print("\nAuth Check:", auth_check.json())
# import requests
# req = requests.get('http://127.0.0.1:8000')
# print(req)
# req = requests.post('http://127.0.0.1:8000/login',
#                     json={'email': 'admin', 'password': 'admin'}
# )
# print(req.json())
# req = requests.post('http://127.0.0.1:8000/login',
#                     params={'email': 'admin', 'password': 'wrong'}
# )
# print(req.json())
# req = requests.post('http://127.0.0.1:8000/registration',
#                     params={'email': 'admin', 'password': 'wrong'}
# )
# print(req.json())
# req = requests.post('http://127.0.0.1:8000/registration',
#                     params={'email': 'neww', 'password': 'wrong'}
# )
# print(req.json())
# req = requests.post('http://127.0.0.1:8000/login',
#                     json={'email': 'neww', 'password': 'wrong'}
# )
# cookie = req.cookies
# print(req.json(), "final login")
# print(cookie.get_dict())
# req = requests.get('http://127.0.0.1:8000/check-auth', cookies=cookie)
# print(req)