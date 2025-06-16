import urllib.request
import urllib.error
import json
from collections import Counter

GRAPHQL_QUERY = """
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

def send_graphql_request():
    try:
        req = urllib.request.Request(
            url="https://countries.trevorblades.com/",
            data=json.dumps({'query': GRAPHQL_QUERY}).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'PythonScript'
            },
            method='POST'
        )
        
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8')).get('data', {}).get('countries', [])
            
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        return None

def main():
    print("Запрашиваю данные о странах...")
    countries = send_graphql_request()
    
    if not countries:
        print("Не удалось получить данные")
        return
    
    
    print("\nПервые 10 стран:")
    for i, country in enumerate(countries[:10], 1):
        print(f"\n{i}. {country['name']} ({country['code']})")
        print(f"   Столица: {country.get('capital', 'нет данных')}")
        print(f"   Валюта: {country.get('currency', 'нет данных')}")
        langs = [lang['name'] for lang in country['languages']] if country['languages'] else ['нет данных']
        print(f"   Языки: {', '.join(langs)}")
    
    
    currencies = {c.get('currency') for c in countries if c.get('currency')}
    languages = [lang['name'] for c in countries for lang in c.get('languages', [])]
    
    print("\nСтатистика:")
    print(f"Всего стран: {len(countries)}")
    print(f"Уникальных валют: {len(currencies)}")
    print("Топ-3 языка:")
    for lang, count in Counter(languages).most_common(3):
        print(f"  {lang}: {count}")

if __name__ == "__main__":
    main()