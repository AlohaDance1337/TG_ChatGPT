from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "stableDiffusion")
async def dialog(call: CallbackQuery):
    await call.message.answer(text="Вы выбрали Stable Diffusion")
