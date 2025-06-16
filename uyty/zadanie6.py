import requests
from bs4 import BeautifulSoup

url = "https://www.cbr.ru/scripts/XML_daily.asp"

def parse_float(value_str):
    return float(value_str.replace(',', '.'))

def get_text_safe(tag, tag_name):
    t = tag.find(tag_name)
    return t.text if t else None

def main():
    response = requests.get(url)
    response.encoding = 'windows-1251'  # Кодировка ЦБ РФ

    if response.status_code != 200:
        print("Ошибка загрузки:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "xml")
    valutes = soup.find_all("Valute")

    currency_data = []
    usd_value = None

    for valute in valutes:
        valute_id = valute.get("ID", "N/A")
        num_code = get_text_safe(valute, "NumCode") or "N/A"
        char_code = get_text_safe(valute, "CharCode") or "N/A"
        name = get_text_safe(valute, "Name") or "N/A"
        nominal_str = get_text_safe(valute, "Nominal") or "1"
        value_str = get_text_safe(valute, "Value")

        try:
            nominal = int(nominal_str)
        except ValueError:
            nominal = 1

        if value_str:
            value = parse_float(value_str)
        else:
            value = 0.0

        currency_data.append({
            "ID": valute_id,
            "NumCode": num_code,
            "CharCode": char_code,
            "Name": name,
            "Nominal": nominal,
            "Value": value
        })

        if char_code == "USD":
            usd_value = value

    # Сортировка по курсу по убыванию
    currency_data.sort(key=lambda x: x["Value"], reverse=True)

    output = []

    print("📦 Курсы валют:\n")
    output.append("📦 Курсы валют:\n\n")
    for c in currency_data:
        info = (f"ID: {c['ID']}, NumCode: {c['NumCode']}, CharCode: {c['CharCode']}, "
                f"Name: {c['Name']}, Nominal: {c['Nominal']}, Value: {c['Value']} руб.")
        print(info)
        output.append(info + "\n")

    # Отдельно курс доллара
    if usd_value is not None:
        usd_info = f"\n💵 Курс доллара (USD): {usd_value} руб.\n"
        print(usd_info)
        output.append(usd_info)
    else:
        print("\n💵 Курс доллара (USD) не найден.\n")
        output.append("\n💵 Курс доллара (USD) не найден.\n")

    # Сохранение в файл
    with open("cbr_currency_parser.txt", "w", encoding="utf-8") as f:
        f.writelines(output)

    print("Результаты сохранены в 'cbr_currency_parser.txt'.")

if __name__ == "__main__":
    main()
