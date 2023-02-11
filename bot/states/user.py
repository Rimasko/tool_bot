from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup


class MainMenu(StatesGroup):
    main_menu = State()
    instagram = State()
    youtube = State()
    pdf = State()


class DownloadFromYoutube(StatesGroup):
    insert_link = State()
    confirm_adding = State()


class DownloadFromInstagram(StatesGroup):
    insert_link = State()
    confirm_adding = State()
