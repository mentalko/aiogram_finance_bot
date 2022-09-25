from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_send_phone = ReplyKeyboardMarkup(row_width=1)
menu_send_phone.add(KeyboardButton('Отправить номер', request_contact=True))
