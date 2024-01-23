import asyncio
from aiogram import Bot, Dispatcher


from config_reader import config


import handlers
from database import DataBase as db
from handlers import bot_messages, user_commands, questionaire


from config_reader import config        #импорт токена из config_reader



async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode='HTML')
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        bot_messages.router
    )

    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())



