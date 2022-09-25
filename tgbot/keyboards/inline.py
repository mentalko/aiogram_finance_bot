from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#https://github.com/aiogram/aiogram/blob/dev-2.x/examples/regular_keyboard_example.py
#https://github.com/egeronik/TelegrammWallBot/blob/557d83d978f9baaaac2e76a50b9b621ee2dd0e10/app/bot/inlines.py


btn_back = InlineKeyboardButton('Назад', callback_data='btn_back')

menu_main = InlineKeyboardMarkup(row_width=2)
menu_main.add(InlineKeyboardButton('Показать баланс', callback_data='btn_show_balance'),
              InlineKeyboardButton('Пополнить баланс', callback_data='btn_topup_balance'),
              InlineKeyboardButton('Обменять валюту', callback_data='btn_exchange'),
              InlineKeyboardButton('Перевести деньги', callback_data='btn_transfer_money')
              )

menu_curency = InlineKeyboardMarkup(row_width=3)
menu_curency.add(InlineKeyboardButton('USD', callback_data='usd'),
                  InlineKeyboardButton('RUB', callback_data='rub'),
                #   InlineKeyboardButton('EUR', callback_data='eur'),
                ).row(btn_back)



def create_menu_exchange(_from = "USD",_to = "RUB"):
    menu_exchange = InlineKeyboardMarkup(row_width=3)
    menu_exchange.row(InlineKeyboardButton(_from, callback_data='btn_exchange_from'),
                    InlineKeyboardButton('=>', callback_data='None'),
                    InlineKeyboardButton(_to, callback_data='btn_exchange_to'))\
                .row(InlineKeyboardButton('Подтвердить!', callback_data='btn_exchange_ok'))\
                # .row(btn_back)
    return menu_exchange


menu_back = InlineKeyboardMarkup(row_width=2)
menu_back.add(btn_back)