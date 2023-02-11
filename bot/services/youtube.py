from dataclasses import dataclass
from pytube import YouTube


@dataclass
class StreamData:
    resolution: str
    size: str


@dataclass
class YoutubeFile:
    title: str
    thumbnail_url: str
    streams: list[StreamData]


class YoutubeDownloaderService:
    @classmethod
    async def get_file_data(cls, url: str):
        yt = YouTube(url)

        return YoutubeFile(
            title=yt.title,
            thumbnail_url=yt.thumbnail_url,
            streams=[
                StreamData(resolution=stream.resolution, size=stream.filesize_mb)
                for stream in yt.streams.filter(progressive=True)
            ],
        )

    @classmethod
    def download(cls, url: str, resolution: str, output_path: str):
        yt = YouTube(url)
        return yt.streams.filter(resolution=resolution).first().download(output_path)
