from .throttling import ThrottlingMiddleware
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
