from aiogram import types
from aiogram.types import ContentType
from loader import dp
from utils.db_api import db
from utils.db_api.db import conn, cur
from data import config


@dp.message_handler(content_types=ContentType.TEXT)
async def text(message):
    if message.text.lower() == 'солодких снів':
        await message.reply('Найкращих снів! \U0001F970\U0001F970\U0001F970', disable_notification=True)

    if message.text.lower() == 'Добpaніч':
        await message.reply('Найкращих снів! \U0001F970\U0001F970\U0001F970', disable_notification=True)

    if "слава україні" in message.text.lower():
        await message.reply(f'Героям слава!', disable_notification=True)

    if message.text.lower() == 'добраніч':
        await message.reply('Найкращих снів! \U0001F970\U0001F970\U0001F970', disable_notification=True)

    if message.text.lower() == 'ранку':
        await message.reply(f'Доброго ранку!! \U0001F970\U0001F970\U0001F970')

    if message.text.lower() == 'добрий ранок':
        await message.reply(f'Доброго ранку!! \U0001F970\U0001F970\U0001F970', disable_notification=True)

    if message.text.lower() == 'доброго ранку':
        await message.reply(f'Доброго ранку!! \U0001F970\U0001F970\U0001F970', disable_notification=True)

    if message.text.lower() == 'доброго ранку!':
        await message.reply(f'Доброго ранку!! \U0001F970\U0001F970\U0001F970', disable_notification=True)

    if message.text.lower() == 'добрий ранок!':
        await message.reply(f'Доброго ранку!! \U0001F970\U0001F970\U0001F970', disable_notification=True)

    if message.text.lower() == 'сранку':
        await message.reply(f'Доброго сранку!! \U0001F970\U0001F970\U0001F970', disable_notification=True)

    if message.text.lower() == 'бляха':
        await message.reply(f'муха', disable_notification=True)

    if message.text.lower() == 'ку':
        await message.reply(f'Ку', disable_notification=True)

    if message.text.lower() == 'hfyre':
        await message.reply(f'І тобі доброго hfyre!!!', disable_notification=True)

    if message.text.lower() == 'лю':
        await message.reply(f'*механічні звуки заздрості...', disable_notification=True)

    if message.text.lower() == 'люблю тебе':
        await message.reply(f'механічні звуки заздрості... ', disable_notification=True)

    if message.text.lower() == 'де всі?':
        await message.reply(f'На уроках мб', disable_notification=True)

    if message.text.lower() == 'лолі':
        await message.reply(f'це любоФ', disable_notification=True)

    if message.text.lower() == 'Слава Україні':
        await message.reply(f'Героям Слава!', disable_notification=True)
