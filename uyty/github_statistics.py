import urllib.request
import urllib.error
import json
import math
from collections import Counter

def get_user_repos(username):
    base_url = f"https://api.github.com/users/{username}/repos"
    repos = []
    page = 1
    per_page = 100
    
    while True:
        url = f"{base_url}?page={page}&per_page={per_page}"
        req = urllib.request.Request(url)
        
    
        req.add_header('User-Agent', 'Python-urllib')
        
        try:
            with urllib.request.urlopen(req) as response:
                data = response.read().decode('utf-8')
                page_repos = json.loads(data)
                
                if not page_repos:
                    break
                    
                repos.extend(page_repos)
                page += 1
                
        except urllib.error.HTTPError as e:
            print(f"Ошибка: {e.code} - {e.reason}")
            error_data = e.read().decode('utf-8')
            error_json = json.loads(error_data)
            print(f"Сообщение от GitHub: {error_json.get('message', 'Unknown error')}")
            return None
            
        except urllib.error.URLError as e:
            print(f"Ошибка подключения: {e.reason}")
            return None
    
    return repos

def display_repos(repos, page_num, page_size=5):
    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size
    
    for repo in repos[start_idx:end_idx]:
        print(f"\nНазвание: {repo['name']}")
        print(f"Язык: {repo.get('language', 'Не указан')}")
        print(f"Звёзды: {repo['stargazers_count']}")
        print(f"Форки: {repo['forks_count']}")

def calculate_stats(repos):
    if not repos:
        return None
    
    total_repos = len(repos)
    languages = [repo.get('language') for repo in repos if repo.get('language')]
    most_common_language = Counter(languages).most_common(1)[0][0] if languages else "Нет данных"
    total_stars = sum(repo['stargazers_count'] for repo in repos)
    
    return {
        'total_repos': total_repos,
        'most_common_language': most_common_language,
        'total_stars': total_stars
    }

def main():
    username = input("Введите имя пользователя GitHub: ")
    repos = get_user_repos(username)
    
    if not repos:
        print("Не удалось получить репозитории пользователя")
        return
    
    total_pages = math.ceil(len(repos) / 5)
    current_page = 1
    
    while True:
        print(f"\n=== Страница {current_page}/{total_pages} ===")
        display_repos(repos, current_page)
        
        if current_page >= total_pages:
            break
            
        choice = input("\nНажмите Enter для следующей страницы или 'q' для выхода: ")
        if choice.lower() == 'q':
            break
            
        current_page += 1
    
    stats = calculate_stats(repos)
    print("\n=== Общая статистика ===")
    print(f"Всего репозиториев: {stats['total_repos']}")
    print(f"Самый популярный язык: {stats['most_common_language']}")
    print(f"Суммарное количество звёзд: {stats['total_stars']}")

if __name__ == "__main__":
    main()