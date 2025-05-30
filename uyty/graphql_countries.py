import requests

url = "https://countries.trevorblades.com/"

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

def main():
    response = requests.post(url, json={"query": query})
    
    if response.status_code != 200:
        print("Ошибка:", response.status_code)
        return

    data = response.json()

    countries = data["data"]["countries"]

    print("=== Первые 10 стран ===")
    for country in countries[:10]:
        name = country["name"]
        code = country["code"]
        capital = country["capital"] or "нет данных"
        currency = country["currency"] or "нет данных"
        langs = [lang["name"] for lang in country["languages"] if lang["name"]]
        lang_list = ", ".join(langs) if langs else "нет данных"

        print(f"{name} ({code}) — столица: {capital}, валюта: {currency}, язык(и): {lang_list}")

    # Статистика
    total_countries = len(countries)
    currencies = set()
    language_counter = {}

    for country in countries:
        if country["currency"]:
            currencies.add(country["currency"])
        for lang in country["languages"]:
            lang_name = lang["name"]
            if lang_name:
                language_counter[lang_name] = language_counter.get(lang_name, 0) + 1

    top_languages = sorted(language_counter.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\n=== Статистика ===")
    print("Общее количество стран:", total_countries)
    print("Уникальных валют:", len(currencies))
    print("Топ-3 языка:")
    for lang, count in top_languages:
        print(f"- {lang}: {count} стран")

if __name__ == "__main__":
    main()
