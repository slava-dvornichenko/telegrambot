from loader import dp
from aiogram.types import Message
from keyboards.default import faq
from aiogram.dispatcher.filters import Command,Text

@dp.message_handler(Command("faq"))
async def faq(message:Message):
    await message.answer("Выберите опцию", reply_markup=faq)


@dp.message_handler(Text(equals=["VPN"]))
async def show_faq(message:Message):
    await message.answer(f"VPN- ")