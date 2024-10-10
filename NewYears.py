import asyncio
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

from commands import db as gdb
from commands.db import conn as conngdb, cursor as cursorgdb

from commands.main import CONFIG as HELLO_CONFIG
from commands.help import CONFIG as HELP_CONFIG



@antispam
async def event(message: types.Message):
	await message.answer(f'''<b>Ивент Новый год 🎃</b>
<i>Добро пожаловать на Новогоднее событие! Весёлые приключения ждут вас, и каждый участник сможет проявить себя в различных конкурсах и заданиях. Мы подготовили крутые призы, которые можно выиграть!</i>

<b>Основные задания:</b>

🎃 <b>Подарок от деда мороза!</b> (<code>Подарок</code>)
Каждый может испытать удачу! В лотерее доступны случайные награды, такие как деньги, конфеты, B-coins 🎭. Не упустите шанс сорвать куш!

👹 <b>Победи друга</b> (<code>Монстр</code>)
Встреться с другом и закидай его снежками, чтобы получить уникальные подарки!

🍬 <b>Обменять </b> (<code>Магазин</code>)
Собранные конфеты можно обменять на крутые призы в магазине. Чем больше снежков, тем ценнее награды!

👻 <b>Возможность пугать игроков</b> (<code>Напугать</code>)
Используйте страшные маски, чтобы пугать других игроков и зарабатывать дополнительные бонусы!''')


@antispam
async def shop(message: types.Message):
	user_id = message.from_user.id
	name = await gdb.url_name(user_id)
	await message.answer(f'''{name}, добро пожаловать в наш магазин:

Маски: 25🍬 - 1🎭
Деньги: 1🍬 - 1е5$

❗️ Для покупки введите:
Купить маску (кол-во)
Открыть конфеты (кол-во)''')


class Database:
	def __init__(self):
		self.conn = sqlite3.connect('modules/temp/NewYears.db')
		self.cursor = self.conn.cursor()
		self.create_tables()

	def create_tables(self):
		self.cursor.execute('''
			CREATE TABLE IF NOT EXISTS users (
				user_id INTEGER,
				snow INTEGER DEFAULT '0',
				hlapyshka INTEGER DEFAULT '3',
				podarok INTEGER DEFAULT '0'
			)''')
		self.conn.commit()
		
	async def reg_user(self, user_id):
		ex = self.cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,)).fetchone()
		if not ex:
			self.cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
			self.conn.commit()
			
	async def get_balance(self, user_id):
		await self.reg_user(user_id)
		return self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()
	



@antispam
async def bagg(message: types.Message):
	user_id = message.from_user.id
	name = await gdb.url_name(user_id)
	data = await db.get_balance(user_id)
	await message.answer(f'{name}, в вашем новогоднем мешке:\n🍬 Снежки: {data[1]}\n🎃 Хлапушка: {data[2]}\n🎭 Подарки: {data[3]}')


def register_handlers(dp: Dispatcher):
  dp.register_message_handler(event, lambda message: message.text.lower() == 'новый год')
  dp.register_message_handler(bagg, lambda message: message.text.lower() == 'мешман')
  dp.register_message_handler(shop, lambda message: message.text.lower() == 'шопнг')



MODULE_DESCRIPTION = {
	'name': 'Новый год',
	'description': '''Ивент-модуль Новый год:
- Новое оформление
- Новый ивент "подарок"
- Снежки
- Новые игровая валюта

* Модуль использует собственную базу данных
* Помощью по модулю введите "Праздник"
!! В РАЗРАБОТКЕ !!'''
}
