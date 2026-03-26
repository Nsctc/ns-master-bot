from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from handlers.play import play_handler
from handlers.controls import controls
from config import *

app = Client("bot",35356899 , api_hash=f1e9f66c392270e798b6e95413601ae9, bot_token=8697551682:AAGHZFUV7I6HC9NfPHZS1DWvm24kUJpNn8E)
call = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply("🎵 NS Master Music Bot", reply_markup=controls())

@app.on_message(filters.command("play"))
async def play(_, message):
    await play_handler(app, message, call)

app.start()
call.start()

import asyncio
asyncio.get_event_loop().run_forever()
