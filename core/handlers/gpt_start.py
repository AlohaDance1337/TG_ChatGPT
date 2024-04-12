from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.core.types.states import GptState

router = Router()


@router.callback_query(F.data == "chatGPT")
async def dialog(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        text="Вы выбрали ChatGPT 3.5. Что вы бы хотели спросить у бота?"
    )
    await state.set_state(GptState.message_to_gpt)


@router.message(GptState.message_to_gpt, F.text)
async def message(message: Message):
    await message.answer(text=f"Вы написали:{message.text}")
