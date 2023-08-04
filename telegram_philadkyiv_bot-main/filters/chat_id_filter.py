from typing import Union

from aiogram.filters.base import Filter
from aiogram.types import Message


class ChatFilter(Filter):
    def __init__(self, chat_id: Union[str, int, list]) -> None:
        self.chat_id = chat_id

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.chat_id, str):
            return message.chat.id == self.chat_id
        if isinstance(self.chat_id, int):
            return message.chat.id == self.chat_id
        else:
            return message.chat.id in self.chat_id