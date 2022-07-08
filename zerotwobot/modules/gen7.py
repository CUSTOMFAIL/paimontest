import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/gen7"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **LIST OF POKEMON IN GENERATION 7** \n\n"
  BUTTON = [[Button.url("GEN7", "https://telegra.ph/GEN7-07-08")]]
  await tbot.send_message(event.chat_id, TEXT,  buttons=BUTTON)
