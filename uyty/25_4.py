# подключаем необходимые библиотеки
import requests
import pandas as pd
import matplotlib.pyplot as plt

# персональный токен GitHub
GITHUB_TOKEN = "token here" 
# базовый адрес для GraphQL-запросов к GitHub
GITHUB_API_URL = "https://api.github.com/graphql"

# заголовки запроса
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

# список кортежей (владелец, имя репозитория), для которых нужно получить число звезд
repos = [
    ("pallets", "flask"),
    ("django", "django"),
    ("numpy", "numpy"),
    ("pandas-dev", "pandas"),
    ("tiangolo", "fastapi")
]

# шаблон запроса GraphQL
query_template = """
query {{
  repository(owner: \"{owner}\", name: \"{name}\") {{
    name
    owner {{ login }}
    stargazerCount
  }}
}}
"""

# получаем данные по каждому репозиторию
data = []
for owner, name in repos:
    query = query_template.format(owner=owner, name=name)
    response = requests.post(GITHUB_API_URL, headers=headers, json={"query": query})
    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе к GitHub API: {response.status_code}")
    result = response.json()
    repo_info = result['data']['repository']
    data.append({
        "owner": repo_info['owner']['login'],
        "repository": repo_info['name'],
        "stars": repo_info['stargazerCount']
    })

# формируем DataFrame на основании списка с данными о репозиториях
df = pd.DataFrame(data)

# строим столбчатую диаграмму для отображения количества звезд популярных репозиториев GitHub
plt.figure(figsize=(10, 6))
plt.bar(df['repository'], df['stars'], color='orange')
plt.xlabel('Репозиторий')
plt.ylabel('Количество звезд')
plt.title('Количество звезд популярных репозиториев GitHub')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
