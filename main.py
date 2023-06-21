from aiogram import Bot,types,Dispatcher,executor
import random

TOKEN = '1170912818:AAF6m9CYUvAHroPGQlRnGCzKkq3C4-XjgC8'
bot = Bot(token = TOKEN)
dp = Dispatcher(bot = bot)

HELP_COMMAND = '''
<b>start</b> - <em>начало работы</em>
<b>help</b> - <em>варианты команд</em>
<b>image</b> - <em>случайное фото</em>
<b>stiker</b> - <em>случайный стикер</em>
'''

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await  message.answer(text='Добро пожаловать!')

    await message.delete()

@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await  message.answer(text=HELP_COMMAND,
                          parse_mode='HTML')
async def on_startup(_):
    print('Я запустился')


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)