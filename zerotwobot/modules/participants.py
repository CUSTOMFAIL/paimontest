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
          Button.url("3. Duke", "https://t.me/CageOfSolutions"),
          Button.url("4. Ishtar", "https://t.me/sishtar_sensei")
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
      ],
      [
          Button.url("11. Shubh", "https://t.me/Angry_bird_0"),
          Button.url("12. Satya", "https://t.me/satya94925")
      ],
      [
          Button.url("13. Irfan", "https://t.me/Candycrush001"),
          Button.url("14. Krish", "https://t.me/Nothing8002")
      ],
      [
          Button.url("15. Sam", "https://t.me/i_am_vey_bussy_person"),
          Button.url("16. Apex", "https://t.me/Apex_boss")
      ],
      [
          Button.url("17. Vyanki", "https://t.me/CaptainDOfficial"),
          Button.url("18. Sooryadev", "https://t.me/sooryadev45")
      ],
      [
          Button.url("19. Demonking", "https://t.me/Demonking2004"),
          Button.url("20. RK", "https://t.me/Lovelyxyz")
      ],
      [
          Button.url("21. Monster", "https://t.me/Monster79990"),
          Button.url("22. Subansh", "https://t.me/Subansh41")
      ],
      [
          Button.url("23. Vibhu", "https://t.me/lucarioaurra"),
          Button.url("24. Abid", "https://t.me/asta_kunn")
      ]
    ]
  await tbot.send_message(event.chat_id, TEXT,  buttons=BUTTON)
