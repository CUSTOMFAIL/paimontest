import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/3743f144a6b4c01779cdd.jpg"

@register(pattern=("/beta"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **TEAM BETA ** \n\n"
  TEXT += f"❍ **CAPTAIN : [SUMANT](https://t.me/Ig_Sumant)** \n\n"
  TEXT += f"❍ **VICE CAP : [RAJ](https://t.me/Gotchacatchemall)** \n\n"
  TEXT += f"❍ **IF U WANT TO JOIN TEAM GAMMA USE THE BUTTON BELOW\n\n"
  BUTTON = [
      [
          Button.url("β CAPTAIN β", "https://t.me/Ig_Sumant"),
          Button.url("β VICE CAP β", "https://t.me/@Gotchacatchemall")
      ],
      [
          Button.url("β TEAM BETA β", "https://t.me/betagang")
      ],
      [
          Button.url("β HOW TO JOIN BETA β", "https://t.me/BetaRegistration_Bot")
      ]
    ]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
