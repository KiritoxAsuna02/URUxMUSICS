import asyncio
import os
import random
import re
from typing import Union

import httpx
import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch

from AnonXMusic.utils.formatters import time_to_seconds
from AnonXMusic.utils.database import is_on_off


            if os.path.exists(xyz):
                return xyz
            x.download([link])
            return xyz

        def song_video_dl():
            formats = f"{format_id}+140"
            fpath = f"downloads/{title}"
            ydl_optssx = {
                "format": formats,
                "outtmpl": fpath,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "merge_output_format": "mp4",
                "cookiefile": cookies(),
            }
            x = yt_dlp.YoutubeDL(ydl_optssx)
            x.download([link])

        def song_audio_dl():
            fpath = f"downloads/{title}.%(ext)s"
            ydl_optssx = {
                "format": format_id,
                "outtmpl": fpath,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
                "cookiefile": cookies(),
            }
            x = yt_dlp.YoutubeDL(ydl_optssx)
            x.download([link])

        if songvideo:
            # await loop.run_in_executor(None, song_video_dl)
            # fpath = f"downloads/{title}.mp4"
            fpath = await loop.run_in_executor(
                None, lambda: asyncio.run(download(vidid, video=True))
            )
            return fpath
        elif songaudio:
            # await loop.run_in_executor(None, song_audio_dl)
            # fpath = f"downloads/{title}.mp3"
            fpath = await loop.run_in_executor(
                None, lambda: asyncio.run(download(vidid))
            )
            return fpath
        elif video:
            direct = True
            downloaded_file = await loop.run_in_executor(
                None, lambda: asyncio.run(download(vidid, video=True))
            )
            """if await is_on_off(config.YTDOWNLOADER):
                direct = True
                downloaded_file = await loop.run_in_executor(None, video_dl)
            else:
                proc = await asyncio.create_subprocess_exec(
                    "yt-dlp",
                    "-g",
                    "-f",
                    "best[height<=?720][width<=?1280]",
                    f"{link}",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                )
                stdout, stderr = await proc.communicate()
                if stdout:
                    downloaded_file = stdout.decode().split("\n")[0]
                    direct = None
                else:
                    return"""
        else:
            direct = True
            # downloaded_file = await loop.run_in_executor(None, audio_dl)
            downloaded_file = await loop.run_in_executor(
                None, lambda: asyncio.run(download(vidid))
            )
        return downloaded_file, direct
