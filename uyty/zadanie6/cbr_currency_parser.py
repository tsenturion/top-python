import requests
import xml.etree.ElementTree as ET

url = "https://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)
response.encoding = "windows-1251"

root = ET.fromstring(response.text)

currencies = []
usd_value = None

for valute in root.findall("Valute"):
    id_ = valute.get("ID")
    num_code = valute.find("NumCode").text
    char_code = valute.find("CharCode").text
    name = valute.find("Name").text
    nominal = int(valute.find("Nominal").text.replace(",", "."))
    value = float(valute.find("Value").text.replace(",", "."))

    currency_info = {
        "ID": id_,
        "NumCode": num_code,
        "CharCode": char_code,
        "Name": name,
        "Nominal": nominal,
        "Value": value
    }

    currencies.append(currency_info)

    if char_code == "USD":
        usd_value = value

# Сортируем по убыванию курса
currencies.sort(key=lambda x: x["Value"], reverse=True)

# Вывод всех валют
print("Курсы валют:")
for c in currencies:
    print(f"{c['ID']} | {c['NumCode']} | {c['CharCode']} | {c['Name']} | {c['Nominal']} | {c['Value']}")

print("\nКурс доллара (USD):")
if usd_value is not None:
    print(f"{usd_value} рублей за 1 доллар США")
else:
    print("USD не найден!")
