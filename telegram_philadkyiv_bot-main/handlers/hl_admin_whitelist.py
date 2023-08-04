from aiogram import types
from aiogram import Router

from aiogram.filters.command import Command
from filters.user_id_filter import UserFilter

from data import config


from mongo.messages import create_message

router = Router()

""" ADMINISTRATOR COMMAND """

# Активує та деактивує команду /whitelist
@router.message(Command("whitelist", prefix='!/'), UserFilter(user_id=config.administrator))
async def whitelist(message: types.Message):
    if config.WHITELIST:
        config.WHITELIST = False
        await create_message(func='send_message', chat_id=message.chat.id, text='🛡❌ Whitelist вимкнено')
    else:
        config.WHITELIST = True
        await create_message(func='send_message', chat_id=message.chat.id, text='🛡✅ Whitelist увімкнено')
        