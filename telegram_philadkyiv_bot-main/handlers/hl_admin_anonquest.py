from aiogram import types
from aiogram import Router

from aiogram.filters.command import Command
from filters.user_id_filter import UserFilter

from data import config
from mongo.messages import create_message

router = Router()

""" ADMINISTRATOR COMMAND """
# Змінює питання з анонімних на неанонімні і навпаки командою /anonquest

@router.message(Command("anonquest", prefix='!/'), UserFilter(user_id=config.administrator))
async def anonquest(message: types.Message):
    if config.ANONQUEST:
        config.ANONQUEST = False
        await create_message(func='send_message', chat_id=message.chat.id, text='💬❌ Анонімні питання вимкнені')
    else:
        config.ANONQUEST = True
        await create_message(func='send_message', chat_id=message.chat.id, text='💬✅ Анонімні питання увімкнені')
        