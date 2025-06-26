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

# запрос на получение последних 100 issues из репозитория vscode, которым владеет microsoft
query = """
query {
  repository(owner: \"microsoft\", name: \"vscode\") {
    issues(last: 100, states: OPEN) {
      nodes {
        title
        createdAt
      }
    }
  }
}
"""

# отправляем POST-запрос
response = requests.post(GITHUB_API_URL, headers=headers, json={"query": query})
if response.status_code != 200:
    raise Exception(f"Ошибка при запросе к GitHub API: {response.status_code}")

# извлекаем из полученного ответа информацию о созданных issues
issues = response.json()['data']['repository']['issues']['nodes']

# преобразуем полученный список в датафрейм
df = pd.DataFrame(issues)

# преобразуем столбец createdAt в формат datetime
df['createdAt'] = pd.to_datetime(df['createdAt'])

# создаем столбец с часами, округляя вниз
df['hour'] = df['createdAt'].dt.floor('h')

# группируем данные и подсчитываем количество issues для каждого часа
issues_per_hour = df.groupby('hour').size().reset_index(name='count')

# строим линейный график для отображения количества созданных issues по часам в репозитории vscode
plt.figure(figsize=(12, 6))
plt.plot(issues_per_hour['hour'], issues_per_hour['count'], marker='o', linestyle='-')
plt.xlabel('Час')
plt.ylabel('Количество issues')
plt.title('Количество созданных issues по часам (репозиторий vscode)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()