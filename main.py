import os
import asyncio
from pyrogram import Client

try:
    API_ID = int(os.getenv("35356899"))
    API_HASH = os.getenv("f1e9f66c392270e798b6e95413601ae9")
    BOT_TOKEN = os.getenv("8697551682:AAF7lCICDszOwZ6Lz3jbUJbTMhL_VZGtZ4o")

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
