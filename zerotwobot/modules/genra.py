import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/aliv"))
async def awake(event):
  TEXT = f"**`Hi I'm Officer Jenny.`** \n\n"
  TEXT += "❍ **I'm Working Properly** \n\n"
  TEXT += f"❍ **My Master : [AYATO](https://t.me/SILVER_KING)** \n\n"
  TEXT += f"❍ **Library Version :** `{telever}` \n\n"
  TEXT += f"❍ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"❍ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  await tbot.send_message(event.chat_id, TEXT)
