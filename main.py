from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('7360083711:AAFhLlEb4pso0HH2Lc7m4VXzoRWPgmf6deU')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открывать веб страницу', web_app=WebAppInfo(url='')))
    await message.answer('Hello, my friend!', reply_markup=markup)

executor.start_polling(dp)