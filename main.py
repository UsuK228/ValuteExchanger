import requests

print("\nКурс валюты к рублю\nBy UsuK\n")

valute_or_crypto = int(input("Обычная валюта или криптовалюта? (1 для обычной, 2 для криптовалюты): "))

if valute_or_crypto == 1:
    try:
        valute_charcode = input("Введите код валюты (USD, EUR, BYN...): ")
        valute_data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
        print(f"Курс {valute_data["Valute"][valute_charcode]["Name"]} ({valute_charcode}) к рублю: {valute_data["Valute"][valute_charcode]["Value"]}")
    except Exception as err:
        print(f"Ошибка: {err}")
elif valute_or_crypto == 2:
    try:
        crypto_charcode = input("Введите код криптовалюты (BTC, ETH, USDT): ")
        crypto_data = requests.get(f"https://rub.rate.sx/1{crypto_charcode}").text
        print(f"Курс {crypto_charcode} к рублю: {crypto_data}")
    except Exception as err:
        print(f"Ошибка: {err}")
else:
    print("Неверное число! Введите 1 или 2")