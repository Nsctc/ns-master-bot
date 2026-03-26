import os
import asyncio
from pyrogram import Client

try:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    print("API_ID:", API_ID)
    print("API_HASH:", API_HASH)
    print("BOT_TOKEN:", BOT_TOKEN)

    app = Client(
        "bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )

    async def main():
        await app.start()
        print("Bot Started ✅")
        await asyncio.Event().wait()

    asyncio.run(main())

except Exception as e:
    print("ERROR:", e)
