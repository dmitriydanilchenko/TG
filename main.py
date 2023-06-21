from aiogram import Bot, Dispatcher, executor, types
import random

TOKEN = '6075262728:AAHYvpVMII4eaRraCZDoA6imAGCKvNrtlkU'
bot = Bot(token = TOKEN)
dp = Dispatcher(bot = bot)

HELP_COMMAND = '''
<b>/start</b> - <em>начало работы</em>
<b>/help</b> - <em>варианты команд</em>
<b>/image</b> - <em>случайное фото</em>
<b>/stiker</b> - <em>случайный стикер</em>
'''
SPISOK_KARTINOK = (
    'https://w.forfun.com/fetch/2c/2c38ec7c72e3d0094f591d6f735a3b8e.jpeg',
    'https://pet-mir.ru/wp-content/uploads/2017/04/84612_org.jpg',
    'https://w.forfun.com/fetch/c4/c493aac67877288476b0fc52d55f55cf.jpeg',
    'https://vsegda-pomnim.com/uploads/posts/2023-03/1679186907_vsegda-pomnim-com-p-koshachi-glazki-foto-72.jpg'
)
SPISOK_STIKEROV = ('CAACAgIAAxkBAAEJbHRkkztqwX35q-ZyYtVLIupnimkiXwACaR0AAulVBRitKUu7Ijoody8E',
                   'CAACAgIAAxkBAAEJbHhkkzuFF3AuvqeFui-UvI_Ttz1CHwAChQkAAhhC7giKfFqZOBzASy8E',
                   'CAACAgIAAxkBAAEJIs9kc6V42moTlmzpbuSETmmD1e24dgACigADJetbEn1YfcTgFPfSLwQ',
                   'CAACAgIAAxkBAAEJbHpkkzunVbVKd9KqO6dz7KdNM6bueQACUQADrWW8FIai9pu49fluLwQ')
async def on_startup(_):
    print('Я запустился')
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await  message.answer(text='Добро пожаловать!\n'
                               'Список команд /help')

@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await  message.answer(text=HELP_COMMAND,
                          parse_mode='HTML')

@dp.message_handler(commands=['image'])
async def cmd_img(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(SPISOK_KARTINOK))

@dp.message_handler(commands=['stiker'])
async def cmd_stiker(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=random.choice(SPISOK_STIKEROV))


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup= on_startup)