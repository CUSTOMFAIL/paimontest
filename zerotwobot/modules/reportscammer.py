import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/reportscammer"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **TO REPORT SCAM/SCAMMERS .... TAKE SCREENSHOT OF THE PROOF AND SEND IT TO [SUPPORT](https://t.me/botperosupport) WITH SCAMMER USERNAME  ** \n\n"
  BUTTON = [[Button.url("SUPPORT GRP", "https://t.me/botperosupport")]]
await tbot.send_message(event.chat_id, TEXT,  buttons=BUTTON)
