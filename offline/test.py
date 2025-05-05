import requests

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    'q': 'Moscow',
    'appid': "",
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    print(data['name'], data['main']['temp'], data['weather'][0]['description'])

else:
    print('ошибка', response.status_code)