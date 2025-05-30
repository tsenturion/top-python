import http.client
import json
from collections import Counter

# ⚠️ ЗАМЕНИ токен на актуальный при необходимости
DEFAULT_TOKEN = ""  # Внимание: Никогда не публикуй его!

def get_repos(username, token):
    repos = []
    page = 1

    while True:
        path = f"/users/{username}/repos?per_page=100&page={page}"
        conn = http.client.HTTPSConnection("api.github.com")
        headers = {
            "User-Agent": "Python",
            "Authorization": f"token {token}"
        }

        conn.request("GET", path, headers=headers)
        response = conn.getresponse()

        if response.status != 200:
            print(f"Ошибка: {response.status} {response.reason}")
            print(response.read().decode())
            return []

        data = json.loads(response.read().decode())
        if not data:
            break

        repos.extend(data)
        page += 1

    return repos

def display_repos_paginated(repos):
    for i in range(0, len(repos), 5):
        for repo in repos[i:i+5]:
            print(f"🔹 {repo['name']}")
            print(f"   Язык: {repo.get('language')}")
            print(f"   ⭐ Звёзды: {repo.get('stargazers_count')}")
            print(f"   🍴 Форки: {repo.get('forks_count')}")
            print()
        if i + 5 < len(repos):
            input("Нажмите Enter для следующей страницы...")

def analyze_stats(repos):
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
    languages = [repo.get('language') for repo in repos if repo.get('language')]
    common_lang = Counter(languages).most_common(1)

    print("📊 Общая статистика:")
    print(f"Всего репозиториев: {len(repos)}")
    print(f"Суммарное количество звёзд: {total_stars}")
    if common_lang:
        print(f"Самый популярный язык: {common_lang[0][0]} ({common_lang[0][1]} репозиториев)")
    else:
        print("Нет информации о языках.")

def main():
    username = input("Введите имя пользователя GitHub: ").strip()
    repos = get_repos(username, DEFAULT_TOKEN)

    if not repos:
        print("Нет данных или ошибка при получении.")
        return

    display_repos_paginated(repos)
    analyze_stats(repos)

if __name__ == "__main__":
    main()
