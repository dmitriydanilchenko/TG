import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6075262728:AAHYvpVMII4eaRraCZDoA6imAGCKvNrtlkU'

# Configure logging
logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('''
    <b>/help</b> - <em>подсказка</em>
    <b>/start</b> - <em>старт</em>
    <b>/give</b> - <em>котик</em>
    
    ''', parse_mode='HTML')
async def on_started(_):
    print('Я запустился')

@dp.message_handler(content_types=['sticker'])
async def id_stiker(message: types.message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands=['give'])
async def stiker (message: types.Message):
    await message.reply("Смотри какой котик")
    await bot.send_sticker(message.from_user.id, sticker= 'CAACAgIAAxkBAAEJIs9kc6V42moTlmzpbuSETmmD1e24dgACigADJetbEn1YfcTgFPfSLwQ')

@dp.message_handler()
async def serdechko (message: types.Message):
    if message.text == '❤️':
        await message.answer("🖤")

'''
@dp.message_handler()
async def kolvo (message: types.Message):
    await message.answer(text=str(message.text.count('m')))
'''




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_started)