import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/hexa"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Officer Jenny.** \n\n"
  TEXT += "❍ **This is HeXa Command** \n\n"
  TEXT += "❍ **List Of Pokemon : [HERE](https://telegra.ph/Pokemon-05-21-2)** \n\n"
  TEXT += "❍ **Use /<pokemon name> To display its best nature \n\n"
  TEXT += "❍ **Use /natures To list natures command \n\n"
  TEXT += "❍ **Use /types To list types command \n\n"
  TEXT += "❍ *Soon .... We will add Rest 700+ Pokemon* \n\n"
  BUTTON = [[Button.url("HeXa", "https://t.me/HeXamonbot?start=1ivnfl3nt91at")]]
  await tbot.send_message(event.chat_id, TEXT,  buttons=BUTTON)
