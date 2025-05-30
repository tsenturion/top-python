import requests
from collections import Counter
url_countries = 'https://countries.trevorblades.com/'

query = """
{
  countries {
    name
    code
    capital
    currency
    languages
    {
      name
    }
  }
}
"""
response = requests.post(url=url_countries, json={'query': query})
response.json()
if response.status_code == 200:
    data = response.json()
    countries = data['data']['countries']
    for country in data['data']['countries'][:10]:
        print(f"Страна: {country['name']}")
        print(f"Code: {country['code']}")
        print(f"Capital: {country['capital']}")
        print(f"Валюта: {country['currency']}")
        print(f"Языки: {[lang['name'] for lang in country['languages']]}")
    total_countries = len(countries)
    print(f"\nОбщее количество стран: {total_countries}")
    
    # Количество уникальных валют (исключаем None/пустые значения)
    currencies = [c['currency'] for c in countries if c['currency']]
    unique_currencies = len(set(currencies))
    print(f"Количество уникальных валют: {unique_currencies}")
    
    # Топ-3 самых часто встречающихся языков
    all_languages = []
    for country in countries:
        all_languages.extend(lang['name'] for lang in country['languages'])
    
    language_counter = Counter(all_languages)
    top_languages = language_counter.most_common(3)
    
    print("\nТоп-3 самых часто встречающихся языков:")
    for lang, count in top_languages:
        print(f"{lang}: {count} стран")
    
else:
    print("ошибка при выполнении запроса", response.status_code)