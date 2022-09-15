from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True,
                                   )

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
help_button = KeyboardButton("/help")

share_location = KeyboardButton("Share location", request_location=True)
share_info = KeyboardButton("Share info", request_contact=True)

start_markup.add(start_button, quiz_button, help_button).row(share_location, share_info)

cancel_button = KeyboardButton("CANCEL")
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(cancel_button)


gender_g = KeyboardButton("Я девушка")
gender_b = KeyboardButton("Я мужчина")
gender_u = KeyboardButton("Я незнаю")

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(gender_b, gender_g, gender_u).row(cancel_button)

