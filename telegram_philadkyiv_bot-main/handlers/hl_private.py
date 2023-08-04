from aiogram import types
from aiogram import Router

from filters.chat_type_filter import ChatTypeFilter
from filters.blocked_filter import Blocked

from mongo.messages import create_message
from mongo.users import check_user

from data import config

router = Router()


# Обробляє повідомлення, які надсилають користувачі в чат
@router.message(ChatTypeFilter(chat_type=['private']), Blocked(False))
async def private(message: types.Message):
    await check_user(message)
    if config.ANONQUEST:
        await create_message(func='send_message', chat_id=config.chat, text=f'✉️ Анонімне питання: \n{message.text}', forward=message)
    else:
        await create_message(func='forward_message', chat_id=config.chat, message_id=message.message_id, from_chat_id=message.chat.id, forward=message)
    
    await message.answer('🔹Повідомлення надіслано', reply_to_message_id=message.message_id)


# Можна написати реакцію бота на заблокованого користувача
@router.message(ChatTypeFilter(chat_type=['private']), Blocked(True))
async def private_blocked(message: types.Message):
    pass