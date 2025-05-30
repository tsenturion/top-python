import requests
import re

def search_shows(query):
    url = f"https://api.tvmaze.com/search/shows?q={query}"
    response = requests.get(url)
    return response.json()

def strip_html(html_text):
    if not html_text:
        return ""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html_text)

def get_show_seasons(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    response = requests.get(url)
    return response.json()

def get_show_episodes(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    response = requests.get(url)
    return response.json()

def main():
    query = input("Введите название шоу для поиска: ").strip()
    results = search_shows(query)

    if not results:
        print("Шоу не найдено!")
        return

    print(f"\nНайдено {len(results)} шоу(шоу):\n")

    for idx, item in enumerate(results):
        show = item['show']
        name = show.get('name', '-')
        premiered = show.get('premiered', '-')  # формат: '1994-09-22'
        year = premiered.split('-')[0] if premiered else '-'
        genres = ', '.join(show.get('genres', [])) or '-'
        summary = strip_html(show.get('summary', '')).strip()
        summary_short = summary[:200] + ('...' if len(summary) > 200 else '')
        print(f"{idx+1}. {name} ({year})")
        print(f"   Жанры: {genres}")
        print(f"   Описание: {summary_short}\n")

    # Выбрать шоу
    while True:
        try:
            show_idx = int(input(f"Выбери номер шоу (1-{len(results)}): "))
            if 1 <= show_idx <= len(results):
                break
            print("Некорректный номер. Попробуй ещё раз.")
        except ValueError:
            print("Введи номер.")

    show = results[show_idx-1]['show']
    show_id = show['id']
    print(f"\nВыбрано шоу: {show['name']}, ID = {show_id}\n")

    # Сезоны
    seasons = get_show_seasons(show_id)
    print("Сезоны:")
    for season in seasons:
        num = season.get('number', '-')
        premiere = season.get('premiereDate', '-')
        end = season.get('endDate', '-')
        print(f"  Сезон {num}: {premiere} — {end}")
    print()

    # Эпизоды
    episodes = get_show_episodes(show_id)
    print(f"Всего эпизодов: {len(episodes)}")
    print("Первые 5 эпизодов:")
    for ep in episodes[:5]:
        ep_name = ep.get('name', '-')
        ep_airdate = ep.get('airdate', '-')
        print(f"  {ep_name} ({ep_airdate})")

if __name__ == "__main__":
    main()
