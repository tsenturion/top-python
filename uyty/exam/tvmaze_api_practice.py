import requests
import re

OUTPUT_FILE = "tvmaze_api_practice.txt"

def remove_html_tags(text):
    return re.sub('<.*?>', '', text or '')

def search_show(show_name):
    url = f"https://api.tvmaze.com/search/shows?q={show_name}"
    response = requests.get(url)
    return response.json()

def get_show_seasons(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    response = requests.get(url)
    return response.json()

def get_show_episodes(show_id):
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    response = requests.get(url)
    return response.json()

def main():
    show_name = "Friends"
    results = search_show(show_name)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        f.write(f"Результаты поиска для шоу: {show_name}\n\n")
        for i, result in enumerate(results):
            show = result['show']
            summary = remove_html_tags(show.get('summary', ''))
            f.write(f"{i + 1}. Название: {show['name']}\n")
            f.write(f"   Год запуска: {show.get('premiered', 'N/A')}\n")
            f.write(f"   Жанры: {', '.join(show.get('genres', []))}\n")
            f.write(f"   Описание: {summary[:200]}...\n\n")

        if not results:
            f.write("Шоу не найдено.")
            return

        selected_show = results[0]['show']
        show_id = selected_show['id']
        f.write(f"Выбранное шоу: {selected_show['name']} (ID: {show_id})\n\n")

        seasons = get_show_seasons(show_id)
        f.write("Сезоны:\n")
        for season in seasons:
            f.write(f"- Сезон {season['number']}: {season.get('premiereDate', 'N/A')} — {season.get('endDate', 'N/A')}\n")
        f.write("\n")

        episodes = get_show_episodes(show_id)
        f.write(f"Всего эпизодов: {len(episodes)}\n")
        f.write("Первые 5 эпизодов:\n")
        for episode in episodes[:5]:
            f.write(f"- {episode['name']} ({episode.get('airdate', 'N/A')})\n")

    print(f"Results written in file {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
