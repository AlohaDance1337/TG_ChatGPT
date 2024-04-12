from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, F
from bot.core.keybuttons.inline import gpt_or_stable

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        text=f"Привет, <b>{message.from_user.username}</b>. Ты запустил бота, которы поможет тебе ответить на твои вопросы. Ты можешь спросить у него любой вопрос(в рамках разумного). Что ты выберешь?",
        reply_markup=gpt_or_stable,
    )
