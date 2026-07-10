from os import getenv
import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.types import (
    Message
)

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Введи ссылку на товар.")

@router.message()
async def menu(message: Message):
    await message.answer(f"Ищу товар:{message}")


dp = Dispatcher()
dp.include_routers(router)


async def main():
    bot = Bot(token=TOKEN)

    print("Start")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
