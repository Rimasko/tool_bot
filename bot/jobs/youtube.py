from aiogram import Bot
from aiogram.types import InputFile
from services import YoutubeDownloaderService

import tempfile


async def download_file(bot: Bot, chat_id, video_url, resolution):
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_path = tmpdirname + "/video.mp4"
        file_path = YoutubeDownloaderService.download(video_url, resolution, temp_path)

        await bot.send_video(chat_id, InputFile(file_path))
