import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/gen3"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **LIST OF POKEMON IN GENERATION 3** \n\n"
  BUTTON = [[Button.url("GEN3", "https://telegra.ph/GEN3-07-08")]]
  await tbot.send_message(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
