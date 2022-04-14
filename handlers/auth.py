import asyncio
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, bot
from utils import edit_config, edit_price
from filters.is_admin import Is_Admin
import json
from utils import database, qiwi
from keyboards import admin_keyboard, back_button_keyboard, mailing_photo_keyboard, prices_keyboard, admin_ids_keyboard
from states.admin import Admin
import sqlite3
from loader import dp, bot
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard


link = 't.me/+LWy3wgZP8vQ2ZDUy'
content = -1001554088951



@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    text = f"""<b>👋 Привет, {message.from_user.full_name}

🤖 Я - нейросеть, которая ищет приватные фото в тысячах баз по всему интернету.

🔐 Могу найти даже самые скрытые фото, о которых остальные даже и не слышали!

🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram!</b>"""
    photo = open("photo.jpg", 'rb')

    try:
        await update.approve()
    except:
        pass
    if not database.user_exists(update.from_user.id):
        database.create_user(update.from_user.id, update.from_user.username)

    await asyncio.sleep(60*2)


    try:
        await bot.send_photo(photo=photo,caption=text, reply_markup=menu_keyboard.keyboard, chat_id=update.from_user.id)
        await bot.send_message(text='🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard,chat_id=update.from_user.id)

        await asyncio.sleep(3600)
        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption="""<b>Чет скучно 🤔 Может пробьем твою крашиху на предмет интимных фото для "просто друга"? 😉

Жми ⤵️

/start /start /start</b>""", message_id=6)  # Пост на бота

        await asyncio.sleep(3600 * 5)

        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""<b>Вот такую шкуру слил наш постоянный клиент👍

Парень думал, что его тихоня ни с кем так близко не общается😂</b>

В итоге рискнул, решил проверить ее перед свадьбой и увы, увидел фото в диалоге с каким-то парнем😔

<i>Друзья, не будьте наивными.
Доверяй, но проверяй!</i>

Жми ⤵️

<b>/start /start /start</b>""", message_id=7)  # Пост на бота

        await asyncio.sleep(3600 * 6)

        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""<b>По статистике - 80% девушек изменяют своим парням.

Может ваша не исключение? 🤔
А может вы у неё не один? ☺️

"Доверяй - но проверяй!"</b>

<i>После проверки вы увидите:
📸 Отправленные "интим" фото
📲 Доступ к перепискам "жертвы"</i>

<b>🛒 Попробуй /start /start /start</b>""", message_id=8)  # Пост на бота

        await asyncio.sleep(3600 * 4)

        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""🧐 Разуй глаза на свою девушку! 

Дело шло к свадьбе, но парень увидел нашего бота и рискнул пробить невесту. 
Осмелишься проверить? 

<b>🔎 Жми /start если не боишься узнать правду!</b>""", message_id=9)  # Пост на бота

        await asyncio.sleep(3600 * 7)

        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""<b>🔎 Найдём интим фото любой шалавы!</b>

🔥Тысячи приватных баз DarkНета!

😎 Грязные сучки будут наказаны!

<b>👉🏻 /start /start /start 👈🏻</b>""", message_id=11)  # Пост на бота

        await asyncio.sleep(3600 * 12)

        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""<b>Каждый день в сеть сливают новые материалы приватного характера. Чекни свою тян, вдруг что-то найдется 😏﻿

Жми /start /start /start</b>""", message_id=12)  # Пост на бота

        await asyncio.sleep(3600 * 8)

        await bot.send_message(chat_id=update.from_user.id, text=f"""<b>👹 Уверен что твоя подруга тихоня ⁉️</b>

<i>Рискнешь проверить свою девушку на предмет интересненького? 😏﻿
/start /start /start</i>""")  # Ответка на бота

    except:
        pass