from aiogram import types
from aiogram.dispatcher import FSMContext
from aiojobs import Scheduler
from jobs.youtube import download_file
from loguru import logger
from services import YoutubeDownloaderService

import keyboards
import states.user


async def yt_download_callback(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Отправьте ссылку на видео, которое хотите скачать")
    await states.user.DownloadFromYoutube.insert_link.set()
    await call.message.delete()


async def yt_download_confirm(msg: types.Message, state: FSMContext):
    file_data = await YoutubeDownloaderService.get_file_data(msg.text)

    if file_data is None:
        await msg.reply("Неверная ссылка\nПопробуйте еще раз")
        return

    bot = msg.bot
    await bot.send_photo(msg.chat.id, file_data.thumbnail_url)
    await bot.send_message(
        msg.chat.id,
        f"Название: {file_data.title}\n",
        reply_markup=keyboards.YoutubeMenu.download_menu(file_data.streams),
    )
    await state.update_data(video_url=msg.text)
    await states.user.DownloadFromYoutube.confirm_adding.set()


async def yt_download_file(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        video_url = data["video_url"]

    resolution = call.data.split("_")[1]
    logger.info(resolution)
    scheduler = Scheduler()

    await scheduler.spawn(download_file(call.bot, call.message.chat.id, video_url, resolution))

    await state.finish()
    await states.user.MainMenu.main_menu.set()

    await call.bot.send_message(
        call.message.chat.id, "Главное меню", reply_markup=keyboards.MainMenu.main_menu()
    )
