from aiogram.filters.base import Filter
from aiogram.types import Message


class IsReplyFilter(Filter):
    def __init__(self, is_reply):
        self.is_reply = is_reply

    async def __call__(self, msg: Message):
        if msg.reply_to_message and self.is_reply:
            return {'reply': msg.reply_to_message}
        elif not msg.reply_to_message and not self.is_reply:
            return True