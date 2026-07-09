from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )

    page = context.new_page()
    print("Открываю Ozon...")
    page.goto("https://www.ozon.ru/product/koshachya-myata-sharik-igrushki-dlya-koshek-3168418801/", wait_until="domcontentloaded")
    while page.title() == "Antibot Challenge Page":
        time.sleep(1)

    time.sleep(1)
    soup = BeautifulSoup(page.content(), 'html.parser')
    elements = soup.find_all('span', class_='tsHeadline600Large')
    print("Цена:", elements[0].text)
    browser.close()
