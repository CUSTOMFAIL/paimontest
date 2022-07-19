import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/f8ddc8b6ca5865e567f12.mp4"

@register(pattern=("/tournament"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "**DICE TOURNAMENT** \n\n\n"
  TEXT += "**RULES** \n\n"
  TEXT += f"❍ ** Participation fee - 250** \n\n"
  TEXT += f"❍ ** Only 36 players** \n\n"
  TEXT += f"❍ ** 6 TEAMS, Each team 6 players** \n\n"
  TEXT += f"❍ ** Banned- Slaking, deoxys, phero** \n\n"
  TEXT += f"❍ ** Players will roll dice to join the team whose numbers come on dice. If team full and a player get the number of full team then re roll.** \n\n"
  TEXT += f"❍ ** To decide team leaders any experinced player will be chosen** Team leader role will be only for matchmaking not for ordering. \n\n"
  TEXT += f"❍ ** Matchmaking depends will depend on dice. Organiser will role dice. Which ever number come the dice will go to that team leader and then team leader will role to battle which ever team they roll on.** \n\n"
  TEXT += f"❍ ** Interteam matches will also depend on dice** \n\n"
  TEXT += f"❍ ** 0L or 6L will depend on dice ** \n\n"
  TEXT += f"❍ ** No. Of pokemon in a team will depend on dice** \n\n"
  TEXT += f"❍ ** Fair or Luck will depend on dice** \n\n"
  TEXT += f"❍ ** Inshort everything depends on dice** \n\n"
  TEXT += f"❍ ** Use /participants for participants list** \n\n"
  TEXT += f"❍ ** Use /prizepool for prizepool** \n\n"
  TEXT += f"❍ ** PRIZE** \n"
  TEXT += f" ** 1st - 15k + X MOD (1 MONTH)** \n"
  TEXT += f" ** 2nd - 10k ** \n"
  TEXT += f" ** 3rd - 5k**"
  BUTTON = [
      [
          Button.url("TOURNAMENT", "https://t.me/xmodnews/8"),
          Button.url("TOUR GROUP", "https://t.me/dicetour")
      ],
      [
          Button.url("X MODS", "https://t.me/xmodnews/2")
      ],
      [
          Button.url("ORGANISER", "https://t.me/bajikeisukekun")
      ]
    ]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
