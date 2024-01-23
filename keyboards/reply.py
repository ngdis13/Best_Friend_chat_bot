from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardRemove
)



main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='мой дневник эмоций'),
            KeyboardButton(text='мгновенная мотивация')
        ],
        [
            KeyboardButton(text='подписка на ежедневную мотивацию'),
            KeyboardButton(text='начать диалог с другом')
        ],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='выбрать функцию из меню',
    selective=True
)

sub = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='время'),
        KeyboardButton(text='поменять время'),
        KeyboardButton(text='отменить подписку')
    ],

    [
        KeyboardButton(text='вернуться в меню')
    ]
],
    resize_keyboard=True
)


dialog = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='начать диалог'),
        KeyboardButton(text='закончить диалог'),
    ],

    [
        KeyboardButton(text='вернуться в меню')
    ]
],
    resize_keyboard=True
)

emotional_diary = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='добавить эмоцию'),
        KeyboardButton(text='посмотреть статистику'),
    ],

    [
        KeyboardButton(text='вернуться в меню')
    ]
],
    resize_keyboard=True
)


rmk = ReplyKeyboardRemove()