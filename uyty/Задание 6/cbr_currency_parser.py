import requests
from bs4 import BeautifulSoup

# 1. Получаем XML
url = "https://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)
xml_data = response.content

# 2. Парсим XML
soup = BeautifulSoup(xml_data, "xml")
valutes = soup.find_all("Valute")

# 3. Собираем данные
currencies = []
for valute in valutes:
    currency = {
        "ID": valute.get("ID"),
        "NumCode": valute.NumCode.text,
        "CharCode": valute.CharCode.text,
        "Name": valute.Name.text,
        "Nominal": int(valute.Nominal.text),
        "Value": float(valute.Value.text.replace(",", "."))
    }
    currencies.append(currency)

# 4. Выводим данные по каждой валюте
print("Курсы валют на сегодня:")
for currency in currencies:
    print(f"ID: {currency['ID']}, NumCode: {currency['NumCode']}, CharCode: {currency['CharCode']}, "
          f"Name: {currency['Name']}, Nominal: {currency['Nominal']}, Value: {currency['Value']}")

# 5. Курс доллара
usd = next((c for c in currencies if c["CharCode"] == "USD"), None)
if usd:
    print("\nКурс доллара (USD):")
    print(f"{usd['Nominal']} {usd['Name']} = {usd['Value']} RUB")
else:
    print("Курс доллара не найден.")

# 6. Сортировка по курсу
sorted_currencies = sorted(currencies, key=lambda x: x["Value"], reverse=True)
print("\nВалюты, отсортированные по курсу (по убыванию):")
for currency in sorted_currencies:
    print(f"{currency['CharCode']}: {currency['Value']} RUB")
