from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

gpt_or_stable = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать ChatGPT 3.5", callback_data="chatGPT")],
        [
            InlineKeyboardButton(
                text="Выбрать Stable Diffusion", callback_data="stableDiffusion"
            )
        ],
    ]
)
