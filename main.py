import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("✅ Bot Working Successfully!")

@app.on_message(filters.command("ping"))
async def ping_handler(client, message):
    await message.reply_text("🏓 Pong!")

async def main():
    await app.start()
    print("🔥 Bot Started")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
