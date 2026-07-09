import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
}

print("Отправляю запрос к Ozon...")
response = requests.get("https://ozon.ru", headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    price_element = soup.find('span', {'data-testid': 'total-price'})
    if price_element:
        print("Цена:", price_element.text.strip())
    else:
        print("Код 200, но сработал Antibot Challenge (капча).")
else:
    print(f"Ошибка доступа. Код ответа: {response.status_code}")
