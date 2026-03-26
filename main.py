import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, InputAudioStream
import yt_dlp

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("✅ Music Bot Started")

@app.on_message(filters.command("play"))
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Song name likho")

    query = " ".join(message.command[1:])
    msg = await message.reply_text(f"🔍 Searching: {query}")

    ydl_opts = {"format": "bestaudio", "quiet": True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)
        url = info["entries"][0]["url"]

    await call_py.join_group_call(
        message.chat.id,
        InputStream(
            InputAudioStream(
                url
            )
        )
    )

    await msg.edit("🎵 Playing in VC...")

@app.on_message(filters.command("stop"))
async def stop(_, message):
    await call_py.leave_group_call(message.chat.id)
    await message.reply_text("⛔ Stopped")

app.start()
call_py.start()
app.idle()
