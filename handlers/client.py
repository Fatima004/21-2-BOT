from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from keyboard import client_cb


# @dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.answer(f"Привет хозяин {message.from_user.first_name}")
    await message.reply(f"This is reply)", reply_markup=client_cb.start_markup)


# @dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Кто краш гиктека?"
    answers = [
        'Esen',
        'Airas',
        'Asylbek',
        'Alexey',
        'Kanat',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="На самом деле краш Фатима",
        open_period=10,
        reply_markup=markup
    )


async def help_command(message: types.Message):
    await message.answer(f"Разбирайся сам!")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(help_command, commands=['help'])
