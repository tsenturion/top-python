import requests
response = requests.get("https://api/openweathermap.org/data/2.5/weater?q=London&appid=")
data = response.json()
print(data)