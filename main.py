from configparser import Error
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
from config import BOT_TOKEN
from app.telebot.handlers.open_food_handler import open_food_handler, product_callback
from app.telebot.keyboards.products_list_keyboard import get_report_keyboard
from aiogram import F

if BOT_TOKEN:
    bot = Bot(token=BOT_TOKEN)
else:
    raise Error("BOT_TOKEN not found")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Hello, world!", reply_markup=get_report_keyboard())


@dp.message(F.text == "📊 Отчет за день")
async def report_command(message: Message):
    await message.answer("Отчет за день", reply_markup=get_report_keyboard())


dp.message.register(open_food_handler)
dp.callback_query.register(product_callback, lambda c: c.data.startswith("product_"))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
