from aiogram import F
from aiogram import types
from aiogram import Router

router = Router()

# Тестовий хендлер
@router.message(F.photo)
async def photo_msg(message: types.Message):
    await message.answer("Это точно какое-то изображение!")