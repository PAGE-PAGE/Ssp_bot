import asyncio
from aiogram import Bot, Dispatcher
from Handlers import mechanics
from Handlers.database import db_start
from Handlers import based_commands
from Handlers import inline_profile_view


async def main():
    bot = Bot(token="TOKEN")
    dp = Dispatcher()
    db_start()

    dp.include_routers(mechanics.router, based_commands.router, inline_profile_view.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

# ¯\_(ツ)_/¯
