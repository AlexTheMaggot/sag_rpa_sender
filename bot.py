import os
import logging
import time

from aiogram import Bot, Dispatcher, executor, types
from config import *


API_TOKEN = BOT_TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Бот для обновления таблицы. Отправьте файл чтобы заменить его на сервере.")


@dp.message_handler(content_types=['document'])
async def echo(message: types.Message):
    if message.chat.id == CHAT_ID:
        timestamp = time.time()
        await message.document.download(destination_file=f'{DIRECTORY}{message.document.file_name}')
        if timestamp < os.path.getmtime(f'{DIRECTORY}{message.document.file_name}'):
            await message.answer('Файл успешно загружен')
        else:
            await message.answer('Ошибка при загрузке файла')
    else:
        await message.answer('Нет доступа')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
