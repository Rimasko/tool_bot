from aiogram import types
from aiogram.dispatcher import FSMContext
from contextlib import suppress

import keyboards.main_menu
import states.user


async def bot_menu(msg: types.Message, state: FSMContext):
    await msg.reply(
        "Главное меню",
        reply_markup=keyboards.main_menu.MainMenu.main_menu(),
    )

    if await state.get_state() is not None:
        with suppress(KeyError):
            await state.finish()

    await states.user.MainMenu.main_menu.set()
