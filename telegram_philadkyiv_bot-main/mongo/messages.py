import logging
import inspect
from datetime import datetime

from aiogram.exceptions import TelegramMigrateToChat
from data import config
from dispatcher import bot 

from mongo.initialization import login
from logger import exceptions

# Реєстрація усіх вихідних повідомлень
async def create_message(func, chat_id=None, text=None, message_id=None, from_chat_id=None, forward=None):
    try:
        if func == 'send_message':
            message = await eval('bot.'+func)(chat_id=chat_id, text=text)

        elif func == 'forward_message':
            message = await eval('bot.'+func)(chat_id=chat_id, message_id=message_id, from_chat_id=from_chat_id)

        else: # На випадок, якщо помилково була вказана інша функція
            message_error = f'NonExistentFunction: функція {func} недоступна до обробки в {inspect.stack()[0][3]} {inspect.stack()[0][1]}'
            logging.warning(message_error)
            await bot.send_message(chat_id=config.administrator, text=f'🔻<b>Error:</b> {message_error}')
        
        await message_registration(message, forward)

    # На випадок, якщо адміністраторський чат став супергрупою
    except TelegramMigrateToChat:
        await exceptions(f'TelegramMigrateToChat: chat_id {chat_id} став супергрупою')

    # Вилавлює інші помилки
    except Exception as e:
        await exceptions(f'Exception: {e}')


# Реєструє повідомлення до бота в базі данних
async def message_registration(message, forward):
    collection = await login('messages')
    post = {"message_id": message.message_id,
            "chat-id": message.chat.id,
            "chat-type": message.chat.type,
            "chat-title": message.chat.title,
            "chat-username": message.chat.username,
            "chat-first_name": message.chat.first_name,
            "chat-last_name": message.chat.last_name,
            "chat-bio": message.chat.bio,
            "chat-description": message.chat.description,
            "from_user-id": message.from_user.id,
            "from_user-is_bot": message.from_user.is_bot,
            "from_user-username": message.from_user.username,
            "from_user-first_name": message.from_user.first_name,
            "from_user-last_name": message.from_user.last_name,
            "from_user-language_code": message.from_user.language_code,
            "from_user-is_premium": message.from_user.is_premium,
            "text": message.text,
            "created_at": datetime.now(),
            "edited_at": datetime.now()}
    
    if message.forward_from != None: # При форварді повідомлення з пп до чату
        extra = {
            "forward_from-id": message.forward_from.id,
            "forward_from-is_bot": message.forward_from.is_bot,
            "forward_from-first_name": message.forward_from.first_name,
            "forward_from-last_name": message.forward_from.last_name,
            "forward_from-username": message.forward_from.username,
            "forward_from-language_code": message.forward_from.language_code,
            "forward_from-is_premium": message.forward_from.is_premium,
        }
        post.update(extra)
    elif forward: # Якщо анонімне питання або користувач приватний
        extra = {
            "forward_from-id": forward.from_user.id,
            "forward_from-is_bot": forward.from_user.is_bot,
            "forward_from-username": forward.from_user.username,
            "forward_from-first_name": forward.from_user.first_name,
            "forward_from-last_name": forward.from_user.last_name,
            "forward_from-language_code": forward.from_user.language_code,
            "forward_from-is_premium": forward.from_user.is_premium,
        }
        post.update(extra)

    collection.insert_one(post).inserted_id


# Отримати данні про конкретне повідомлення з бази
async def get_message(message_id):
    collection = await login('messages')
    result = collection.find_one({'message_id': message_id, 'chat-id':config.chat},{'_id': 0, 'forward_from-id': 1})
    return result