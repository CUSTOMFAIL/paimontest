import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/xmod"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
  TEXT += "❍ **X   M O D** \n\n"
  TEXT += "❍ **WHAT IS XMOD?** \n\n"
  TEXT += "❍ **X MOD IS GROUP OF PEOPLE WHO HOLD POWER WITHIN OFFICER JENNY TO GLOBALLY BAN SCAM/SCAMMER. XMOD PEOPLE ALSO CONDUCT AUCTION, TOURNAMENTS AND MANYMORE.... AND THEY ALSO HELP IN TRADE BY BECOMING MODERATOR .... AS IF ADMIN IS OFFLINE THEN X MOD CAN SERVE AS MIDDLE MAN IN TRADE. THEY WILL MAKE SURE THAT NO SCAM OCCURS. THEY WILL BE MOST TRUSTED. {X MOD IS NOT A FEDERATION}** \n\n"
  TEXT += "❍ **HOW TO IDENTIFY IS A PERSON IS X MOD OR NOT? AND WHAT IS A SCAMMER USES X MOD TAG?** \n"
  TEXT += "❍ **ALTHOUGH X MODS WILL USE X MOD TAG IN NAME BUT TO IDENTIFY IF A PERSON IS X MOD OR NOT USE /INFO ON THAT PERSON WITH OFFICER JENNY. IF THAT PERSON IS X MOD ... OFFICER JENNY WILL SHOW RANKED AS X MOD. TO GET LIST OF X MOD CLICK ON THE BUTTON GIVEN BELOW** \n\n"
  TEXT += "❍ **HOW CAN ANYONE BECOME X MOD?** \n\n"
  TEXT += "❍ **U CAN BECOME X MOD IF YOU ARE TRUSTED BY OWNER OR THROUGH RECOMMENDATION BY OTHER X MOD** \n\n"
  BUTTON = [
      [
          Button.url("X MOD NEWS", "https://t.me/xmodnews"),
      ],
      [
          Button.url("X MOD BANS", "https://t.me/xmodbans")
      ],
      [
          Button.url("X MOD LIST", "https://t.me/xmodnews/3")
      ]
    ]
  await tbot.send_message(event.chat_id, TEXT,  buttons=BUTTON)
