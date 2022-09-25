
import logging
import os
import json

import aiohttp.client
from aiogram.types import Location
import urllib

from tgbot.services.object import Account

# https://github.com/karvozavr/weather-bot/blob/master/weather_service.py
# https://github.com/arichr/yakusubot/blob/main/translate/func.py


class BankServiceException(BaseException):
    pass


_url = 'http://api/accounts'


class BankAPI:

    async def get_account_by_id(account_id: int) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{_url}/{account_id}") as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    return None

    async def create_account(id, username, phone_number, balance_usd, balance_rub) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{_url}", data=json.dumps({
                'id': id,
                'username': username,
                'phone_number': phone_number,
                'balance_usd': balance_usd,
                'balance_rub': balance_rub,
            })) as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    return {"error": resp.status}

    async def make_topup(id, curency, value) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api/topup?id={id}&curency={curency}&value={value}") as resp:
                if resp.status == 200:
                    return {}
                else:
                    return {"error": resp.status, "url": resp.url}

    async def make_exchange(id, curency_from, curency_to, value) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api/exchange?id={id}&curency_from={curency_from}&curency_to={curency_to}&value={value}") as resp:
                if resp.status == 200:
                    return {}
                else:
                    return {"error": resp.status, "url": resp.url}

    async def create_transaction(id, account_to, curency, value) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"http://api/transactions", data=json.dumps({
                'account_from': id,
                'account_to': account_to,
                'curency': curency,
                'value': value,
            })) as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    return {"error": resp.status}

# async def create_account() -> dict:
#     url = 'http://localhost:8080/account'

#     await session.post(url, data=json.dumps(payload),)
#     make_http_query(url)


# async def make_get_query(url: str) -> dict:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             if resp.status == 200:
#                 return await resp.json()


# async def make_post_query(url: str, payload: dict) -> dict:
#     payload = json.dumps(payload)
#     headers = {'content-type': 'application/json'}
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, data=data, headers=headers) as resp:
#             if resp.status == 200:
#                 return await resp.json()


# async def translate(
#     target: Language,
#     text: str,
#     show_original=False,
# ) -> Translation:
    # """Translate text.
    # Parameters:
    #     target: Target language
    #     text: Your text
    #     show_original: Show original text?
    # Returns:
    #     Translation
    # """
    # url = 'https://translation.googleapis.com/language/translate/v2'
    # payload = {
    #     'key': 'AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw',
    #     'q': text,
    #     'target': target.code,
    #     'format': 'text',
    #     'source': '',
    # }


# async def make__query(url: str) -> WeatherInfo:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             if resp.status == 200:
#                 return get_weather_from_response(await resp.json())

# async def make__query2(url: str) -> WeatherInfo:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, params=payload) as request:
#             if request.status != status.OK:
#                 return Translation(
#                     title='Sorry, Google API is not available.',
#                     text="Can't connect to Google API. Contact @arisetta.",
#                 )
#             return (await request.json())['sl']
