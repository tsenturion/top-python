import requests
import time

def get_user_repos(username, token, page=1, per_page=5):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {'Authorization': f'token {token}'} if token else {}
    params = {
        'page': page,
        'per_page': per_page,
        'sort': 'updated',
        'direction': 'desc'
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def display_repo_info(repos):
    for repo in repos:
        print(f"\nНазвание: {repo['name']}")
        print(f"Язык: {repo['language'] or 'Не указан'}")
        print(f"Звёзды: {repo['stargazers_count']}")
        print(f"Форки: {repo['forks_count']}")

def main():
    username = input("Введите имя пользователя GitHub: ")
    token = input("Введите ваш GitHub токен (или нажмите Enter для анонимного доступа): ").strip()
    
    if not token:
        print("\n[Предупреждение] Без токена лимит запросов сильно ограничен (60 в час)")
    
    all_repos = []
    page = 1
    total_stars = 0
    languages = {}
    
    try:
        while True:
            print(f"\nСтраница {page}:")
            repos = get_user_repos(username, token, page)
            
            if not repos:
                print("\nБольше нет репозиториев.")
                break
                
            display_repo_info(repos)
            
            # Собираем статистику
            for repo in repos:
                all_repos.append(repo)
                total_stars += repo['stargazers_count']
                
                lang = repo['language']
                if lang:
                    languages[lang] = languages.get(lang, 0) + 1
            
            # Проверяем, есть ли еще репозитории
            if len(repos) < 5:
                break
                
            choice = input("\nПоказать следующую страницу? (y/n): ").lower()
            if choice != 'y':
                break
                
            page += 1
            time.sleep(1)  # Задержка для избежания rate limiting
            
    except requests.exceptions.HTTPError as e:
        print(f"\nОшибка: {e}")
        if e.response.status_code == 404:
            print("Пользователь не найден.")
        elif e.response.status_code == 403:
            print("Превышен лимит запросов. Попробуйте позже или используйте токен.")
        return
    
    # Выводим общую статистику
    if all_repos:
        print("\n=== ОБЩАЯ СТАТИСТИКА ===")
        print(f"Всего репозиториев: {len(all_repos)}")
        
        if languages:
            most_common_lang = max(languages.items(), key=lambda x: x[1])
            print(f"Самый популярный язык: {most_common_lang[0]} ({most_common_lang[1]} репозиториев)")
        else:
            print("Языки не указаны ни в одном репозитории")
            
        print(f"Суммарное количество звёзд: {total_stars}")
    else:
        print("\nУ пользователя нет публичных репозиториев.")

if __name__ == "__main__":
    main()