
import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio
from aiogram import types
from aiogram.dispatcher import filters

FORBIDDEN_PHRASE = [
    'Курс',
    'Фигня'
]

nameforbot = '@VolodyaShestirkinBot'


API_TOKEN = '6266310277:AAGXmHk0YlgvU1I_dsRWR6JcfVj6g-oFDyw'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(filters.Text(startswith=nameforbot, ignore_case=True))
async def text_example(msg: types.Message):
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    reply = f'Твоё сообщение "{msg.text}" слишком заумное! Я не пониматъ!'
    await msg.reply(reply, reply_markup=reply_markup)

@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    await message.answer('Бот работает и готов отвечать!2')

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Володя19 и я настоящий!\nОтправь мне любое сообщение с использованием mention (@VolodyaShestirkinBot), а я тебе обязательно отвечу.") 



#if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)