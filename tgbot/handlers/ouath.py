from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

import tgbot.keyboards.inline as kb

from tgbot.services.api_request import BankAPI


async def bot_ouath(message: types.ContentType.CONTACT):
    user = message.from_user
    data = await BankAPI.create_account(user.id, user.username, message.contact.phone_number, 1000, 10000)

    await message.answer("Отлично, теперь вы зарегистрированы!", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Меню", reply_markup=kb.menu_main)


def register_ouath(dp: Dispatcher):
    dp.register_message_handler(
        bot_ouath, content_types=types.ContentType.CONTACT)
