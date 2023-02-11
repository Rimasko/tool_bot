from aiogram import Bot
from aiogram.types import ParseMode
from pydantic import BaseSettings
from pydantic import RedisDsn


class Settings(BaseSettings):
    BOT_TOKEN: str
    BASE_URL: str

    WEBHOOK_PATH: str = "/tg/webhooks/bot/"
    REDIS_DSN: RedisDsn = RedisDsn("redis://localhost:6379/0")
    ADMINS: list[str] = []
    LOGGING_LEVEL: str = "DEBUG"

    class Config:
        # `.env.prod` takes priority over `.env`
        env_file = ".env", ".env.prod"
        env_file_encoding = "utf-8"


settings = Settings()
bot = Bot(settings.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
