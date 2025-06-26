import requests
import xml.etree.ElementTree as ET

URL = "https://www.cbr.ru/scripts/XML_daily.asp"
OUTPUT_FILE = "cbr_currency_parser.txt"

def fetch_and_parse():
    response = requests.get(URL)
    response.encoding = 'windows-1251'
    root = ET.fromstring(response.text)
    return root.findall('Valute')

def parse_valutes(valute_elements):
    valutes = []

    for valute in valute_elements:
        valute_data = {
            'ID': valute.attrib['ID'],
            'NumCode': valute.find('NumCode').text,
            'CharCode': valute.find('CharCode').text,
            'Name': valute.find('Name').text,
            'Nominal': int(valute.find('Nominal').text),
            'Value': float(valute.find('Value').text.replace(',', '.')),
        }
        valutes.append(valute_data)

    return valutes

def format_valute(v):
    return (
        f"ID: {v['ID']}\n"
        f"NumCode: {v['NumCode']}\n"
        f"CharCode: {v['CharCode']}\n"
        f"Name: {v['Name']}\n"
        f"Nominal: {v['Nominal']}\n"
        f"Value: {v['Value']} руб.\n"
        + "-" * 40 + "\n"
    )

def main():
    valute_elements = fetch_and_parse()
    valutes = parse_valutes(valute_elements)

    usd = next((v for v in valutes if v['CharCode'] == 'USD'), None)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        if usd:
            f.write(f"Курс доллара (USD): {usd['Value']} руб. за {usd['Nominal']} {usd['CharCode']}\n\n")
        sorted_valutes = sorted(valutes, key=lambda x: x['Value'], reverse=True)

        f.write("Валюты, отсортированные по курсу к рублю (по убыванию):\n\n")
        for v in sorted_valutes:
            f.write(format_valute(v))

    print(f"Данные успешно сохранены в файл {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
