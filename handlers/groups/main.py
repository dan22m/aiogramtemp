from aiogram import types
from loader import dp
import base_text
from data import config



@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(base_text.start_msg)
    


@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await message.answer(base_text.help_msg)
    

@dp.message_handler(
    commands="json",
    commands_prefix="!/*"
)
async def cmd_json(message: types.Message):
    await message.answer(f'<code>{message}</code>'.replace(",", ",\n"))
   