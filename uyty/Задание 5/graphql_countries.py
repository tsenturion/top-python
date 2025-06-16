import requests
from collections import Counter

query = """
{
  countries {
    code
    name
    capital
    currency
    languages {
      name
    }
  }
}
"""

url = "https://countries.trevorblades.com/"
response = requests.post(url, json={'query': query})
data = response.json()

countries = data['data']['countries']

print("Первые 10 стран:")
for country in countries[:10]:
    langs = [lang['name'] for lang in country['languages']]
    print(f"{country['name']} ({country['code']}) | Столица: {country['capital']} | Валюта: {country['currency']} | Языки: {', '.join(langs)}")

# Статистика
total_countries = len(countries)

unique_currencies = set()
for country in countries:
    if country['currency']:
        for curr in country['currency'].split(','):
            unique_currencies.add(curr.strip())

all_languages = []
for country in countries:
    for lang in country['languages']:
        if lang['name']:
            all_languages.append(lang['name'])

top_languages = Counter(all_languages).most_common(3)

print("\nСтатистика:")
print(f"Общее количество стран: {total_countries}")
print(f"Количество уникальных валют: {len(unique_currencies)}")
print("Топ-3 самых популярных языка:")
for lang, count in top_languages:
    print(f"{lang}: {count}")
