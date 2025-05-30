import urllib.request
import urllib.parse
import json
from collections import Counter

def get_repos(username, per_page=5):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{urllib.parse.quote(username)}/repos?per_page={per_page}&page={page}"
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
        if not data:
            break
        repos.extend(data)
        if len(data) < per_page:
            break
        page += 1
    return repos

def main():
    username = input("Введите имя пользователя GitHub: ").strip()
    per_page = 5

    print(f"\nЗагрузка репозиториев пользователя {username}...\n")

    repos = get_repos(username, per_page=per_page)
    if not repos:
        print("У пользователя нет публичных репозиториев или пользователь не найден.")
        return

    total_stars = 0
    language_counter = Counter()

    # Постраничный вывод
    for i in range(0, len(repos), per_page):
        print(f"--- Страница {(i // per_page) + 1} ---")
        for repo in repos[i:i+per_page]:
            name = repo.get("name", "—")
            language = repo.get("language") or "—"
            stars = repo.get("stargazers_count", 0)
            forks = repo.get("forks_count", 0)
            print(f"Название: {name}")
            print(f"Язык программирования: {language}")
            print(f"Звёзды: {stars}")
            print(f"Форки: {forks}")
            print()
            total_stars += stars
            if language and language != "—":
                language_counter[language] += 1
        if i + per_page < len(repos):
            input("Нажмите Enter для показа следующей страницы...")

    # Общая статистика
    print("=== Общая статистика ===")
    print(f"Общее количество репозиториев: {len(repos)}")
    if language_counter:
        most_common_lang, lang_count = language_counter.most_common(1)[0]
        print(f"Чаще всего используемый язык: {most_common_lang} ({lang_count} раз)")
    else:
        print("Нет данных о языках.")
    print(f"Суммарное количество звёзд: {total_stars}")

if __name__ == "__main__":
    main()
