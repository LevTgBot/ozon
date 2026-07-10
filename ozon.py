from camoufox.sync_api import Camoufox
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1920, 1080))
display.start()



# Camoufox сам сгенерирует идеальные отпечатки реального пользователя
with Camoufox(
    headless=False,
    proxy={"server": "http://ip:port"},
    timezone="Europe/Moscow", 
    locale="ru-RU"
) as browser:
    page = browser.new_page()
    page.goto("https://ozon.ru")

    print(page.title())
    page.wait_for_timeout(10000)

    display.stop()
