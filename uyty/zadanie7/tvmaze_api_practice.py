import requests
import re

def clean_html_tags(text):
    if not text:
        return ""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def search_shows(query):
    url = f"https://api.tvmaze.com/search/shows?q={query}"
    r = requests.get(url)
    return r.json()

def get_show_seasons(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    r = requests.get(url)
    return r.json()

def get_show_episodes(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    r = requests.get(url)
    return r.json()

if __name__ == "__main__":
    query = input("Введите название шоу для поиска (например, Friends): ")
    results = search_shows(query)

    print(f"\nНайдено шоу: {len(results)}\n")
    for idx, item in enumerate(results):
        show = item['show']
        name = show.get("name")
        premiered = show.get("premiered", "N/A")
        genres = ', '.join(show.get("genres", []))
        summary = clean_html_tags(show.get("summary", ""))
        short_summary = summary[:200].replace('\n', ' ') + ("..." if len(summary) > 200 else "")
        print(f"{idx+1}. {name} ({premiered[:4] if premiered != 'N/A' else 'N/A'})")
        print(f"   Жанры: {genres}")
        print(f"   Описание: {short_summary}\n")

    if not results:
        print("Нет результатов.")
        exit()

    choice = input(f"Выберите номер шоу (1-{len(results)}) [по умолчанию 1]: ")
    if not choice.strip().isdigit():
        choice_idx = 0
    else:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(results):
            choice_idx = 0

    show = results[choice_idx]['show']
    show_id = show['id']
    print(f"\nID выбранного шоу: {show_id} ({show['name']})")

    # Получаем сезоны
    print("\nСписок сезонов:")
    seasons = get_show_seasons(show_id)
    for season in seasons:
        num = season.get('number')
        premiere = season.get('premiereDate', 'N/A')
        end = season.get('endDate', 'N/A')
        print(f"  Сезон {num}: {premiere} — {end}")

    # Получаем эпизоды
    episodes = get_show_episodes(show_id)
    print(f"\nВсего эпизодов: {len(episodes)}")
    print("Первые 5 эпизодов:")
    for ep in episodes[:5]:
        print(f"  {ep.get('season')}x{ep.get('number')} — {ep.get('name')} ({ep.get('airdate')})")

    # Сохраняем результат в .txt
    with open("tvmaze_result.txt", "w", encoding="utf-8") as f:
        f.write(f"Найдено шоу: {len(results)}\n\n")
        for idx, item in enumerate(results):
            show = item['show']
            name = show.get("name")
            premiered = show.get("premiered", "N/A")
            genres = ', '.join(show.get("genres", []))
            summary = clean_html_tags(show.get("summary", ""))
            short_summary = summary[:200].replace('\n', ' ') + ("..." if len(summary) > 200 else "")
            f.write(f"{idx+1}. {name} ({premiered[:4] if premiered != 'N/A' else 'N/A'})\n")
            f.write(f"   Жанры: {genres}\n")
            f.write(f"   Описание: {short_summary}\n\n")
        f.write(f"\nID выбранного шоу: {show_id} ({show['name']})\n")
        f.write("\nСписок сезонов:\n")
        for season in seasons:
            num = season.get('number')
            premiere = season.get('premiereDate', 'N/A')
            end = season.get('endDate', 'N/A')
            f.write(f"  Сезон {num}: {premiere} — {end}\n")
        f.write(f"\nВсего эпизодов: {len(episodes)}\n")
        f.write("Первые 5 эпизодов:\n")
        for ep in episodes[:5]:
            f.write(f"  {ep.get('season')}x{ep.get('number')} — {ep.get('name')} ({ep.get('airdate')})\n")

    print('\nРезультаты записаны в файл tvmaze_result.txt')
