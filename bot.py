from api import mahsulot,random,random1
from aiogram import Dispatcher,Bot,executor
from aiogram.types import Message
import logging
import time

logging.basicConfig(level=logging.INFO)

bot=Bot(token='5897198043:AAEPq4jtsniDUeGDJpITeiOH5xhOqD5UAe4')
dp=Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    print(f"{message.from_user.full_name}({message.from_user.username})[id: {message.from_user.id}]: {message.text} | Time: {time.asctime()}")
    await message.answer(f"Hi {message.from_user.full_name}. I can get information about product!")

@dp.message_handler(commands='random')
async def rand(message: Message):
    print(f"{message.from_user.full_name}({message.from_user.username})[id: {message.from_user.id}]: {message.text} | Time: {time.asctime()}")
    ans=random()
    ans1=random1()
    await message.answer(ans)
    await message.answer_photo(photo=ans1)

@dp.message_handler()
async def mahsu(message: Message):
    print(f"{message.from_user.full_name}({message.from_user.username})[id: {message.from_user.id}]: {message.text} | Time: {time.asctime()}")
    if not message.text.isnumeric():
        try:
            text=message.text
            ans=mahsulot(text)
            await message.answer(ans)
        except:
            await message.reply("Mahsulot topilmadi!")
    else:
        await message.reply("So'zni kirit. Son mumkin emas!")


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)