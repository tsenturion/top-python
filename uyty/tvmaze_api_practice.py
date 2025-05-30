import http.client
import urllib.parse
import json
import re

def strip_html(text):
    return re.sub(r'<[^>]+>', '', text)

def get_show_search_results(query):
    conn = http.client.HTTPSConnection("api.tvmaze.com")
    path = f"/search/shows?q={urllib.parse.quote(query)}"
    conn.request("GET", path)
    res = conn.getresponse()
    data = json.loads(res.read().decode())
    return data

def get_seasons(show_id):
    conn = http.client.HTTPSConnection("api.tvmaze.com")
    path = f"/shows/{show_id}/seasons"
    conn.request("GET", path)
    res = conn.getresponse()
    return json.loads(res.read().decode())

def get_episodes(show_id):
    conn = http.client.HTTPSConnection("api.tvmaze.com")
    path = f"/shows/{show_id}/episodes"
    conn.request("GET", path)
    res = conn.getresponse()
    return json.loads(res.read().decode())

def main():
    query = input("Введите название шоу для поиска: ").strip()
    results = get_show_search_results(query)

    if not results:
        print("Ничего не найдено.")
        return

    print("\n🔎 Найденные шоу:")
    for i, result in enumerate(results):
        show = result['show']
        name = show.get('name')
        premiered = show.get('premiered', 'N/A')
        genres = ", ".join(show.get('genres', []))
        summary = strip_html(show.get('summary') or "")[:200]
        print(f"\n[{i + 1}] {name} ({premiered})")
        print(f"   Жанры: {genres}")
        print(f"   Описание: {summary}...")

    # Выбор первого шоу
    selected_show = results[0]['show']
    show_id = selected_show['id']
    print(f"\n📺 Выбрано шоу: {selected_show['name']} (ID: {show_id})")

    # Получение сезонов
    seasons = get_seasons(show_id)
    print("\n📅 Сезоны:")
    for season in seasons:
        print(f"  Сезон {season['number']}: {season.get('premiereDate')} — {season.get('endDate')}")

    # Получение эпизодов
    episodes = get_episodes(show_id)
    print(f"\n🎬 Всего эпизодов: {len(episodes)}")
    print("Первые 5 эпизодов:")
    for ep in episodes[:5]:
        print(f"  - {ep['name']} ({ep.get('airdate')})")

if __name__ == "__main__":
    main()
