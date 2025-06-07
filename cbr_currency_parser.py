import urllib.request
import xml.etree.ElementTree as ET

def fetch_exchange_rates():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    with urllib.request.urlopen(url) as response:
        return response.read()

def parse_exchange_rates(xml_data):
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()
    valutes = []

    for valute in root.findall("Valute"):
        valute_data = {
            "ID": valute.get("ID"),
            "NumCode": valute.find("NumCode").text,
            "CharCode": valute.find("CharCode").text,
            "Name": valute.find("Name").text,
            "Nominal": int(valute.find("Nominal").text),
            "Value": float(valute.find("Value").text.replace(",", ".")),
        }
        valutes.append(valute_data)

    return valutes

def display_exchange_rates(valutes):
    sorted_valutes = sorted(valutes, key=lambda x: x["Value"], reverse=True)

    print(f"{'ID':<10} {'NumCode':<6} {'CharCode':<3} {'Name':<30} {'Nominal':<8} {'Value':<10}")
    print("-" * 70)
    for valute in sorted_valutes[:10]:
        print(f"{valute['ID']:<10} {valute['NumCode']:<6} {valute['CharCode']:<3} {valute['Name']:<30} {valute['Nominal']:<8} {valute['Value']:<10.4f}")

    usd_rate = next((v for v in sorted_valutes if v["CharCode"] == "USD"), None)
    if usd_rate:
        print(f"\nКурс доллара США (USD): {usd_rate['Value'] / usd_rate['Nominal']:.4f} руб. за 1 USD")
    else:
        print("\nКурс доллара США (USD) не найден.")

def main():
    try:
        xml_data = fetch_exchange_rates()
        valutes = parse_exchange_rates(xml_data)
        display_exchange_rates(valutes)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()