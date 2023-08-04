from aiogram import Bot, Dispatcher, Router

from aiogram.enums.parse_mode import ParseMode

from data import config

router = Router()

# storage = MemoryStorage()
# dp = Dispatcher(storage=storage)

dp = Dispatcher()
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
