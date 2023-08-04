from aiogram import types
from aiogram import Router

from filters.reply_filter import IsReplyFilter
from filters.chat_id_filter import ChatFilter
from filters.user_id_filter import UserFilter
from aiogram.filters.command import Command

from mongo.users import get_user, change
from mongo.messages import get_message

from data import config

router = Router()


# Блокування користувача
@router.message(ChatFilter(chat_id=config.chat), IsReplyFilter('is_reply'), UserFilter(user_id=config.admin_ids), Command("ban", prefix='!/'))
async def admin_ban(message: types.Message):
    user_id = await get_message(message.reply_to_message.message_id)
    user_id = user_id['forward_from-id']

    result = await get_user(user_id, 'users')
    # print(result['blocked'])
    try:
        if result['blocked']:
            await message.answer('🔒Користувач уже заблокований', reply_to_message_id=message.message_id)
        else:
            await change('user_id', result.from_user.id, 'blocked', True)
            await message.answer('🔒Користувач заблокований', reply_to_message_id=message.message_id)
    except Exception as e:
        print(e)

@router.message(ChatFilter(chat_id=config.chat), IsReplyFilter('is_reply'), UserFilter(user_id=config.admin_ids), Command("unban", prefix='!/'))
async def admin_unban(message: types.Message):
    user_id = await get_message(message.reply_to_message.message_id)
    user_id = user_id['forward_from-id']

    result = await get_user(user_id, 'users')
    # print(result['blocked'])
    try:
        if result['blocked']:
            await change('user_id', message.from_user.id, 'blocked', False)
            await message.answer('🔓Користувач розблокований', reply_to_message_id=message.message_id)
        else:
            await message.answer('🔓Користувач уже розблокований', reply_to_message_id=message.message_id)
    except Exception as e:
        print(e)
