import http.client
import json
import html
from urllib.parse import quote

def fetch_show_data(show_name):
    conn = http.client.HTTPSConnection("api.tvmaze.com")
    conn.request("GET", f"/search/shows?q={quote(show_name)}")
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return json.loads(data)

def fetch_show_details(show_id):
    conn = http.client.HTTPSConnection("api.tvmaze.com")
    conn.request("GET", f"/shows/{show_id}")
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return json.loads(data)

def fetch_seasons(show_id):
    conn = http.client.HTTPSConnection("api.tvmaze.com")
    conn.request("GET", f"/shows/{show_id}/seasons")
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return json.loads(data)

def fetch_episodes(show_id):
    conn = http.client.HTTPSConnection("api.tvmaze.com")
    conn.request("GET", f"/shows/{show_id}/episodes")
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return json.loads(data)

def clean_html_tags(text):
    return html.unescape(text).replace("\n", " ").strip()

def display_show_info(show):
    print(f"Название: {show['name']}")
    print(f"Год запуска: {show['premiered']}")
    print(f"Жанры: {', '.join(show['genres'])}")
    print(f"Описание: {clean_html_tags(show['summary'])[:200]}...")
    print("-" * 50)

def display_seasons(seasons):
    for season in seasons:
        print(f"Сезон {season['number']}: {season['premiereDate']} - {season['endDate']}")
    print("-" * 50)

def display_episodes(episodes):
    print(f"Общее количество эпизодов: {len(episodes)}")
    for episode in episodes[:5]:
        print(f"{episode['name']} ({episode['airdate']})")
    print("-" * 50)

def main():
    show_name = input("Введите название шоу: ")
    shows = fetch_show_data(show_name)
    if not shows:
        print("Шоу не найдено.")
        return

    show = shows[0]['show']
    display_show_info(show)

    show_id = show['id']
    seasons = fetch_seasons(show_id)
    display_seasons(seasons)

    episodes = fetch_episodes(show_id)
    display_episodes(episodes)

if __name__ == "__main__":
    main()