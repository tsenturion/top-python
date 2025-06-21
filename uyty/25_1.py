# подключаем необходимые библиотеки
import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL для получения данных о всех ТВ-шоу со страницы с индексом 0
url = "https://api.tvmaze.com/shows?page=0"

# отправляем GET-запрос и получаем ответ в формате JSON
response = requests.get(url)
data = response.json()

# преобразуем JSON в список
shows_list = list(data)

# выводим на экран названия всех шоу
print("Названия всех шоу:")
for show in shows_list:
    print(show['name'])

# создаем DataFrame на основании полученного списка
df = pd.DataFrame(shows_list)

# выводим общую информацию о датафрейме
print("Информация о DataFrame:")
print(df.info())

# создаем серию с годами выхода всех шоу
# преобразуем 'premiered' в год, если значение не None
df['premiere_year'] = pd.to_datetime(df['premiered'], errors='coerce').dt.year

# строим гистограмму с распределением шоу по годам премьеры
plt.figure(figsize=(12, 6))
df['premiere_year'].dropna().astype(int).value_counts().sort_index().plot(kind='bar')
plt.title('Распределение ТВ-шоу по годам премьеры')
plt.xlabel('Год премьеры')
plt.ylabel('Количество шоу')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
