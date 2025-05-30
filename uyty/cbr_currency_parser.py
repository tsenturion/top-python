import http.client
import xml.etree.ElementTree as ET

def fetch_cbr_xml():
    conn = http.client.HTTPSConnection("www.cbr.ru")
    conn.request("GET", "/scripts/XML_daily.asp")
    response = conn.getresponse()
    if response.status != 200:
        print("Ошибка при получении XML:", response.status)
        return None
    return response.read()

def parse_currencies(xml_data):
    root = ET.fromstring(xml_data)
    currencies = []
    usd_value = None

    for valute in root.findall("Valute"):
        char_code = valute.find("CharCode").text
        currency = {
            "ID": valute.attrib.get("ID"),
            "NumCode": valute.find("NumCode").text,
            "CharCode": char_code,
            "Name": valute.find("Name").text,
            "Nominal": int(valute.find("Nominal").text),
            "Value": float(valute.find("Value").text.replace(",", "."))
        }
        currencies.append(currency)

        if char_code == "USD":
            usd_value = currency["Value"]

    currencies.sort(key=lambda x: x["Value"], reverse=True)
    return currencies, usd_value

def display_currencies(currencies):
    for c in currencies:
        print(f"[{c['ID']}] {c['CharCode']} ({c['NumCode']}): {c['Name']}")
        print(f"  Номинал: {c['Nominal']}, Курс: {c['Value']} руб.")
        print()

def main():
    xml_data = fetch_cbr_xml()
    if not xml_data:
        return

    currencies, usd = parse_currencies(xml_data)

    print("📊 Курсы валют ЦБ РФ (отсортировано по курсу):")
    print("-" * 50)
    display_currencies(currencies)
    print("-" * 50)
    print(f"💵 Курс доллара США (USD): {usd} руб.")

if __name__ == "__main__":
    main()
