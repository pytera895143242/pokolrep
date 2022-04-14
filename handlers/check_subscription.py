from loader import dp
from aiogram import types
from utils import database
from filters.not_subscribed import Not_Subscribed
from states.subscription import Subscription
import json
from aiogram.dispatcher.storage import FSMContext
from keyboards import social_check_keyboard, menu_keyboard, subscription_check_keyboard

@dp.message_handler(Not_Subscribed())
async def check_subscription(message: types.Message):
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    if database.user_exists(message.from_user.id):
        await message.answer(f'💡Для доступа к боту, подпишись на наш канал, в нём регулярно выходят 🔞 сливы, после чего нажми кнопку - «Я подписался»👇\n\n{config["Bot_Data"]["Channel_Link"]}', reply_markup=subscription_check_keyboard.keyboard)
        await Subscription.waiting.set()
    else:
        database.create_user(message.from_user.id, message.from_user.username)
        await message.answer(f'💡Для доступа к боту, подпишись на наш канал, в нём регулярно выходят 🔞 сливы, после чего нажми кнопку - «Я подписался»👇\n\n{config["Bot_Data"]["Channel_Link"]}', reply_markup=subscription_check_keyboard.keyboard)
        await Subscription.waiting.set()

@dp.message_handler(state=Subscription.waiting)
async def answer_while_waiting(message: types.Message, state: FSMContext):
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    if config['Bot_Data']['Subscription_Required']:
        await message.answer(f'💡Для доступа к боту, подпишись на наш канал, в нём регулярно выходят 🔞 сливы, после чего нажми кнопку - «Я подписался»👇\n\n{config["Bot_Data"]["Channel_Link"]}', reply_markup=subscription_check_keyboard.keyboard)
    else:
        await state.finish()
        text = f"""<b>👋 Привет, {message.from_user.full_name}

🤖 Я - нейросеть, которая ищет приватные фото в тысячах баз по всему интернету.

🔐 Могу найти даже самые скрытые фото, о которых остальные даже и не слышали!

🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram!</b>"""
        photo = open("photo.jpg", 'rb')

        await message.answer_photo(photo = photo, caption = text, reply_markup=menu_keyboard.keyboard)
        await message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)

@dp.callback_query_handler(text='check_subscribtion', state=Subscription.waiting)
async def check_subscribtion(callback: types.CallbackQuery, state: FSMContext):
    if database.get_user(callback.from_user.id)['subscribed']:
        await callback.message.delete()
        text = f"""<b>👋 Привет, {message.from_user.full_name}

        🤖 Я - нейросеть, которая ищет приватные фото в тысячах баз по всему интернету.

        🔐 Могу найти даже самые скрытые фото, о которых остальные даже и не слышали!

        🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram!</b>"""
        photo = open("photo.jpg", 'rb')
        await callback.message.answer_photo(photo = photo, caption = text , reply_markup=menu_keyboard.keyboard)
        await callback.message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)
        await state.finish()
    else:
        await callback.answer('Вы не подписались!')

@dp.chat_member_handler(state='*')
async def handle_channel_actions(chat_member: types.ChatMemberUpdated):
    if chat_member.old_chat_member.status == 'left' and (chat_member.new_chat_member.status == 'member' or chat_member.new_chat_member.status == 'creator'):
        database.update_user(chat_member.from_user.id, 'subscribed', 1)
    elif chat_member.old_chat_member.status == 'member' and chat_member.new_chat_member.status == 'left':
        database.update_user(chat_member.from_user.id, 'subscribed', 0)