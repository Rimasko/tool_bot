from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import MenuButtonDefault
from aiogram.utils.exceptions import BadRequest
from aiogram.utils.exceptions import InvalidQueryID


async def set_menu(bot, chat_id):
    try:
        await bot.set_chat_menu_button(chat_id, MenuButtonDefault())
    except BadRequest:
        pass


async def bot_cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    # await msg.delete_reply_markup()
    await set_menu(msg.bot, msg.chat.id)


async def bot_cancel_handler(call: types.CallbackQuery, state: FSMContext):
    # from bot import bot

    await state.finish()
    try:
        await call.message.delete_reply_markup()
    except InvalidQueryID:
        pass
    await set_menu(call.bot, call.message.chat.id)
