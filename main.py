import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.getenv("35356899"))
API_HASH = os.getenv("f1e9f66c392270e798b6e95413601ae9")
BOT_TOKEN = os.getenv("8697551682:AAF7lCICDszOwZ6Lz3jbUJbTMhL_VZGtZ4o")

app = Client(
    "ns_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("🤖 NS Music Bot Active ✅")

@app.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply_text("🏓 Pong!")

async def main():
    print("Starting Bot...")
    await app.start()
    print("Bot Started ✅")

    await asyncio.Event().wait()

asyncio.run(main())
