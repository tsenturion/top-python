import urllib.request
from xml.etree import ElementTree as ET
from decimal import Decimal

def get_currency_rates():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    
    try:
        
        with urllib.request.urlopen(url) as response:
            xml_data = response.read()
        
        
        root = ET.fromstring(xml_data)
        valutes = root.findall('Valute')
        
        currencies = []
        usd_rate = None
        
        for valute in valutes:
            currency = {
                'ID': valute.get('ID'),
                'NumCode': valute.find('NumCode').text,
                'CharCode': valute.find('CharCode').text,
                'Name': valute.find('Name').text,
                'Nominal': int(valute.find('Nominal').text),
                'Value': Decimal(valute.find('Value').text.replace(',', '.'))
            }
            currencies.append(currency)
            
            if currency['CharCode'] == 'USD':
                usd_rate = currency
        
        
        currencies.sort(key=lambda x: x['Value'], reverse=True)
        
        return currencies, usd_rate
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return None, None

def main():
    currencies, usd_rate = get_currency_rates()
    
    if not currencies:
        print("Не удалось получить данные о валютах")
        return
    
    print("Курсы валют ЦБ РФ (отсортированы по курсу):")
    print("-" * 70)
    print(f"{'Код':<8} {'Цифр.код':<8} {'Букв.код':<6} {'Номинал':<8} {'Курс':<10} Название")
    print("-" * 70)
    
    for currency in currencies:
        print(f"{currency['ID']:<8} {currency['NumCode']:<8} {currency['CharCode']:<6} "
              f"{currency['Nominal']:<8} {currency['Value']:<10} {currency['Name']}")
    
    if usd_rate:
        print("\nКурс доллара США (USD):")
        print(f"1 USD = {usd_rate['Value']} RUB (за {usd_rate['Nominal']} USD)")

if __name__ == "__main__":
    main()