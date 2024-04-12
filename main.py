from aiogram import Bot, Dispatcher
from bot.core.utils import get_token
from bot.core.handlers import routers

import logging
import asyncio

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


async def main():
    bot = Bot(get_token("TG_Bot"), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(*routers)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
