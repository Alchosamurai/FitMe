from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from app.open_food_app.shemas.open_food_facts_shemas import OpenFoodFactsProduct


def get_products_list_keyboard(
    products: list[OpenFoodFactsProduct],
) -> InlineKeyboardMarkup:
    buttons = []
    for product in products:
        callback_data = f"product_{product.uuid}"

        # Проверяем длину callback_data (Telegram ограничивает до 64 байт)
        if len(callback_data.encode("utf-8")) > 64:
            # Если слишком длинный, используем только UUID
            callback_data = product.uuid[:50]  # Оставляем только первые 50 символов

        buttons.append(
            [InlineKeyboardButton(text=str(product), callback_data=callback_data)]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_report_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Отчет за день")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )