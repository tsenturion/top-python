import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    response.encoding = 'windows-1251'  # важно для правильной кодировки

    if response.status_code != 200:
        print("Ошибка загрузки данных:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "xml")

    valutes = []
    for valute in soup.find_all("Valute"):
        val_id = valute.get("ID")
        num_code = valute.NumCode.text
        char_code = valute.CharCode.text
        name = valute.Name.text
        nominal = int(valute.Nominal.text)
        # Значение курса с запятой, заменяем на точку и преобразуем в float
        value = float(valute.Value.text.replace(',', '.'))

        valutes.append({
            "ID": val_id,
            "NumCode": num_code,
            "CharCode": char_code,
            "Name": name,
            "Nominal": nominal,
            "Value": value
        })

    # Отдельно курс доллара (USD)
    usd = next((v for v in valutes if v["CharCode"] == "USD"), None)

    # Сортируем по курсу Value по убыванию
    valutes_sorted = sorted(valutes, key=lambda x: x["Value"], reverse=True)

    print("Курсы валют ЦБ РФ на текущую дату:\n")
    for v in valutes_sorted:
        print(f'{v["ID"]}: NumCode={v["NumCode"]}, CharCode={v["CharCode"]}, '
              f'Name="{v["Name"]}", Nominal={v["Nominal"]}, Value={v["Value"]}')

    if usd:
        print(f"\nКурс доллара (USD): {usd['Value']} руб. за {usd['Nominal']} единиц")

if __name__ == "__main__":
    main()
