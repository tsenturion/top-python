import requests

def get_repos(username):
    page = 1
    per_page = 5
    all_repos = []

    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page={per_page}&page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            print("Ошибка:", response.status_code)
            return []

        repos = response.json()
        if not repos:
            break

        for repo in repos:
            name = repo["name"]
            lang = repo["language"]
            stars = repo["stargazers_count"]
            forks = repo["forks_count"]
            print(f"\nНазвание: {name}")
            print(f"Язык: {lang}")
            print(f"Звёзды: {stars}, Форки: {forks}")
            all_repos.append(repo)

        page += 1
        input("\nНажмите Enter для загрузки следующих 5...")

    return all_repos

def show_stats(repos):
    total = len(repos)
    langs = {}
    stars = 0

    for r in repos:
        lang = r["language"]
        if lang:
            langs[lang] = langs.get(lang, 0) + 1
        stars += r["stargazers_count"]

    # Наиболее частый язык
    if langs:
        most_common = max(langs, key=langs.get)
    else:
        most_common = "Неизвестно"

    print("\n=== Статистика ===")
    print("Всего репозиториев:", total)
    print("Часто используемый язык:", most_common)
    print("Общее число звёзд:", stars)

if __name__ == "__main__":
    user = input("Введите имя пользователя GitHub: ")
    repos = get_repos(user)
    if repos:
        show_stats(repos)
