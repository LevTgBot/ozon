import asyncio  # Добавили для асинхронных пауз
from camoufox.async_api import AsyncCamoufox 
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup

async def price(url):
    display = Display(visible=0, size=(1920, 1080))
    display.start()

    try:
        # Camoufox генерирует отпечатки реального пользователя
        async with AsyncCamoufox(
            headless=False,
            proxy={"server": "http://93.77.191.156:8118"},
            geoip=True
        ) as browser:
            page = await browser.new_page()
            await page.goto(url)
            
            # Добавили await к page.title() и заменили time.sleep на асингулярный аналог
            while await page.title() == "Antibot Challenge Page":
                await asyncio.sleep(1)
            
            # Добавили await для печати заголовка
            print(await page.title())
            await asyncio.sleep(1)
            
            # Добавили await для получения HTML-кода
            html_content = await page.content()
            soup = BeautifulSoup(html_content, 'html.parser')
            
            elements = soup.find_all('span', class_='tsHeadline600Large')
            
            if elements:
                result_price = elements[0].text.strip()
                print("Цена:", result_price)
                return result_price
            else:
                print("Элемент с ценой не найден")
                return "Цена не найдена"
                
    finally:
        # Блок try/finally гарантирует, что виртуальный дисплей закроется 
        # и память не утечет, даже если внутри парсера произойдет ошибка
        display.stop()
