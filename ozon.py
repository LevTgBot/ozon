from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth 
import time
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920, 1080))
display.start()

stealth = Stealth()

with sync_playwright() as p:
    stealth.use_sync(p)
    browser = stealth_p.chromium.launch(
    headless=False,
    proxy={
        "server": "http://93.77.191.156:8118"
    },
    args=[
        "--disable-blink-features=AutomationControlled",
        "--no-sandbox",             # Обязательно для root в Linux
        "--disable-setuid-sandbox"  # Дополнительная изоляция для Linux
    ]
    )
    
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )
    
    page = browser.new_page()
    print("Открываю Ozon...")
    page.goto("https://www.ozon.ru/product/koshachya-myata-sharik-igrushki-dlya-koshek-3168418801/", wait_until="domcontentloaded")
    while page.title() == "Antibot Challenge Page":
        time.sleep(1)
    
    time.sleep(1)
    #soup = BeautifulSoup(page.content(), 'html.parser')
    #elements = soup.find_all('span', class_='tsHeadline600Large')
    print(page.content())
    browser.close()
    display.stop()
