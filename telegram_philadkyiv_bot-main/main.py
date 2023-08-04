import asyncio
import logging
import inspect

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import FSInputFile

from handlers import *

from data import config

from dispatcher import dp, bot
from mongo.messages import create_message
from logger import exceptions

import time
import datetime


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    for admin_id in config.admin_ids:
        try:
            me = await bot.get_me()
            await create_message(func='send_message', chat_id=admin_id, text=f"🟩 Бот @{me.username} увімкнений")
        except TelegramBadRequest:
            await exceptions(f'TelegramBadRequest: chat_id {str(admin_id)} недоступний в {inspect.stack()[0][3]} {inspect.stack()[0][1]}')


async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    downtime = time.time() - uptime
    time_format = str(datetime.timedelta(seconds = downtime))

    try:
        if config.SENDLOG == True:
            file_id = FSInputFile("py_log.log")
            await bot.send_document(chat_id=config.administrator, document=file_id)
    except Exception as e:
        print(e)

    for admin_id in config.admin_ids:
        try:
            me = await bot.get_me()
            await create_message(func='send_message', chat_id=admin_id, text=f"🟥 Бот @{me.username} вимкнений. " + str(time_format))
        except TelegramBadRequest:
            await exceptions(f'TelegramBadRequest: chat_id {str(admin_id)} недоступний в {inspect.stack()[0][3]} {inspect.stack()[0][1]}')


async def main():
    dp.include_router(hl_start.router)  
    dp.include_router(hl_ban.router)
    dp.include_router(hl_admin_json.router)
    dp.include_router(hl_admin_anonquest.router)
    dp.include_router(hl_admin_whitelist.router)
    # dp.include_router(hl_test.router) 

    dp.include_router(hl_answer.router)     # Тримати в кінці списку
    dp.include_router(hl_private.router)    # Тримати в кінці списку

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot)


if __name__ == "__main__":
    uptime = time.time()
    
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")
    
    asyncio.run(main())
