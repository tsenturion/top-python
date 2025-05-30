import urllib.request
import json
from collections import Counter

def main():
    url = "https://countries.trevorblades.com/"
    query = '''
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
    '''
    data = json.dumps({"query": query}).encode('utf-8')
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'  # Добавили User-Agent
    }

    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req) as response:
        result = json.load(response)

    countries = result['data']['countries']

    print("Первые 10 стран:")
    for country in countries[:10]:
        langs = ', '.join(lang['name'] for lang in country['languages'] if lang['name'])
        print(f"{country['name']} | Код: {country['code']} | Столица: {country.get('capital','-')} | Валюта: {country.get('currency','-')} | Языки: {langs}")

    all_currencies = set()
    all_languages = []
    for country in countries:
        if country.get("currency"):
            all_currencies.update(map(str.strip, country["currency"].split(',')))
        for lang in country['languages']:
            if lang['name']:
                all_languages.append(lang['name'])

    print("\n--- Статистика ---")
    print(f"Общее количество стран: {len(countries)}")
    print(f"Количество уникальных валют: {len(all_currencies)}")
    print("Топ-3 самых часто встречающихся языков:")
    for lang, count in Counter(all_languages).most_common(3):
        print(f"{lang}: {count}")

if __name__ == "__main__":
    main()
