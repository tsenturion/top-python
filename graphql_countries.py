import http.client
import json
from collections import Counter

# GraphQL-запрос для получения списка стран с необходимой информацией
query = """
{
  countries {
    name
    code
    capital
    currency
    languages {
      name
    }
  }
}
"""

# Отправка POST-запроса к API
conn = http.client.HTTPSConnection("countries.trevorblades.com")
headers = {'Content-Type': 'application/json'}
body = json.dumps({'query': query})
conn.request("POST", "/", body, headers)
response = conn.getresponse()
data = response.read()
conn.close()

# Обработка ответа
if response.status == 200:
    countries = json.loads(data)['data']['countries']
    
    # Заголовок таблицы
    print(f"{'Название страны':<25} {'Код':<6} {'Столица':<20} {'Валюта':<12} {'Языки'}")
    print("=" * 80)
    
    # Отображение первых 10 стран
    for country in countries[:10]:
        languages = ", ".join(lang['name'] for lang in country['languages']) or "—"
        capital = country['capital'] or "—"
        currency = country['currency'] or "—"
        print(f"{country['name']:<25} {country['code']:<6} {capital:<20} {currency:<12} {languages}")
    
    # Статистика
    total_countries = len(countries)
    currencies = [country['currency'] for country in countries if country['currency']]
    languages = [lang['name'] for country in countries for lang in country['languages']]
    
    unique_currencies = len(set(currencies))
    top_languages = Counter(languages).most_common(3)
    
    print("\n" + "=" * 40)
    print("Статистика по странам:")
    print(f"Общее количество стран: {total_countries}")
    print(f"Количество уникальных валют: {unique_currencies}")
    print("Топ-3 самых часто встречающихся языков:")
    for lang, count in top_languages:
        print(f"  {lang}: {count} раз")
else:
    print(f"Ошибка при запросе данных: HTTP {response.status}")