import requests
from bs4 import BeautifulSoup

def parse_float(value):
    return float(value.replace(',', '.'))

def main():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    response.encoding = 'windows-1251'
    soup = BeautifulSoup(response.text, "xml")

    currencies = []
    usd_value = None

    for valute in soup.find_all("Valute"):
        currency_id = valute.get("ID")
        num_code = valute.NumCode.text if valute.NumCode else None
        char_code = valute.CharCode.text if valute.CharCode else None
        name = valute.Name.text if valute.Name else None
        nominal = int(valute.Nominal.text) if valute.Nominal else None
        value = parse_float(valute.Value.text) if valute.Value else None

        currencies.append({
            "ID": currency_id,
            "NumCode": num_code,
            "CharCode": char_code,
            "Name": name,
            "Nominal": nominal,
            "Value": value
        })

        if char_code == "USD":
            usd_value = value

    # Оставим только валюты с корректным курсом
    currencies = [c for c in currencies if c["Value"] is not None]

    currencies.sort(key=lambda x: x["Value"], reverse=True)

    print("Валюты (отсортированы по курсу к рублю):\n")
    for cur in currencies:
        print(
            f"ID: {cur['ID']}, NumCode: {cur['NumCode']}, CharCode: {cur['CharCode']}, "
            f"Name: {cur['Name']}, Nominal: {cur['Nominal']}, Value: {cur['Value']}"
        )

    print("\nКурс доллара (USD) к рублю:", usd_value)

if __name__ == "__main__":
    main()
