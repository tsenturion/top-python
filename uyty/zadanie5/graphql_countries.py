import requests
from collections import Counter

url = "https://countries.trevorblades.com/"

query = """
{
  countries {
    name
    code
    capital
    currency
    languages {
      code
      name
    }
  }
}
"""

response = requests.post(url, json={'query': query})
data = response.json()

if 'data' not in data:
    print("Ошибка! Нет данных.")
    exit()

countries = data["data"]["countries"]

# Отобразить первые 10 стран
print("Первые 10 стран:")
for country in countries[:10]:
    langs = ", ".join(lang['name'] for lang in country['languages'] if lang['name'])
    print(f"{country['name']} (код: {country['code']}), столица: {country.get('capital')}, валюта: {country.get('currency')}, языки: {langs}")

# Статистика
total_countries = len(countries)

# Количество уникальных валют
all_currencies = set()
for country in countries:
    # иногда валюта может быть в формате "USD,EUR"
    if country.get('currency'):
        for cur in country['currency'].split(','):
            all_currencies.add(cur.strip())

unique_currencies_count = len([c for c in all_currencies if c])

# Топ-3 самых частых языка
all_langs = []
for country in countries:
    all_langs.extend(lang['name'] for lang in country['languages'] if lang['name'])

top_3_langs = Counter(all_langs).most_common(3)

print("\nСтатистика:")
print(f"Общее количество стран: {total_countries}")
print(f"Количество уникальных валют: {unique_currencies_count}")
print("Топ-3 самых частых языка:")
for lang, count in top_3_langs:
    print(f"{lang}: {count} стран")

