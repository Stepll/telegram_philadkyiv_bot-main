from typing import Union

from aiogram.filters.base import Filter
from aiogram.types import Message


class UserFilter(Filter):
    def __init__(self, user_id: Union[int, str, list]) -> None:
        self.user_id = user_id

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_id, int):
            return message.from_user.id == self.user_id
        elif isinstance(self.user_id, str):
            return message.from_user.id == self.user_id
        else:
            return message.from_user.id in self.user_id