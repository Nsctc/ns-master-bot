import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# START command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello 👋 Bot is working!")

# PING command
@app.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply_text("Pong 🏓")

async def main():
    await app.start()
    print("Bot Started Successfully ✅")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
