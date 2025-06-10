# подключаем необходимые библиотеки
import requests
import pandas as pd
import plotly.express as px

# URL для получения списка ТВ-шоу, где в названии есть слово "друзья (friends)"
url = "https://api.tvmaze.com/search/shows?q=friends"

# отправляем GET-запрос и получаем ответ в формате JSON
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Ошибка при запросе: {response.status_code}")

data = response.json()

# преобразуем JSON в список
shows_list = list(data)

# выводим на экран количество выгруженных шоу
print(f"Количество шоу с 'friends' в названии: {len(shows_list)}")

# создаем список с данными по каждому шоу
shows_data = []
for item in shows_list:
    show = item.get('show', {})
    name = show.get('name', 'Unknown')
    language = show.get('language', 'Unknown')
    genres = show.get('genres', [])

    # пропускаем шоу без жанров
    # иначе будет ошибка
    if not genres:
        continue

    for genre in genres:  # добавим одну строку на каждый жанр
        shows_data.append({
            'name': name,
            'language': language,
            'genre': genre
        })

# формируем DataFrame на основании списка с данными по каждому шоу
df = pd.DataFrame(shows_data)

# строим Sunburst-диаграмму
fig = px.sunburst(
    df,
    path=['language', 'genre', 'name'],
    title='Sunburst-диаграмма: Язык → Жанр → Название шоу ("Friends")',
    width=800,
    height=600
)
fig.show()