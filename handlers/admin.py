from aiogram import types, Dispatcher
from config import bot, dp, ADMINS


async def ban(message: types.Message):
    if message.chat.type != "private":
        if not message.from_user.id in ADMINS:
            await message.reply("Ты не мой босс!!!")
        elif not message.reply_to_message:
            await message.reply("Комманда должна быть ответом на ссобщение")
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            # await bot.ban_chat_member()
            await message.answer(f"{message.from_user.first_name} братан забанил пользователя "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.reply("пиши в группу!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
