import requests
import re

def clean_html(raw_html):
    """Удаляет HTML-теги из строки"""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def search_shows(query):
    url = f"https://api.tvmaze.com/search/shows?q={query}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_seasons(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_episodes(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    query = input("Введите название шоу для поиска: ").strip()
    results = search_shows(query)

    if not results:
        print("Шоу не найдено.")
        return

    print(f"\nНайдено {len(results)} шоу по запросу '{query}':\n")
    for i, item in enumerate(results, 1):
        show = item['show']
        name = show.get('name', 'N/A')
        premiered = show.get('premiered', 'N/A')
        genres = ", ".join(show.get('genres', [])) or 'N/A'
        summary = show.get('summary') or ''
        summary_clean = clean_html(summary)[:200]
        print(f"{i}. Название: {name}")
        print(f"   Год запуска: {premiered}")
        print(f"   Жанры: {genres}")
        print(f"   Описание: {summary_clean}")
        print()

    # Выбираем первое шоу для дальнейшей работы
    chosen_show = results[0]['show']
    show_id = chosen_show['id']
    print(f"Выбрано шоу: {chosen_show['name']} (ID: {show_id})\n")

    seasons = get_seasons(show_id)
    print(f"Сезоны шоу '{chosen_show['name']}':")
    for season in seasons:
        number = season.get('number', 'N/A')
        premiereDate = season.get('premiereDate', 'N/A')
        endDate = season.get('endDate', 'N/A')
        print(f"  Сезон {number}: с {premiereDate} по {endDate}")

    episodes = get_episodes(show_id)
    print(f"\nВсего эпизодов: {len(episodes)}")
    print("Первые 5 эпизодов:")
    for ep in episodes[:5]:
        ep_name = ep.get('name', 'N/A')
        airdate = ep.get('airdate', 'N/A')
        season_num = ep.get('season', 'N/A')
        number = ep.get('number', 'N/A')
        print(f"  Сезон {season_num}, эпизод {number}: {ep_name} (Дата выхода: {airdate})")

if __name__ == "__main__":
    main()
