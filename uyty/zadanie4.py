import requests
from collections import Counter

def fetch_repos(username, token, per_page=5):
    page = 1
    repos = []
    headers = {"Authorization": f"token {token}"}

    output_lines = []
    output_lines.append(f"\nЗагружаем репозитории пользователя '{username}'...\n")

    while True:
        url = f"https://api.github.com/users/{username}/repos"
        params = {'per_page': per_page, 'page': page}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            error = f"Ошибка: {response.status_code}. Проверьте имя пользователя или токен."
            print(error)
            output_lines.append(error)
            break

        batch = response.json()
        if not batch:
            break

        repos.extend(batch)

        for repo in batch:
            info = (
                f"📦 {repo['name']}\n"
                f"   Язык: {repo['language']}\n"
                f"   ⭐ Звёзды: {repo['stargazers_count']}\n"
                f"   🍴 Форки: {repo['forks_count']}\n"
            )
            print(info)
            output_lines.append(info)

        page += 1
        input("Нажмите Enter для загрузки следующей страницы...\n")

    return repos, output_lines

def analyze_repos(repos):
    total = len(repos)
    stars = sum(repo['stargazers_count'] for repo in repos)
    languages = [repo['language'] for repo in repos if repo['language']]
    most_common_lang = Counter(languages).most_common(1)
    most_used = most_common_lang[0][0] if most_common_lang else "Неизвестно"

    analysis = (
        "\n📊 Общая статистика:\n"
        f"Всего репозиториев: {total}\n"
        f"Наиболее используемый язык: {most_used}\n"
        f"Суммарное количество звёзд: {stars}\n"
    )
    print(analysis)
    return analysis

def main():
    username = input("Введите имя пользователя GitHub: ").strip()
    token = input("Введите ваш GitHub токен (Personal Access Token): ").strip()

    repos, output_lines = fetch_repos(username, token)

    if repos:
        analysis_result = analyze_repos(repos)
        output_lines.append(analysis_result)

    # Сохраняем вывод в файл
    with open("github_repo_analyzer.txt", "w", encoding="utf-8") as f:
        f.writelines(output_lines)

    print("Результаты сохранены в 'github_repo_analyzer.txt'.")

if __name__ == "__main__":
    main()
