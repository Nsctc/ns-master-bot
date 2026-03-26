from pyrogram import filters
from yt_dlp import YoutubeDL
from queue import add
from database import songs
from pytgcalls.types.input_stream import AudioPiped

async def play_handler(client, message, call):
    query = message.text.split(None, 1)[1]

    with YoutubeDL({"format": "bestaudio"}) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        url = info['url']
        title = info['title']

    add(message.chat.id, url)
    songs.insert_one({"title": title})

    await call.join_group_call(message.chat.id, AudioPiped(url))
    await message.reply(f"🎶 Playing: {title}")
