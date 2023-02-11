from aiogram import Dispatcher
from aiogram import types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.utils.executor import start_webhook
from aiojobs import Scheduler
from config import bot
from config import settings
from utils import misc


WEBHOOK_URL = f"{settings.BASE_URL}{settings.WEBHOOK_PATH}"


def setup_logging(dp: Dispatcher):
    logger = misc.setup_logger()
    dp["business_logger"] = logger
    dp["business_logger_init"] = {"type": "business"}
    dp["aiogram_logger"] = logger
    dp["aiogram_logger_init"] = {"type": "aiogram"}


async def on_startup(dp: Dispatcher):
    import filters
    import handlers
    import middlewares

    middlewares.setup(dp)
    filters.setup(dp)
    handlers.setup(dp)
    webhook_logger = dp["aiogram_logger"].bind(webhook_url=WEBHOOK_URL)
    webhook_logger.info("Configured webhook")
    webhook_logger.info(WEBHOOK_URL)
    dp["scheduler"] = Scheduler()

    await dp.bot.set_webhook(WEBHOOK_URL, allowed_updates=types.AllowedUpdates.all())


async def on_shutdown(dp: Dispatcher):
    dp["aiogram_logger"].warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    dp["aiogram_logger"].warning("Bot !")


if __name__ == "__main__":
    storage = RedisStorage2(
        host=settings.REDIS_DSN.host,
        port=settings.REDIS_DSN.port,
    )
    dp = Dispatcher(bot, storage=storage)
    setup_logging(dp)

    start_webhook(
        dispatcher=dp,
        webhook_path=settings.WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host="localhost",
        port=5005,
    )
