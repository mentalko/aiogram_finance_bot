from aiogram import Dispatcher, types
from aiogram.types import Message
from tgbot.services.api_request import BankAPI

import tgbot.keyboards.inline as kb
import tgbot.keyboards.reply as kb_r


async def user_start(message: Message):
    if BankAPI.get_account_by_id(message.from_user.id):
        await message.answer("Вы уже зарегистрированы!", reply_markup=types.ReplyKeyboardRemove())
        await message.answer("Меню", reply_markup=kb.menu_main)

    else:
        await message.reply("Привет! \nОтправь свой номер для авторизации!", reply_markup=kb_r.menu_send_phone)

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
