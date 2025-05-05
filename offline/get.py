# ?search=python
"""
https://api.github.com/data?type=student&id=123
параметры:
type=student
id=123

200 - успешно
301 запрашиваемый ресурс перенесен на другой адрес
404 не найдена
500 внутренняя ошибка сервера
"""
import requests

"""response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

payload = {"q": 'python', 'sort': 'stars'}
response = requests.get(url="https://api.github.com/search/repositories", params=payload)
print(response.url)"""
#print(response.text)

"""headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get("https://api.github.com", headers=headers)
print(response.request.headers)"""

"""try:
    response = requests.get("https://api.github.com", timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP ошибка {http_err}")
except requests.exceptions.ConnectionError:
    print("ошибка соединения")
except requests.exceptions.Timeout:
    print("время ожидания истекло")
except requests.exceptions.RequestException as err:
    print(f"другая ошибка {err}")
"""
"""
https://httpbin.org/
"""
"""response = requests.get("https://httpbin.org/get", params={'course': "networking"})
print(response.json())
"""
#import requests

"""
requests.get(url, params=None, **kwargs)

объект ответа = экземпляр Response

response.status_code

response.text

response.content - данные в байтовом формате
with open('image.jpg', 'wb') as f:
    f.write(response.content)
    
response.json()
data = response.json()
print(data['name']

response.headers - заголовки ответа
print(response.headers)
словарь 
    print(response.headers["Content-Type"]) тип содержимого
    #print(response.headers["User-agent"]) информация о клиентском приложении
    #print(response.headers["Authorization"]) данные для авторизации
    Accept - что мы хотим получить
    Date дата ответа
    Server информация о сервере

response.url - фактический url
print(response.url)

response.cookies


методы управления ошибками
response.raise_for_status() - проверяет код ответа и вызывает исключение HTTPError (если 400 500)
try:
    response = requests.get("https://api.github.com")
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Ошибка HTTP: {err}")


requests.get(url, params=None, **kwargs)
headers
timeout
auth
proxies
verify 
"""

"""
1
https://api.github.com
вывести код ответа, факт юрл, заголовки, тело
"""
"""try:
    response = requests.get("https://api.github.com")
    print(response.status_code)
    print(response.url)
    print(response.headers)
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"произошла ошибка при выполнении запроса{e}")"""
"""
2
https://httpbin.org/
передать ваше имя, course=networking task=get_request
вывести факт юрл
"""
"""try:
    params = {
        'name': "Name",
        'course': 'networking',
        'task': 'get_request'
    }
    response = requests.get("https://httpbin.org/get", params=params)
    print(response.url)

except requests.exceptions.RequestException as e:
    print(f"произошла ошибка при передаче параметров{e}")"""
"""
3
https://api.github.com/users/tsenturion
вывести логин login, ссылку на профиль html_url, количество репозиториев public_repos
"""
"""try:
    response = requests.get("https://api.github.com/users/tsenturion")
    response.raise_for_status()
    data = response.json()
    print(data.get("login"))
    print(data.get("html_url"))
    print(data.get('public_repos'))

except requests.exceptions.RequestException as e:
    print(f"произошла ошибка при получении данных пользователя{e}")
except ValueError:
    print('ошибка преобразования ответа в json')"""
"""
4
https://httpbin.org/headers
передать юзерагент любой
вывести тело
"""
"""try:
    headers = {
        'User-Agent': "my-app/0.0.1"
    }
    response = requests.get("https://httpbin.org/headers", headers=headers)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"произошла ошибка при отправке заголовков{e}")"""
"""
https://api.github.com/dfbdpfmds
обработка ошибок, таймаут
"""
"""try:
    response = requests.get("https://api.github.com/dfbdpfmds", timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP ошибка {http_err}")
except requests.exceptions.ConnectionError:
    print("ошибка соединения")
except requests.exceptions.Timeout:
    print("время ожидания истекло")
except requests.exceptions.RequestException as err:
    print(f"другая ошибка {err}")"""

#except requests.exceptions.ConnectionError: - не может установить соединение с сервером

#except requests.exceptions.Timeout: - запрос слишком долго ждет ответа от сервера

#    response.raise_for_status()
#except requests.exceptions.HTTPError as http_err: - неудачный код ответа от сервера

#TooManyRedirects - слишком много перенаправлений

#except requests.exceptions.RequestException as err: - поймать любую ошибку

"""
редирект перенаправление 300-399
301
302
303
307
308

сервер сообщает новый URL в заголовке Location
response.history - список всех промежуточных ответов

allow_redirects - переходить ли по новому адресу
"""

"""response = requests.get("http://github.com", allow_redirects=False)
print(response.url)
print(response.headers["Location"])
print(response.status_code)

print("история редиректов")
for resp in response.history:
    print(resp.status_code, resp.url)
"""

"""response = requests.get("http://github.com", allow_redirects=False)

if response.status_code in (301, 302, 303, 307, 308):
    new_url = response.headers['Location']
    print(f"перенаправляемся на {new_url}")
    new_response = requests.get(new_url)
    print(new_response.status_code)"""

#TooManyRedirects - слишком много перенаправлений (более 30)

"""from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = Session()
retries = Retry(total=5, redirect=5)
adapter = HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount("https://", adapter)

response = session.get("http://github.com")
print(response.url)"""
"""try:
    response = requests.get("зацикленный юрл")
except requests.exceptions.TooManyRedirects:
    print("слишком много перенаправлений")"""


"""
1
http://github.com
показать финальный url
список промежуточных переходов (статус и юрл)

2
http://github.com
с отключением автоматических 
получить статус и заголовок Location
показать адрес куда сервер предлагает перейти

3
добавить для 2 
вручную новый запрос на этот адрес
вывести финальный статус и юрл

4
https://httpbin.org/redirect/100
отправить запрос
перехватить ошибку
сообщение об ошибке

5
count_redirects(url: str) -> int
запрос к юрл
возвращает колво промежуточных редиректов
обработка искл
если ошибка return -1
"""
def count_redirects(url: str) -> int:
    try:
        response = requests.get(url, timeout=5)
        return len(response.history)
    except requests.exceptions.RequestException as e:
        print(f"ошибка запроса {e}")
        return -1