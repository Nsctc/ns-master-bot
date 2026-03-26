from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def controls():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⏸ Pause", callback_data="pause")],
        [InlineKeyboardButton("⏭ Skip", callback_data="skip")]
    ])
