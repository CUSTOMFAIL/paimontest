import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/1b0aa314c1c03883384ea.mp4"

@register(pattern=("/theta"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **TEAM THETA** \n\n"
  TEXT += f"❍ **CAPTAIN : [AIZEN](https://t.me/hell_knight_01)** \n\n"
  TEXT += f"❍ **VICE CAP : [EREN](https://t.me/ereh_kun)** \n\n"
  TEXT += f"❍ **IF U WANT TO JOIN TEAM THETA USE THE BUTTON BELOW\n\n"
  BUTTON = [
      [
          Button.url("ϑCAPTAINϑ", "https://t.me/hell_knight_01"),
          Button.url("ϑVICE CAPϑ", "https://t.me/ereh_kun")
      ],
      [
          Button.url("ϑTEAM THETAϑ", "https://t.me/theta_clique")
      ],
      [
          Button.url("ϑ HOW TO JOIN THETA ϑ", "https://t.me/ThetaRecruitment_bot")
      ]
    ]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
