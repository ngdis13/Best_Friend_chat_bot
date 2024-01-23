from aiogram import Router, F
from aiogram.types import Message

from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)
from aiogram.filters import Command, CommandObject


from keyboards import reply

router = Router()



@router.message(Command('start'))
async def start(message: Message):
    content = as_list(
        as_marked_section(
            Bold(f'♡ Hello, {message.from_user.first_name} ♡'),
            '\n\n',
            marker=''
    )
    )
    await message.answer(**content.as_kwargs(), reply_markup=reply.main)

