import time

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove


from keyboards import reply, inline, builders, fabric

router = Router()

@router.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == 'мой дневник эмоций':
        await message.answer("твой дневник эмоций", reply_markup=reply.emotional_diary)
    elif msg == 'добавить эмоцию':
        await message.answer("как ты себя чувствуешь? оцени свое состояние от 0 до 10")
    elif msg == 'посмотреть статистику':
        await message.answer("эмоциональный график")



    elif msg == 'начать диалог с другом':
        await message.answer("диалог с другом:", reply_markup=reply.dialog)
    # if msg == 'начать диалог':
    #     await message.answer("диалог с другом:", reply_markup=reply.dialog)    подключить чат джп
    elif msg == 'закончить диалог':
        await message.answer("хорошо поболтали, возвращайся снова, я всегда рядом")

    elif msg == 'мгновенная мотивация':
        await message.answer("мгновенная мотивация:")     #чат



    elif msg == 'подписка на ежедневную мотивацию':
        await message.answer("оформление подписки на ежедневную мотивацию", reply_markup=reply.sub)
    elif msg == 'время':
        await message.answer("выбери время в которое я буду присылать тебе сообщение")
    elif msg == 'поменять время':
        await message.answer("напиши в какое время ты бы хотел получать сообщение")
    elif msg == 'отменить подписку':
        await message.answer("очень жаль, что ты больше не хочешь получать ежедневную мотивацию от меня")


    elif msg == 'вернуться в меню':
        await message.answer("ты вернулся в меню", reply_markup=reply.main)

