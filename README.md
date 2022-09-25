# Telegram CashBot 

Telegram Бот реализует простые банковские операции как: пополнение, перевод средств и обмен валют.\
Бот написан на Python с использованием асинхронной библиотеки aiogram, API на чистом Golang


Bot for money transfers in Telegram.\
Telegram Bot implements simple banking operations such as: replenishment, transfer of funds and currency exchange.\
The bot is written in Python using the aiogram asynchronous library, pure Golang API

<!-- The public instance of this bot is running as [@my_aiogramBOT](https://t.me/my_aiogramBOT). -->

Golang API Server repository: https://github.com/mentalko/go_api_server


## Features
* registration by phone number
* show balance
* top up your account
* transferring money to another user of the bot by his login
* exchange money from dollars to rubles and vice versa

## TODO:
- [ ] transaction history
- [ ] fix some shit code magic


## Screenshots
![Main menu](https://)

## How to use
1. Rename ".env example" to ".env" and pate your bot tocken
```
BOT_TOKEN=
```
2. Run docker-compose
```
docker-compose up --build 
```