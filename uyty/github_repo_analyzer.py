import requests
from collections import Counter

def fetch_repos(killer2101, headers, per_page=5):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{killer2101}/repos"
        params = {"per_page": per_page, "page": page}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Ошибка запроса: {response.status_code}")
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def print_repo_info(repos):
    for repo in repos:
        print(f"Название: {repo.get('name')}")
        print(f"Язык: {repo.get('language')}")
        print(f"Звёзды: {repo.get('stargazers_count')}")
        print(f"Форки: {repo.get('forks_count')}")
        print("-" * 40)

def print_statistics(repos):
    total_repos = len(repos)
    languages = [repo.get('language') for repo in repos if repo.get('language')]
    stars_sum = sum(repo.get('stargazers_count', 0) for repo in repos)

    most_common_lang = None
    if languages:
        most_common_lang = Counter(languages).most_common(1)[0][0]

    print("\nОбщая статистика:")
    print(f"Общее количество репозиториев: {total_repos}")
    print(f"Язык, который встречается чаще всего: {most_common_lang}")
    print(f"Суммарное количество звёзд: {stars_sum}")

def main():
    username = input("Введите имя пользователя GitHub: ").strip()

    headers = {"Authorization": f"token {token}"}
    repos = fetch_repos(username, headers, per_page=5)

    if not repos:
        print("Репозитории не найдены или ошибка запроса.")
        return

    print_repo_info(repos)
    print_statistics(repos)

if __name__ == "__main__":
    main()
