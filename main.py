from pyrogram import Client, filters
import os

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION"]

AUTO_REPLY = """Antidote abhi off hai.

Agar koi kaam hai to is par contact karo:
https://antidote69.lovable.app
"""

app = Client(
    "antidote",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

@app.on_message(filters.reply & filters.group)
async def auto_reply(client, message):
    replied = message.reply_to_message

    if (
        replied
        and replied.from_user
        and replied.from_user.is_self
    ):
        await message.reply_text(AUTO_REPLY)

app.run()
