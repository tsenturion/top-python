# подключаем необходимые библиотеки
import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL для получения списка ТВ-шоу, где в названии есть слово "сверхъестественное (supernatural)"
search_url = "https://api.tvmaze.com/search/shows?q=supernatural"

# отправляем GET-запрос и получаем ответ в формате JSON
search_response = requests.get(search_url)
if search_response.status_code != 200:
    raise Exception(f"Ошибка при запросе: {search_response.status_code}")

search_data = search_response.json()

# преобразуем JSON в список
search_results = list(search_data)

# сохраняем id сериала "Сверхъестественное" (Supernatural, 2005–2020)
supernatural_id = None
for item in search_results:
    show = item.get('show', {})
    if show.get('name', '').lower() == 'supernatural' and '2005' in str(show.get('premiered', '')):
        supernatural_id = show['id']
        break

if supernatural_id is None:
    raise Exception("Сериал 'Сверхъестественное' не найден")

# URL для получения списка эпизодов сериала "Сверхъестественное"
episodes_url = f"https://api.tvmaze.com/shows/{supernatural_id}/episodes"

# отправляем GET-запрос и получаем ответ в формате JSON
episodes_response = requests.get(episodes_url)
if episodes_response.status_code != 200:
    raise Exception(f"Ошибка при получении эпизодов: {episodes_response.status_code}")

episodes_data = episodes_response.json()

# формируем DataFrame на основании списка с данными по каждой серии
episodes_df = pd.DataFrame(episodes_data)

# отфильтровываем только нужные столбцы
episodes_df = episodes_df[['season', 'number', 'name', 'airdate', 'rating']]
episodes_df['average'] = episodes_df['rating'].apply(lambda r: r['average'] if isinstance(r, dict) else None)

# находим данные о серии с минимальным рейтингом
min_rating_episode = episodes_df.loc[episodes_df['average'].idxmin()]
print("Серия с минимальным рейтингом:")
print(min_rating_episode)

# находим данные о серии с максимальным рейтингом
max_rating_episode = episodes_df.loc[episodes_df['average'].idxmax()]
print("Серия с максимальным рейтингом:")
print(max_rating_episode)

# группируем данные и вычисляем средний рейтинг для каждого сезона
season_ratings = episodes_df.groupby('season')['average'].mean().reset_index()

# строим столбчатую диаграмму рейтинга сезонов сериала "Сверхъестественное"
plt.figure(figsize=(12, 6))
plt.bar(season_ratings['season'], season_ratings['average'], color='skyblue')
plt.xlabel('Сезон')
plt.ylabel('Средний рейтинг')
plt.title('Средний рейтинг по сезонам сериала "Сверхъестественное" (2005–2020)')
plt.xticks(season_ratings['season'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()