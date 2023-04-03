
import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio
from aiogram import types
from aiogram.dispatcher import filters
import random
import os
import aiocron
from datetime import datetime, time


PICTURES_DIR = 'pictures'
PICTURES = [os.path.join(PICTURES_DIR, file) for file in os.listdir(PICTURES_DIR) if file.endswith(('.jpg', '.jpeg', '.png'))]

# Создаем список файлов gif из папки gifs, которая находится в текущей директории
GIFS_DIR = 'gifs'
GIFS = [os.path.join(GIFS_DIR, file) for file in os.listdir(GIFS_DIR) if file.endswith('.gif')]

BAD_WORDS = ['бля', 'бляяя', 'пиздец', 'охуеть', 'блядь', 'хуй', 'пизда']

# Создаем список файлов pictures из папки pictures, которая находится в текущей директории
PICTURES_DIR = 'pictures'
PICTURES = [os.path.join(PICTURES_DIR, file) for file in os.listdir(PICTURES_DIR) if file.endswith(('.jpg', '.jpeg', '.png'))]

WELCOME_GIF_DIR = 'welcome'
WELCOME_GIF = [os.path.join(WELCOME_GIF_DIR, file) for file in os.listdir(WELCOME_GIF_DIR) if file.endswith('.gif')]


nameforbot = '@VoldemarShestirkin_bot'


API_TOKEN = '6295421173:AAEhrPkXjShPY1-7NGPd06tiPYn5n8QtgRU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@aiocron.crontab('59 12 * * 1-5') # Запускаем каждый день с понедельника по пятницу в 17:00
async def scheduled_message():
    # Выбираем случайную картинку из списка
    picture = random.choice(PICTURES)

    # Отправляем сообщение с фото
    with open(picture, 'rb') as photo:
        await bot.send_photo(chat_id=-867417566, photo=photo, caption='Пора обедать!')


@aiocron.crontab('0 17 * * 1-5') # Запускаем каждый день с понедельника по пятницу в 12:40
async def scheduled_message():
    # Выбираем случайную картинку из списка
    picture = random.choice(PICTURES)

    # Отправляем сообщение с фото
    with open(picture, 'rb') as photo:
        await bot.send_photo(chat_id=-867417566, photo=photo, caption='Пора ужинать!')

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
    # Выбираем случайную гифку из списка
    gif = random.choice(WELCOME_GIF)
    
    # Открываем файл гифки как binary file
    with open(gif, 'rb') as animation:
        # Отправляем гифку вместе с сообщением приветствия
        await bot.send_animation(message.chat.id, animation=types.InputFile(animation), caption="Привет! Я Володя MVP_0.0.1 и я настоящий!\nОтправь любое сообщение с упоминанием моего юзернейма, и я тебе обязательно тебе отвечу!\nз.ы. всем плодотворного дня и хорошего настроения :3")








@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    await message.answer('Дратути!')



#@dp.message_handler(filters.Text(startswith=nameforbot, ignore_case=True))
#async def text_example(msg: types.Message):
    #reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #reply = f'Твоё сообщение "{msg.text}" слишком заумное! Я не пониматъ!'
    #await msg.reply(reply, reply_markup=reply_markup)





#@dp.message_handler(filters.Text(contains=FORBIDDEN_PHRASE, ignore_case=True))
#async def text_example(msg: types.Message):
  #  await msg.reply('Сам фигня!')

#@dp.message_handler()
#async def check_forbidden_word(msg: types.Message):
    # Проверяем наличие матерных слов в сообщении
 #   for bad_word in BAD_WORDS:
  #      if bad_word in msg.text.lower():  # Сравниваем в нижнем регистре
   #         await msg.reply('Не матерись, пожалуйста!')
    #        return  # Прерываем цикл, если найдено матерное слово

    # Проверяем наличие выборочных запрещенных слов из списка FORBIDDEN_PHRASE
   # for forbidden_word in FORBIDDEN_PHRASE:
    #    if forbidden_word.lower() in msg.text.lower():  # Сравниваем в нижнем регистре
     #       await msg.reply('Такие слова использовать нельзя!')
      #      return  # Прерываем цикл, если найдено запрещенное слово

    # Если нет запрещенных слов и матерных слов, продолжаем обработку сообщения
    #await text_example(msg)


@dp.message_handler(filters.Text(startswith=nameforbot, ignore_case=True))
async def text_example(msg: types.Message):
    regexp = r'@VoldemarShestirkin_bot'
     #Ищем совпадение регулярного выражения
    match = re.search(regexp, msg.text)
     #Если совпадение найдено, исключаем его из цитирования
    if match:
        reply_text = re.sub(regexp, '', msg.text)
    else:
        reply_text = msg.text
     #Отправляем ответ с цитированием
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reply = f'Твоё сообщение "{reply_text}" слишком заумное! Я не пониматъ!'
    await msg.reply(reply, reply_markup=reply_markup)


#@dp.message_handler()
#async def check_forbidden_word(msg: types.Message):
   #if msg.text.lower().startswith(nameforbot.lower()):
   #     return
   #  #Проверяем наличие матерных слов в сообщении
   #for bad_word in BAD_WORDS:
    #    if bad_word in msg.text.lower(): # Сравниваем в нижнем регистре
     #       # В случае нахождения матерного слова отправляем ответ с гифкой
      #      gif = random.choice(GIFS) # Выбираем случайную гифку из списка
       #     with open(gif, 'rb') as animation:
        #        caption = 'Аниме девочки за плохие слова бьют луком по голове!'
         #       await bot.send_animation(msg.chat.id, animation=types.InputFile(animation), caption=caption, reply_to_message_id=msg.message_id)
          #  return # Прерываем обработку сообщения
     #Если нет запрещенных слов и матерных слов, продолжаем обработку сообщения
   #await text_example(msg)




if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)