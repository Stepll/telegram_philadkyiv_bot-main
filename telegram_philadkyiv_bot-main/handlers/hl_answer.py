from aiogram import types
from aiogram import Router

from filters.reply_filter import IsReplyFilter
from filters.chat_id_filter import ChatFilter
from filters.user_id_filter import UserFilter
from filters.whitelist_filter import WhiteList

from dispatcher import bot

from data import config
from mongo.messages import create_message, get_message

router = Router()

# Обробляє відповідь на неанонімні питання
@router.message(ChatFilter(chat_id=config.chat), IsReplyFilter('is_reply'), WhiteList(False))
@router.message(ChatFilter(chat_id=config.chat), IsReplyFilter('is_reply'), UserFilter(user_id=config.admin_ids), WhiteList(True))
async def answer(message: types.Message):

    # Знаходимо повідомлення в базі та витягуємо id користувача, до якого буде надіслано
    user_id = await get_message(message.reply_to_message.message_id)
    user_id = user_id['forward_from-id']

    try:
        await create_message(func='send_message',chat_id=user_id, text=message.text)
        await message.answer(text="🔹Повідомлення надіслано", reply_to_message_id=message.message_id)

    except: # Скоріш за все виникає через те, що користувач заблокував бот
        await message.answer(text="🔸Повідомлення не було доставлено", reply_to_message_id=message.message_id)
