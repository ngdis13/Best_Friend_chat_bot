import time

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove


from keyboards import reply, inline, builders, fabric

router = Router()

@router.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == 'мой дневник эмоций':
        await message.answer("Ты попал в дневник эмоций!📔\n\nЗдесь ты можешь добавлять в свой виртуальный дневник свое "
                             "эмоциональное состояние, которое будешь оценивать каждый день от 0 до 10 \n\nА еще ты можешь посмотреть свой эмоциональный график, чтобы оценить стабильность своего "
                             "эмоционального фона",reply_markup=reply.emotional_diary)
    elif msg == 'добавить эмоцию':
        await message.answer("как ты себя чувствуешь?🫶🏻 оцени свое состояние от 0 до 10")
    elif msg == 'посмотреть статистику':
        await message.answer("твой эмоциональный график за последний месяц:")



    elif msg == 'закончить диалог':
        await message.answer("Хорошо поболтали, возвращайся снова, я всегда рядом!")

    elif msg == 'мгновенная мотивация':
        await message.answer("ты классный")     #чат



    elif msg == 'подписка на ежедневную мотивацию':
        await message.answer("Ух-ты! Ты зашел в раздел подписки на ежедневную рассылку мотивации!", reply_markup=reply.sub)
    elif msg == 'оформить подписку':
        await message.answer("Выбери время в которое я буду присылать тебе мотивирующее сообщение")
    elif msg == 'поменять время':
        await message.answer("Напиши в какое время ты бы хотел получать сообщение")
    elif msg == 'отменить подписку':
        await message.answer("очень жаль, что ты больше не хочешь получать ежедневную мотивацию от меня")


    elif msg == 'вернуться в меню':
        await message.answer("ты вернулся в меню", reply_markup=reply.main)

