from config import settings
from loguru import logger
from loguru import Logger


def setup_logger() -> Logger:
    logger.add(
        level=settings.LOGGING_LEVEL,
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="30 KB",
        compression="zip",
        sink="logs/bot.log",
    )
    return logger
