from typing import Union

from aiogram.filters.base import Filter
from aiogram.types import Message

from data import config

class WhiteList(Filter):
    def __init__(self, flag: bool) -> None:
        self.flag = flag
        
    async def __call__(self, message: Message) -> bool:
        return config.WHITELIST == self.flag