from aiogram.types import InlineKeyboardMarkup
from keyboards.inline.consts import InlineConstructor
from services.youtube import StreamData
from typing import Any


class YoutubeMenu(InlineConstructor):
    @classmethod
    def download_menu(cls, streams: list[StreamData]) -> InlineKeyboardMarkup:
        schema = [len(streams)]
        actions: list[Any] = []

        for stream in streams:
            actions.append(
                {
                    "text": f"{stream.resolution} {stream.size}mb",
                    "callback_data": f"resolution_{stream.resolution}",
                }
            )

        return cls._create_kb(actions, schema)
