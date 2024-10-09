from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from assets.transform import transform_int as tr
from decimal import Decimal
from assets.antispam import antispam
from datetime import datetime
from bot import bot
import time
import sqlite3
import random


@antispam
async def event(message: types.Message):
	await message.answer(f'''<b>Ивент Хэллоуин 🎃</b>
<i>Добро пожаловать на Хэллоуинское событие! Жуткие приключения ждут вас, и каждый участник сможет проявить себя в различных конкурсах и заданиях. Мы подготовили крутые призы, которые можно выиграть!</i>

<b>Основные задания:</b>

🎃 <b>Тыквенная Лотерея</b> (<code>Джекпот</code>)
Каждый может испытать удачу! В лотерее доступны случайные награды, такие как деньги, конфеты, B-coins 🎭. Не упустите шанс сорвать куш!

👹 <b>Победи монстра</b> (<code>Монстр</code>)
Встреться с монстрами и побеждай их, чтобы получить уникальные трофеи!

🍬 <b>Обмен конфет</b> (<code>Магазин</code>)
Собранные конфеты можно обменять на крутые призы в магазине. Чем больше конфет, тем ценнее награды!

👻 <b>Возможность пугать игроков</b> (<code>Напугать</code>)
Используйте страшные маски, чтобы пугать других игроков и зарабатывать дополнительные бонусы!''')


def register_handlers(dp: Dispatcher):
  dp.register_message_handler(event, lambda message: message.text.lower() == 'праздник')

MODULE_DESCRIPTION = {
	'name': 'Новый год',
	'description': '''Ивент-модуль Новый год:
- Новое оформление
- Новый ивент "подарки дедушке"
- Новая игра
- Новые игровые валюты

* Модуль использует собственную базу данных
* Помощью по модулю введите "Праздник"
!! В РАЗРАБОТКЕ !!'''
}
