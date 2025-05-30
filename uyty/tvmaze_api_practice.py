import requests
import re

# 1. Функция для очистки HTML-тегов из описания
def clean_summary(text):
    return re.sub(r'<[^>]+>', '', text)[:200] + '...' if text else 'Нет описания'

# 2. Поиск шоу по имени
search_query = input("Введите название шоу: ")
search_url = f"https://api.tvmaze.com/search/shows?q={search_query}"
search_response = requests.get(search_url)

if search_response.status_code != 200:
    print("Ошибка при поиске шоу!")
    exit()

search_results = search_response.json()

# 3. Вывод результатов поиска
print("\nРезультаты поиска:")
for idx, result in enumerate(search_results, 1):
    show = result['show']
    print(f"\n{idx}. {show['name']}")
    print(f"   Год запуска: {show.get('premiered', 'Неизвестно')}")
    print(f"   Жанры: {', '.join(show['genres']) if show['genres'] else 'Нет жанров'}")
    print(f"   Описание: {clean_summary(show.get('summary'))}")

# 4. Выбор первого шоу из результатов
selected_show = search_results[0]['show']
show_id = selected_show['id']
print(f"\nВыбрано шоу: {selected_show['name']} (ID: {show_id})")

# 5. Получение списка сезонов
seasons_url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
seasons_response = requests.get(seasons_url)

if seasons_response.status_code == 200:
    seasons = seasons_response.json()
    print("\nСезоны:")
    for season in seasons:
        print(f"Сезон {season['number']}:")
        print(f"  Начало: {season.get('premiereDate', 'Неизвестно')}")
        print(f"  Окончание: {season.get('endDate', 'Неизвестно')}")
else:
    print("\nОшибка при получении сезонов!")

# 6. Получение списка эпизодов
episodes_url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
episodes_response = requests.get(episodes_url)

if episodes_response.status_code == 200:
    episodes = episodes_response.json()
    print(f"\nВсего эпизодов: {len(episodes)}")
    print("\nПервые 5 эпизодов:")
    for episode in episodes[:5]:
        print(f"Эпизод {episode['number']}: {episode['name']}")
        print(f"  Дата выхода: {episode.get('airdate', 'Неизвестно')}")
else:
    print("\nОшибка при получении эпизодов!")
