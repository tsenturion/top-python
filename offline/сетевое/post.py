import requests

"""url = 'https://httpbin.org/post'
data = {'username': "alice", 'password': 'secret'}
# username=alice&password=secret - application/x-www-form-urlencoded
response = requests.post(url, data=data)
print(response.text)

json_data = {'username': "alice", 'password': 'secret'}

response = requests.post(url, json=json_data)
print(response.json())
#application/json

data = {'key': 'value'}
headers = {'Content-Type': 'application/json', 'Authorization': 'token'}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
try:
    response = requests.post(url, json=data, timeout=5)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(e)"""
"""url = 'https://httpbin.org/post'
files = {'file': open('example.txt', 'rb')}
#multipart/form-data
response = requests.post(url, files=files)
print(response.text)"""

"""
payload = {"q": 'python', 'sort': 'stars'}
response = requests.get(url="https://api.github.com/search/repositories", params=payload)
"""
"""
rest - архитектура, опирается на http методы
get
post
put - полностью обновить объект
patch - частично обновить
delete -удалить

пример
POST /api/users HTTP/1.1
Host example.com
Content-Type: application/json

{
    'name': 'ivan',
    'email': 'ivan@example.com'
}
"""
"""url = 'https://example.com/api/users'
user = {
    'name': 'ivan',
    'email': 'ivan@example.com'
}

response = requests.post(url, json=user)
print(response.status_code)"""
#201 Created
#200 OK
#400 Bad Request
#401 Unauthorized/403 Forbidden нет доступа
#500 Internal Server Error


"""
data= (посмотреть form headers )
json= (Content-Type)
передача заголовков
с обработкой ответа от сервера 
https://reqres.in
"""

url = 'https://httpbin.org/post'
data = {
    'username': "alice",
    'password': 'secret'
}

"""resposne = requests.post(url, data=data)

print(resposne.status_code)
print(resposne.json())"""

user = {
    'username': 'alice123',
    'email': 'alice@example.com',
    'is_active': True
}

"""resposne = requests.post(url, json=user)
print(resposne.status_code)
print(resposne.json()['json'])
print(resposne.json())"""

payload = {'task': 'POST headers'}
headers = {
    'Authorization': '12345',
    'Custom-Header': 'CustomValue'
}

"""response = requests.post(url, json=payload, headers=headers)

print(response.json()['headers'])"""

"""url = 'https://reqres.in/api/register'
data = {
    'email': 'evo.holt@reqres.in',
    'password': 'pistol'
}
headers = {
    'x-api-key': 'reqres-free-v1'
}
response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())
"""
"""
.post()
data= - отправка формы
data = {
    'email': 'evo.holt@reqres.in',
    'password': 'pistol'
}
resposne = requests.post(url, data=data)

json=
json_data = {'username': "alice", 'password': 'secret'}
response = requests.post(url, json=data)

headers= - кастомные заголовки
Authorization - токен авторизации
User-Agent - описание клиента
Content-Type - тип тела запроса
headers = {
    'x-api-key': 'reqres-free-v1'
}
response = requests.post(url, json=data, headers=headers)

files=
files = {'file': open('example.txt', 'rb')}
response = requests.post(url, files=files)
multipart/form-data

params= - если нужен url с параметрами
timeout= - защита от зависания
response.status_code 
response.json()
response.text
try:
    response.raise_for_status()
except

idempotency 
"""