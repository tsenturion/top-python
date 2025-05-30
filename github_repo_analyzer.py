import urllib.request
import json
from collections import Counter

def main():
    username = input("Введите имя пользователя GitHub: ").strip()
    token = input("Введите ваш персональный токен GitHub: ").strip()

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'token {token}'
    }

    per_page = 5
    page = 1
    total_repos = 0
    total_stars = 0
    language_counter = Counter()

    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page={per_page}&page={page}"
        req = urllib.request.Request(url, headers=headers)

        try:
            with urllib.request.urlopen(req) as response:
                if response.status != 200:
                    print(f"Ошибка: получен статус-код {response.status}")
                    break

                data = json.loads(response.read().decode())
                if not data:
                    break  # Нет больше репозиториев

                print(f"\nСтраница {page}:\n")
                for repo in data:
                    name = repo.get('name', 'N/A')
                    language = repo.get('language', 'N/A')
                    stars = repo.get('stargazers_count', 0)
                    forks = repo.get('forks_count', 0)

                    print(f"Название: {name}")
                    print(f"Язык программирования: {language}")
                    print(f"Звёзды: {stars}")
                    print(f"Форки: {forks}")
                    print("-" * 40)

                    total_repos += 1
                    total_stars += stars
                    if language:
                        language_counter[language] += 1

                page += 1

        except urllib.error.HTTPError as e:
            print(f"HTTP ошибка: {e.code} - {e.reason}")
            break
        except urllib.error.URLError as e:
            print(f"Ошибка URL: {e.reason}")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break

    print("\nОбщая статистика:")
    print(f"Общее количество репозиториев: {total_repos}")
    if language_counter:
        most_common_language = language_counter.most_common(1)[0][0]
        print(f"Наиболее часто используемый язык: {most_common_language}")
    else:
        print("Наиболее часто используемый язык: N/A")
    print(f"Суммарное количество звёзд: {total_stars}")

if __name__ == "__main__":
    main()