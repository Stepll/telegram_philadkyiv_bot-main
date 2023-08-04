from aiogram import types
from aiogram import Router

from filters.chat_type_filter import ChatTypeFilter
from aiogram.filters.command import Command

from mongo.messages import create_message
from mongo.users import check_user

router = Router()

# Надсилає привітальне повідомлення при команді /start або /help

@router.message(Command("help", prefix='!/'), ChatTypeFilter(chat_type=['private']))
@router.message(Command("start", prefix='!/'), ChatTypeFilter(chat_type=['private']))
async def start(message: types.Message):
    await check_user(message)
    await create_message(func='send_message', chat_id=message.chat.id, text="Задай своє питання і ми надішлемо його анонімно нашим служителям")