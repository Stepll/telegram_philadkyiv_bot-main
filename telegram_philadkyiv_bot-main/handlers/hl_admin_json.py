from aiogram import types
from aiogram import Router

from aiogram.filters.command import Command
from filters.user_id_filter import UserFilter

from data import config
from mongo.messages import create_message

router = Router()

""" ADMINISTRATOR COMMAND """
# Надсилає id чату при команді головного адміністратора /json

@router.message(Command("json", prefix='!/'), UserFilter(user_id=config.administrator))
async def json(message: types.Message):
    await create_message(func='send_message', chat_id=message.chat.id, text=str(message.chat.id))