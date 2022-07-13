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
  TEXT += "❍ **FACTIONS** \n\n"
  TEXT += "❍ **Q. What are Factions and Why were they made?** \n\n"
  TEXT += "❍ **   Many of you are bored of HeXa and it is dying.\nSo here's a thought, how about we have guilds/clans/teams/factions in HeXa,  interesting isn't it?\nWouldn't it be fun if you have a competition of which team's the best? Yeah precisely, that's why factions exist.\n\n\n1) Have a competitive spirit\n2) Tournaments\n3) Play for pride and glory\n\nFactions are basically a team.\n\n\nThe reason Factions were created was to encourage the spirit of competition and teamwork among the players. Also to help newbies get guidance from some of the experienced players in HeXa and get rivals from the same and other factions to compete against and get stronger. \n\n\nEach faction is lead by a captain that will guide you to achieve greatness.\n\n\nBeing in any of the Offical Factions allows you to be eligible for participating in the HeXa tournament. We hold competition and tournaments ever now and then and each of the tournament has a different theme to it. Factions fight against each other for gaining points. The Faction with highest points is crowned champions and are awarded for the same.** \n\n"
  TEXT += "❍ **PLEASE DO NOTE THAT WE ONLY ACCEPT OP 0L, LEGENDARY, SHINY** \n\n"
  TEXT += "❍ **Q. What are the official factions?** \n\n"
  TEXT += "❍ **• BETA\n• THETA\n• GAMMA  ** \n\n"
  TEXT += "❍ **USE FACTIONS COMMANDS TO KNOW MORE ABOUT THEM /theta, /gamma, /beta** \n\n"
  BUTTON = [
      [
          Button.url("FACTIONS", "https://t.me/HeXaFaction"),
      ],
    ]
  await tbot.send_message(event.chat_id, TEXT,  buttons=BUTTON)
