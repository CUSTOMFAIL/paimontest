import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/auction"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **HERE IS ABOUT AUCTION......** \n\n"
  TEXT += "❍ **AS U MAY KNOW WHAT IS AUCTION.... AND HOW PURCHASING IS DONE** \n\n"
  TEXT += "❍ **SO HERE WE BROUGHT AUCTION TO HEXA TO INCREASE THE FUN** \n\n"
  TEXT += "❍ **PLEASE DO NOTE THAT WE ONLY ACCEPT OP 0L, LEGENDARY, SHINY** \n\n"
  TEXT += "❍ **WE ONLY ACCEPT TMS BY TRUSTED SELLERS** \n"
  TEXT += "❍ **FOLLOW THE GIVEN BELOW LINK TO UNDERSTAND MORE* \n\n"
  BUTTON = [
      [
          Button.url("AUCTION GROUP", "https://t.me/hexaauction"),
      ],
      [
          Button.url("AUCTION CHANNEL", "https://t.me/shinyhub_official")
      ],
      [
          Button.url("AUCTION BOT", "https://t.me/hexaauctionbot")
      ]
    ]
  await tbot.send_message(event.chat_id, TEXT,  buttons=BUTTON)
