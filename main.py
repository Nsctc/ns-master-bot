import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Bot Working ✅🔥")

async def main():
    await app.start()
    print("Bot Started Successfully ✅")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
