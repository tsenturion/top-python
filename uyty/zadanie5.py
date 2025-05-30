import requests
from collections import Counter

url = "https://countries.trevorblades.com/"

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

def main():
    response = requests.post(url, json={"query": query})

    if response.status_code != 200:
        print("Ошибка запроса:", response.status_code)
        return

    data = response.json()["data"]["countries"]

    output = []

    print("🌍 Первые 10 стран:\n")
    output.append("🌍 Первые 10 стран:\n\n")
    for country in data[:10]:
        lang_names = [lang["name"] for lang in country["languages"] if lang["name"]]
        info = (
            f"Название: {country['name']}, Код: {country['code']}, "
            f"Столица: {country.get('capital', '-')}, "
            f"Валюта: {country.get('currency', '-')}, "
            f"Языки: {', '.join(lang_names) if lang_names else 'Нет данных'}"
        )
        print(info)
        output.append(info + "\n")

    # Статистика
    total_countries = len(data)
    unique_currencies = set()
    language_counter = Counter()

    for country in data:
        if country["currency"]:
            for curr in country["currency"].split(","):
                unique_currencies.add(curr.strip())

        for lang in country["languages"]:
            if lang["name"]:
                language_counter[lang["name"]] += 1

    stats = (
        f"\n📊 Статистика:\n"
        f"Всего стран: {total_countries}\n"
        f"Уникальных валют: {len(unique_currencies)}\n"
        f"Топ-3 языка:\n"
    )

    top_languages = language_counter.most_common(3)
    for lang, count in top_languages:
        stats += f"- {lang}: {count} стран\n"

    print(stats)
    output.append(stats)

    # Сохраняем в файл
    with open("graphql_countries.txt", "w", encoding="utf-8") as f:
        f.writelines(output)

    print("Результаты сохранены в 'graphql_countries.txt'.")

if __name__ == "__main__":
    main()
