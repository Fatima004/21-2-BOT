from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboard.client_cb import gender_markup, cancel_markup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    age = State()
    gender = State()
    region = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.photo.set()
        await message.answer(f"Салалекум {message.from_user.first_name} "
                             f"скинь фотку...",
                             reply_markup=cancel_markup)
    else:
        await message.answer("Пиги в личку!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Как звать?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какого года будишь эу??")


async def load_age(message: types.Message, state: FSMContext):
    try:
        if not 1950 < int(message.text) < 2015:
            await message.answer("Нормально авшайса!")
        else:
            async with state.proxy() as data:
                data['age'] = 2022 - int(message.text)
            await FSMAdmin.next()
            await message.answer("Какого пола?", reply_markup=gender_markup)
    except:
        await message.answer("Нормально авшайса!")


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer("Каяктан болосун??", reply_markup=cancel_markup)


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"{data['name']}, {data['age']}, {data['gender']}, "
                                     f"{data['region']}\n\n {data['username']}")
    await state.finish()
    await message.answer("Все свободен!")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты!")


def register_handlers_fsm_admin(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
