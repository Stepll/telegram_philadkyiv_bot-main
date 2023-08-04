from aiogram import types
from aiogram import Router

from aiogram.filters.command import Command
from filters.chat_type_filter import ChatTypeFilter

from mongo.messages import create_message
from mongo.users import check_user

router = Router()

""" 
    ВИМКНЕНО 
"""
# Надсилає список команд при команді /help
@router.message(Command('help', prefix='!/'), ChatTypeFilter(chat_type=["private"]))
async def help(message: types.Message):
    await check_user(message)
    await create_message(func='send_message', chat_id=message.chat.id, text="help")