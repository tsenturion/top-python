import requests
import time
from collections import Counter

def get_github_repos(username, token):
    headers = {'Authorization': f'token {token}'} if token else {}
    url = f'https://api.github.com/users/{username}/repos'
    repos = []
    page = 1
    per_page = 100 
    
    while True:
        params = {'page': page, 'per_page': per_page}
        response = requests.get(url, headers=headers, params=params)
        

        if response.status_code == 403 and 'rate limit exceeded' in response.text.lower():
            reset_time = int(response.headers.get('X-RateLimit-Reset', time.time() + 60))
            wait_time = max(0, reset_time - time.time())
            print(f"Rate limit exceeded. Waiting {wait_time:.0f} seconds...")
            time.sleep(wait_time)
            continue
            
        response.raise_for_status()
        data = response.json()
        
        if not data:
            break
            
        repos.extend(data)
        page += 1
        

        if len(data) < per_page:
            break
    
    return repos

def display_repos(repos, page_num, page_size=5):
    start = (page_num - 1) * page_size
    end = start + page_size
    page_repos = repos[start:end]
    
    for repo in page_repos:
        print(f"\nНазвание: {repo['name']}")
        print(f"Язык: {repo['language'] or 'Не указан'}")
        print(f"Звёзды: {repo['stargazers_count']}")
        print(f"Форки: {repo['forks_count']}")
    
    return len(page_repos)

def calculate_stats(repos):
    total_repos = len(repos)
    languages = [repo['language'] for repo in repos if repo['language']]
    most_common_language = Counter(languages).most_common(1)[0][0] if languages else "Нет данных"
    total_stars = sum(repo['stargazers_count'] for repo in repos)
    
    return {
        'total_repos': total_repos,
        'most_common_language': most_common_language,
        'total_stars': total_stars
    }

def main():
    username = input("Введите имя пользователя GitHub: ")
    token = input("Введите ваш GitHub токен (или оставьте пустым для анонимного доступа): ").strip()
    
    try:
        print("\nЗагрузка репозиториев...")
        repos = get_github_repos(username, token)
        
        if not repos:
            print("У этого пользователя нет репозиториев или пользователь не существует.")
            return
        
        stats = calculate_stats(repos)
        print(f"\nНайдено репозиториев: {stats['total_repos']}")
        
        page_num = 1
        page_size = 5
        total_pages = (len(repos) + page_size - 1) // page_size
        
        while True:
            print(f"\n=== Страница {page_num} из {total_pages} ===")
            displayed = display_repos(repos, page_num, page_size)
            
            if displayed < page_size or page_num * page_size >= len(repos):
                break
                
            choice = input("\nНажмите Enter для следующей страницы или 'q' для выхода: ")
            if choice.lower() == 'q':
                break
                
            page_num += 1
        
        # Вывод статистики
        print("\n=== Общая статистика ===")
        print(f"Всего репозиториев: {stats['total_repos']}")
        print(f"Самый популярный язык: {stats['most_common_language']}")
        print(f"Суммарное количество звёзд: {stats['total_stars']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к GitHub API: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()