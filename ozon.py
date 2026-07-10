from camoufox.sync_api import Camoufox
from pyvirtualdisplay import Display
import time

display = Display(visible=0, size=(1920, 1080))
display.start()



# Camoufox сам сгенерирует идеальные отпечатки реального пользователя
with Camoufox(
    headless=False,
    proxy={"server": "http://93.77.191.156:8118"}
) as browser:
    page = browser.new_page()
    page.goto("https://ozon.ru")
    while page.title() == "Antibot Challenge Page":
        time.sleep(1)
        
    print(page.title())
    page.wait_for_timeout(10000)

    display.stop()
