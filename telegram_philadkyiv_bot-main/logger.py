import logging
from dispatcher import bot
from data import config

# Логування помилок
async def exceptions(message_error):
    logging.warning(message_error)
    await bot.send_message(chat_id=config.administrator, text=f'🔻<b>Error:</b> {message_error}')