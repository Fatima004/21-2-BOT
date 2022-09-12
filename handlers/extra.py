from aiogram import types, Dispatcher
from config import bot, dp


# @dp.message_handler(content_types=['text', 'photo'])
async def echo(message: types.Message):
    username = f"@{message.from_user.username}" \
        if message.from_user.username is not None else message.from_user.full_name
    bad_words = ['js', 'html', 'css', 'react', "дурак", "глупый"]
    for word in bad_words:
        if word in message.text.lower():
            await message.answer(
                f"ХАРАМ ХАРАМ ХАРАМ {username} сам ты {word}"
            )

    if message.text.startswith("."):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == 'dice':
        dice = await bot.send_dice(message.chat.id, emoji="⚽️")
        # print(dice.dice.value)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo, content_types=['text', 'photo'])
