from aiogram import Router
from aiogram.types import Message
from app.telebot.handlers.users_state_controller import UsersStateController
from app.telebot.shemas.user_states import UserState


router = Router()


@router.message()
async def main_message_handler(message: Message):
    if not message.from_user:
        return
    match UsersStateController().get_user_state(message.from_user.id):
        case UserState.START:
            await message.answer("""Привет! Я бот для подсчета калорий.
                Чтобы начать, просто введи назнвание блюда/продукта.""")
        case UserState.ADD_PRODUCT:
            await message.answer("Введите название продукта:")
            
        case UserState.ADD_PRODUCT_AMOUNT:
            await message.answer("Введите количество продукта:")
        case UserState.ADD_PRODUCT_DATE:
            await message.answer("Введите дату:")
        case _: 
            await message.answer("Я не знаю, что делать с этим сообщением.")