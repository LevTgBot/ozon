from camoufox.sync_api import Camoufox
from pyvirtualdisplay import Display
import time
from bs4 import BeautifulSoup

def price(url):
    display = Display(visible=0, size=(1920, 1080))
    display.start()



    # Camoufox сам сгенерирует идеальные отпечатки реального пользователя
    with Camoufox(
        headless=False,
        proxy={"server": "http://93.77.191.156:8118"},
        geoip=True
    ) as browser:
        page = browser.new_page()
        page.goto(url)
        while page.title() == "Antibot Challenge Page":
            time.sleep(1)
        
        print(page.title())
        time.sleep(1)
        soup = BeautifulSoup(page.content(), 'html.parser')
        elements = soup.find_all('span', class_='tsHeadline600Large')
        print("Цена:", elements[0].text)

        display.stop()
