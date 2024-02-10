from aiogram import Router, F
from aiogram.types import Message

from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)
from aiogram.filters import Command, CommandObject

from aiogram import types


from keyboards import reply

from chat_ai_connect import chat_ai

router = Router()



@router.message(Command('start'))
async def start(message: Message):
    content = as_list(
        as_marked_section(
            Bold(f'♡ Hello, {message.from_user.first_name} ♡'),
            '\n\n',
            Bold('Я - твой лучший друг Капибара и я готов помочь тебе в любую минуту 🥺'),
            '\n\n',
            'Я могу:',
            '\n',
            '1. Поболтать с тобой по душам в любое время и обсудить тревожные вопросы',
            '\n',
            '2. Со мной ты можешь отслеживать свой эмоциональный фон с помощью дневника эмоций',
            '\n',
            '3. Если ты чувствуешь нехватку мотивации каждый день, то я могу присылать тебе мотивирующие сообщения, '
            'мы обязательно сможем поднять твою мотивацию!',
            '\n',
            '4. Когда тебе трудно придумать идею для занятия, ты можешь мгновенно получить от меня вдохновение',
            '\n\n',
            'Я всегда на связи, мой дорогой друг!',
            marker=''
    )

    )
    await message.answer(**content.as_kwargs(), reply_markup=reply.main)

@router.message()
async def friend_dialog(message: types.Message):
    await message.answer('Привет! Я твой друг, расскажи, как твои дела?')

    while True:
        if message.text != 'закончить диалог':
            msg = message.text
            await message.answer(chat_ai.ChatAi.gpt_chat(msg))
            print(msg)
            continue

