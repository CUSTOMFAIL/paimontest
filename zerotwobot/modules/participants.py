import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/participants"))
async def awake(event):
  TEXT = f"**Here are the list of participants** \n\n"
  TEXT += "❍ **Limited seats be quick** \n\n"
  BUTTON = [
      [
          Button.url("1. Kaustubh", "https://t.me/kaustubh_kurosaki"),
          Button.url("2. Dhruva", "https://t.me/nothing_here_get_lost")
      ],
      [
          Button.url("3. Ishtar", "https://t.me/ishtar_sensei"),
          Button.url("4. Sooryadev", "https://t.me/sooryadev45")
      ],
      [
          Button.url("5. Ekansh", "https://t.me/legendeku"),
          Button.url("6. Ded Lord", "https://t.me/hell_lord6124")
      ],
      [
          Button.url("7. Vansh", "https://t.me/vc5123"),
          Button.url("8. Pokestar", "https://t.me/poke_fan_777")
      ],
      [
          Button.url("9. Buttercup", "https://t.me/itz_butter_cup"),
          Button.url("10. Morty", "https://t.me/Morty_4_life")
      ]
    ]
  await tbot.send_message(event.chat_id, TEXT,  buttons=BUTTON)
