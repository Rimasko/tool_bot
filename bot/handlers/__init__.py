from .errors import message_not_modified
from .errors import message_to_delete_not_found
from .user import bot_cancel
from .user import bot_cancel_handler
from .user import bot_help
from .user import bot_menu
from .user import bot_start
from .youtube import yt_download_callback
from .youtube import yt_download_confirm
from .youtube import yt_download_file
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import CommandHelp
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters import Text
from aiogram.utils import exceptions

import keyboards
import states.user as user_states


def setup(dp: Dispatcher):
    # User handlers
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(bot_menu, Command(commands=["menu"]))
    dp.register_message_handler(bot_menu, Command(commands=["start"]), state="*")
    dp.register_callback_query_handler(
        bot_cancel_handler,
        lambda c: c.data == keyboards.MainMenuCallbacks.reject,
        state="*",
    )
    dp.register_message_handler(bot_cancel, Command(commands=["cancel"]), state="*")

    # Errors handlers
    dp.register_errors_handler(message_not_modified, exception=exceptions.MessageNotModified)
    dp.register_errors_handler(
        message_to_delete_not_found,
        exception=exceptions.MessageToDeleteNotFound,
    )

    # Youtube handlers
    dp.register_callback_query_handler(
        yt_download_callback,
        lambda c: c.data == keyboards.MainMenuCallbacks.youtube,
        state=user_states.MainMenu.main_menu,
    )
    dp.register_message_handler(
        yt_download_confirm,
        state=user_states.DownloadFromYoutube.insert_link,
    )
    dp.register_callback_query_handler(
        yt_download_file,
        lambda m: m.data.startswith("resolution_"),
        state=user_states.DownloadFromYoutube.confirm_adding,
    )
    # Instagram handlers
