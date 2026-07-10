import asyncio
from camoufox.async_api import AsyncCamoufox 
from pyvirtualdisplay import Display

# Выносим дисплей и браузер в глобальные переменные
display = None
browser_instance = None

async def init_browser():
    """Запускаем браузер один раз при старте бота"""
    global display, browser_instance
    if browser_instance is None:
        display = Display(visible=0, size=(1920, 1080))
        display.start()
        
        # Запускаем один долгоживущий процесс браузера
        browser_instance = await AsyncCamoufox(
            headless=False,
            proxy={"server": "http://93.77.191.156:8118"},
            geoip=True
        ).__aenter__() # Ручной запуск асинхронного контекстного менеджера

async def close_browser():
    """Закрываем браузер при выключении бота"""
    global display, browser_instance
    if browser_instance:
        await browser_instance.close()
    if display:
        display.stop()

async def price(url):
    global browser_instance
    # На всякий случай проверяем, запущен ли браузер
    if not browser_instance:
        await init_browser()
        
    # Открываем только ОДНУ новую вкладку (это происходит мгновенно)
    page = await browser_instance.new_page()
    
    try:
        # Ускоряем загрузку: блокируем картинки, шрифты и медиа
        await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "font", "media", "stylesheet"] else route.continue_())
        
        # Переходим на сайт (с таймаутом 20 секунд, чтобы не ждать вечно)
        await page.goto(url)
        
        # Быстрая проверка на антибот
        while await page.title() == "Antibot Challenge Page":
            await asyncio.sleep(0.5)
            
        # Используем встроенный быстрый локатор Playwright вместо BeautifulSoup
        # Он сам дождется появления элемента на странице
        price_element = page.locator('span.tsHeadline600Large').first
        
        # Ждем элемент максимум 5 секунд
        await price_element.wait_for(state="attached", timeout=5000)
        
        result_price = await price_element.text_content()
        return result_price.strip()
        
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return "Не удалось получить цену"
        
    finally:
        # Обязательно закрываем вкладку, чтобы не копилась память
        await page.close()
