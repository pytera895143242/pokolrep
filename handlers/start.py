from loader import dp
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = f"""<b>👋 Привет, {message.from_user.full_name}

🤖 Я - нейросеть, которая ищет приватные фото в тысячах баз по всему интернету.
 
🔐 Могу найти даже самые скрытые фото, о которых остальные даже и не слышали!

🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram!</b>"""
    photo = open("photo.jpg", 'rb')

    if not database.user_exists(message.from_user.id):
        database.create_user(message.from_user.id, message.from_user.username)
        if message.get_args() != '':
            if database.user_exists(message.get_args()):
                database.update_user(message.from_user.id, 'invited_by', message.get_args())
        await message.answer_photo(photo = photo, caption = text, reply_markup=menu_keyboard.keyboard)
        await message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)
    else:
        await message.answer_photo(photo = photo, caption = text, reply_markup=menu_keyboard.keyboard)
        await message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)