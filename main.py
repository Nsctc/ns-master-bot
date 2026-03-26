import os
from pyrogram import Client

API_ID = int(os.getenv("35356899"))
API_HASH = os.getenv("f1e9f66c392270e798b6e95413601ae9")
BOT_TOKEN = os.getenv("8697551682:AAF7lCICDszOwZ6Lz3jbUJbTMhL_VZGtZ4o")

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

app.start()
print("Bot Started ✅")

import time
while True:
    time.sleep(10)
