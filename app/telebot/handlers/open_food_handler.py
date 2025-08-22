from aiogram.types import Message, CallbackQuery
from app.open_food_app.calories_service import CaloriesService
from app.telebot.keyboards.products_list_keyboard import get_products_list_keyboard

user_products = {}


async def open_food_handler(message: Message):
    product_name = message.text
    if message.from_user.id in user_products:
        await calculate_calories(message)
        return
    await find_products(message, product_name)


async def find_products(message: Message, product_name: str) -> None:
    products = await CaloriesService().get_products_by_name(product_name)
    if products:
        await message.answer(
            "Найдены продукты:", reply_markup=get_products_list_keyboard(products)
        )
    else:
        await message.answer("Продукты не найдены")


async def calculate_calories(message: Message) -> None:
    try:
        amount = float(message.text)
    except ValueError:
        await message.answer("Введите число")
        return
    
    product = user_products[message.from_user.id]
    calories = CaloriesService.calculate_calories(product, amount)
    fat = CaloriesService.calculate_fat(product, amount)
    carbohydrates = CaloriesService.calculate_carbohydrates(product, amount)
    protein = CaloriesService.calculate_protein(product, amount)
    
    await message.answer(
        f"Калории: {calories} ккал\nЖиры: {fat} г\nУглеводы: {carbohydrates} г\nБелки: {protein} г"
    )
    del user_products[message.from_user.id]


async def product_callback(callback: CallbackQuery):
    try:
        product_uuid = callback.data.split("_")[1]
        
        # Получаем продукт по UUID
        product = await CaloriesService().get_product_by_uuid(product_uuid)  # Нужно реализовать поиск по UUID
        if product:
            user_products[callback.from_user.id] = product
            await callback.message.answer("Введите потребленное количество продукта в граммах")
        else:
            await callback.message.answer("Продукт не найден")
            
    except Exception as e:
        await callback.message.answer(f"Ошибка: {str(e)}")
    
    await callback.answer()
