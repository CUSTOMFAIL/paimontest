import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/845d1e212b922a023b0d9.jpg"

@register(pattern=("/chatgroup"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **HERE ARE 3 CHAT GRPS WHERE U CAN TALK RELATED TO HEXA** \n\n"
  TEXT += "❍ **JOIN THESE TO ENJOY HEXA..... INVITE FRIENDS..... MAKE FRIENDS.....** \n\n"

  BUTTON = [
      [
          Button.url("CHATTERPOKE", "https://t.me/ChatterPokeandHexa")
      ],
      [
          Button.url("GANGLAND", "https://t.me/killers69")
      ],
      [
          Button.url("AKATSUKI", "https://t.me/HEXA_AKATSUKI")
      ]
    ]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
