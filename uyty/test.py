import requests

url = 'https://api.openweathermap.org/data/2.5/weather'

params = {
    'q': 'Moscow',             
    'appid': '99a9a75da640a2098df3bc7c5a91a721',  
    'units': 'metric',         
    'lang': 'ru'               
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()  
    print('Погода в городе:', data['name'])
    print('Температура:', data['main']['temp'], '°C')
    print('Описание:', data['weather'][0]['description'])
else:
    print('Ошибка при запросе данных:', response.status_code)
