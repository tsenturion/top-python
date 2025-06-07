import urllib.request
import urllib.parse
import json
import re
from textwrap import shorten

def clean_html_tags(text):
    """Удаляет HTML-теги из текста"""
    if text is None:
        return ""
    return re.sub(r'<[^>]+>', '', text)

def get_show_info(show_name):
    """Поиск шоу по имени"""
    url = f"https://api.tvmaze.com/search/shows?q={urllib.parse.quote(show_name)}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
    except Exception as e:
        print(f"Ошибка при запросе шоу: {e}")
        return None

def get_seasons(show_id):
    """Получение списка сезонов по ID шоу"""
    url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Ошибка при запросе сезонов: {e}")
        return None

def get_episodes(show_id):
    """Получение списка эпизодов по ID шоу"""
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Ошибка при запросе эпизодов: {e}")
        return None

def main():
    # 1. Поиск шоу по имени
    show_name = input("Введите название шоу для поиска: ")
    shows = get_show_info(show_name)
    
    if not shows:
        print("Шоу не найдено")
        return
    
    print("\nНайденные шоу:")
    for i, show_data in enumerate(shows[:5], 1):
        show = show_data['show']
        print(f"\n{i}. {show['name']}")
        print(f"   Год запуска: {show.get('premiered', 'неизвестно')}")
        print(f"   Жанры: {', '.join(show.get('genres', ['не указаны']))}")
        description = clean_html_tags(show.get('summary'))
        print(f"   Описание: {shorten(description, width=200, placeholder='...')}")
    
    # 2. Выбор шоу (берем первое)
    selected_show = shows[0]['show']
    show_id = selected_show['id']
    print(f"\nВыбрано шоу: {selected_show['name']} (ID: {show_id})")
    
    # 3. Получение сезонов
    seasons = get_seasons(show_id)
    if seasons:
        print("\nСезоны:")
        for season in seasons:
            print(f"Сезон {season['number']}:")
            print(f"   Начало: {season.get('premiereDate', 'неизвестно')}")
            print(f"   Окончание: {season.get('endDate', 'неизвестно')}")
    
    # 4. Получение эпизодов
    episodes = get_episodes(show_id)
    if episodes:
        print(f"\nВсего эпизодов: {len(episodes)}")
        print("\nПервые 5 эпизодов:")
        for episode in episodes[:5]:
            print(f"Эпизод {episode['season']}x{episode['number']}: {episode['name']}")
            print(f"   Дата выхода: {episode.get('airdate', 'неизвестно')}")

if __name__ == "__main__":
    main()