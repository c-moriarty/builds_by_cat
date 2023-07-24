import asyncio #асинхронный запуск бота
import logging #для настройки логгирования

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode #содержит настройки разметки сообщений
from aiogram.fsm.storage.memory import MemoryStorage #хранилище данных для состояний пользователя

import config #настройки бота
from handlers import router #пока пустой


async def main(): #в этой функции запускается сам бот
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML) #объект бота с токеном; parse_mode отвечает за разетку сообщений по умолчанию
    dp = Dispatcher(storage=MemoryStorage()) #объект диспетчера; storage=MemoryStorage() отвечает за то, что все данные, не сохраненные в БД, будут стерты при перезапуске
    dp.include_router(router) #подключает к диспетчеру все обработчики, которые используют router
    await bot.delete_webhook(drop_pending_updates=True) #удаляет все обновления, которые произошли после последнего завершения работы бота, чтобы бот обрабатывал только те сообщения, которые пришли ему непосредственно во время его работы, а не за всё время.
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) #запускает бота


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

