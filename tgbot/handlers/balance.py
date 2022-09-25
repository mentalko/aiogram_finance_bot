from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.storage import FSMContext

import tgbot.keyboards.inline as kb
from tgbot.misc.states import Balance
from tgbot.services.api_request import BankAPI

from random import choice


async def bot_main_menu(callback_query: types.CallbackQuery, state: FSMContext):
    if state:
        await state.reset_state()

    text = [
        "Меню: \n/help"
    ]
    await callback_query.message.edit_text('\n'.join(text), reply_markup=kb.menu_main)


async def bot_show_balance(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    account_data = await BankAPI.get_account_by_id(user_id)

    text = [
        "Баланс:",
        f"RUB: {account_data['balance_rub']} руб",
        f"USD: ${account_data['balance_usd']}",
    ]

    await callback_query.message.edit_text('\n'.join(text), reply_markup=kb.menu_main)


async def bot_topup_balance(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(operation_type="TOPUP")
    text = [
        "Пополнение! \nВыберете валюту, которую хотите зачислить на счет:",
    ]
    await callback_query.message.edit_text('\n'.join(text), reply_markup=kb.menu_curency)
    await Balance.B_curency.set()


async def bot_exchange(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(operation_type="EXCHANGE")
    text = [
        "USD -> RUB"
    ]
    await callback_query.message.edit_text('\n'.join(text), reply_markup=kb.create_menu_exchange())


async def bot_transfer_money(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(operation_type="TRANSFER")
    text = [
        "Перевод! \nУкажите ник пользователя или номер телефона:",
    ]
    await callback_query.message.edit_text('\n'.join(text), reply_markup=kb.menu_back)
    await Balance().B_recipient.set()


async def select_exchange(callback_query: types.CallbackQuery, state: FSMContext):
    data = callback_query.data
    curency_list = ['RUB', 'USD',  'RUB', 'USD', ] # 'CNY', "EUR"]

    curent_vls = callback_query.message.text.split('->')
    b_from = curent_vls[0].strip()
    b_to = curent_vls[1].strip()

    if not 'ok' in data:
        if 'from' in data:
            indx = curency_list.index(b_from)
            b_from = curency_list[indx + 1]
        if 'to' in data:
            indx = curency_list.index(b_to)
            b_to = curency_list[indx + 1]
        await callback_query.message.edit_text(f"{b_from} -> {b_to}", reply_markup=kb.create_menu_exchange(b_from, b_to))

    elif 'ok' in data:
        await callback_query.message.answer('Теперь укажите сумму:')
        await state.update_data(b_from=b_from.lower(), b_to=b_to.lower())
        await Balance.B_value.set()


async def select_recipient(message: types.Message(), state: FSMContext):
    selected_recipient = message.text
    await state.update_data(recipient=selected_recipient)
    await message.answer(f"Пользователь {selected_recipient} задан! \nВыберете валюту, которую хотите перевести:", reply_markup=kb.menu_curency)
    await Balance.B_curency.set()


async def select_curency(callback_query: types.CallbackQuery, state: FSMContext):
    selected_curency = callback_query.data
    await state.update_data(curency=selected_curency)
    await callback_query.message.edit_text("Укажите сумму;", reply_markup=kb.menu_back)
    await Balance.B_value.set()


async def select_value(message: types.Message(), state: FSMContext):
    selected_value = message.text
    await state.update_data(value=selected_value)
    await operation_complited(message, state)


async def operation_complited(message: types.Message(), state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    type = data.get("operation_type")
    
    if type == "TOPUP":
        value = int(data.get("value"))
        curency = "balance_" + data.get("curency")
        await BankAPI.make_topup(user_id, curency, value)

    elif type == "TRANSFER":
        value = int(data.get("value"))
        curency = data.get("curency").upper()
        account_to = data.get("recipient")
        await BankAPI.create_transaction(user_id, account_to, curency, value)

    elif type == "EXCHANGE":
        value = int(data.get("value"))
        curency_from = "balance_" + data.get("b_from")
        curency_to = "balance_" + data.get("b_to")
        await BankAPI.make_exchange(user_id, curency_from, curency_to, value)

    await message.answer("Операция выполнена!", reply_markup=kb.menu_main)


def register_balance(dp: Dispatcher):
    dp.register_callback_query_handler(
        bot_show_balance, lambda c: c.data == 'btn_show_balance', state='*')
    dp.register_callback_query_handler(
        bot_topup_balance, lambda c: c.data == 'btn_topup_balance', state='*')
    dp.register_callback_query_handler(
        bot_exchange, lambda c: c.data == 'btn_exchange', state='*')
    dp.register_callback_query_handler(
        bot_transfer_money, lambda c: c.data == 'btn_transfer_money', state='*')

    dp.register_callback_query_handler(
        bot_main_menu, lambda c: c.data == 'btn_back', state='*')

    dp.register_callback_query_handler(
        select_exchange, lambda c: c.data.startswith('btn_exchange_'))
    dp.register_message_handler(select_recipient, state=Balance.B_recipient)
    dp.register_callback_query_handler(select_curency, state=Balance.B_curency)
    dp.register_message_handler(select_value, state=Balance.B_value)
