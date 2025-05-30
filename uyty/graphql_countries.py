import http.client
import json
from collections import Counter

def fetch_countries():
    conn = http.client.HTTPSConnection("countries.trevorblades.com")

    query = """
    {
      countries {
        code
        name
        capital
        currency
        languages {
          code
          name
        }
      }
    }
    """

    headers = {
        "Content-Type": "application/json"
    }

    body = json.dumps({"query": query})
    conn.request("POST", "/", body=body, headers=headers)
    response = conn.getresponse()

    if response.status != 200:
        print("Ошибка:", response.status, response.reason)
        print(response.read().decode())
        return []

    data = json.loads(response.read().decode())
    return data["data"]["countries"]

def main():
    countries = fetch_countries()
    if not countries:
        print("Не удалось получить данные.")
        return

    print("🔹 Первые 10 стран:")
    for country in countries[:10]:
        lang_names = [lang["name"] for lang in country.get("languages", []) if lang["name"]]
        print(f"{country['name']} ({country['code']})")
        print(f"  Столица: {country.get('capital')}")
        print(f"  Валюта: {country.get('currency')}")
        print(f"  Языки: {', '.join(lang_names)}")
        print()

    # Статистика
    total_countries = len(countries)
    all_currencies = set()
    all_languages = []

    for c in countries:
        if c.get("currency"):
            for cur in c["currency"].split(","):  # иногда бывает список через запятую
                all_currencies.add(cur.strip())

        all_languages.extend(lang["name"] for lang in c.get("languages", []) if lang["name"])

    lang_counter = Counter(all_languages)
    top_langs = lang_counter.most_common(3)

    print("📊 Статистика:")
    print(f"Всего стран: {total_countries}")
    print(f"Уникальных валют: {len(all_currencies)}")
    print("Топ-3 языка:")
    for lang, count in top_langs:
        print(f"  {lang}: {count}")

if __name__ == "__main__":
    main()
