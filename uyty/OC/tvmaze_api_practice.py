import requests
import re
from textwrap import shorten

def clean_html(text):
    if text is None:
        return ""
    return re.sub(r'<[^>]+>', '', text)

def search_show(query):
    url = f"https://api.tvmaze.com/search/shows?q={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при поиске шоу: {e}")
        return None

def display_show_info(show):
    print("\nИнформация о шоу")
    print(f"Название: {show['name']}")
    print(f"Год запуска: {show['premiered']}")
    print(f"Жанры: {', '.join(show['genres']) if show['genres'] else 'Не указаны'}")
    
    description = clean_html(show['summary'])
    short_description = shorten(description, width=200, placeholder="...")
    print(f"Описание: {short_description}")

def get_seasons(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении сезонов: {e}")
        return None

def display_seasons(seasons):
    print("\n=== Сезоны шоу ===")
    for season in seasons:
        print(f"\nСезон {season['number']}:")
        print(f"  Начало: {season['premiereDate']}")
        print(f"  Окончание: {season['endDate'] or 'Еще выходит'}")

def get_episodes(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении эпизодов: {e}")
        return None

def display_episodes(episodes):

    print(f"\nВсего эпизодов: {len(episodes)} ===")
    print("\nПервые 5 эпизодов:")
    for episode in episodes[:5]:
        print(f"\nЭпизод {episode['number']} (Сезон {episode['season']}):")
        print(f"  Название: {episode['name']}")
        print(f"  Дата выхода: {episode['airdate']}")

def main():
    print("Поиск TV шоу на TVMaze ")
    query = input("Введите название шоу для поиска: ")
    
    # Поиск шоу
    results = search_show(query)
    if not results:
        print("Шоу не найдено или произошла ошибка.")
        return
    
    print(f"\nНайдено результатов: {len(results)}")
    
    for i, result in enumerate(results[:3], 1):
        show = result['show']
        print(f"\n{i}. {show['name']} ({show['premiered']})")
    
    try:
        choice = int(input("\nВыберите номер шоу для подробной информации (1-3): ")) - 1
        if choice < 0 or choice >= len(results[:3]):
            print("Неверный выбор.")
            return
    except ValueError:
        print("Введите число.")
        return
    
    selected_show = results[choice]['show']
    display_show_info(selected_show)
    
    seasons = get_seasons(selected_show['id'])
    if seasons:
        display_seasons(seasons)
    
    episodes = get_episodes(selected_show['id'])
    if episodes:
        display_episodes(episodes)

if __name__ == "__main__":
    main()