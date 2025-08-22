from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
from config import BOT_TOKEN
from app.telebot.handlers.open_food_handler import open_food_handler, product_callback

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Hello, world!")

dp.message.register(open_food_handler)
dp.callback_query.register(product_callback, lambda c: c.data.startswith("product_"))

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
