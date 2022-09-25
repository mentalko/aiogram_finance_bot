from aiogram import Dispatcher, types
from aiogram.types import Message

import tgbot.keyboards.inline as kb
import tgbot.keyboards.reply as kb_r
import logging

from tgbot.services.api_request import BankAPI


async def admin_start(message: Message):
    if await BankAPI.get_account_by_id(message.from_user.id):
        await message.answer("Вы уже зарегистрированы!", reply_markup=types.ReplyKeyboardRemove())
        await message.answer("Меню", reply_markup=kb.menu_main)

    else:
        await message.answer("Привет, админ! \nОтправь свой номер для авторизации!", reply_markup=kb_r.menu_send_phone)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start,
                                commands=["start"], state="*", is_admin=True)
