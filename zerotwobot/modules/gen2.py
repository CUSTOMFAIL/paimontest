import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/gen2"))
async def awake(event):
  TEXT = f"`+-----------+------------+\n|🌟Chikorita|🌟Bayleef   |\n|🌟Meganium |🌟Cyndaquil |\n|🌟Quilava  |🌟Typhlosion|\n|🌟Totodile |🌟Feraligatr|\n|🌟Croconaw |🌟Sentret   |\n|🌟Furret   |🌟Hoothoot  |\n|🌟Noctowl  |🌟Ledyba    |\n|🌟Ledian   |🌟Spinarak  |\n|🌟Ariados  |🌟Crobat    |\n|🌟Chinchou |🌟Lanturn   |\n|🌟Pichu    |🌟Cleffa    |\n|🌟Igglybuff|🌟Togepi    |\n|🌟Togetic  |🌟Natu      |\n|🌟Xatu     |🌟Mareep    |\n|🌟Flaaffy  |🌟Ampharos  |\n|🌟Bellossom|🌟Marill    |\n|🌟Azumarill|🌟Sudowoodo |\n|🌟Politoed |🌟Hoppip    |\n|🌟Skiploom |🌟Jumpluff  |\n|🌟Aipom    |🌟Sunkern   |\n|🌟Sunflora |🌟Yanma     |\n|🌟Wooper   |🌟Quagsire  |\n|🌟Espeon   |🌟Umbreon   |\n|🌟Murkrow  |🌟Slowking  |\n|🌟Unown    |🌟Misdreavus|\n|🌟Wobbuffet|🌟Girafarig |\n|🌟Pineco   |🌟Forretress|\n|🌟Dunsparce|🌟Gligar    |\n|🌟Steelix  |🌟Snubbull  |\n|🌟Granbull |🌟Qwilfish  |\n|🌟Scizor   |🌟Shuckle   |\n|🌟Heracross|🌟Sneasel   |\n|🌟Teddiursa|🌟Ursaring  |\n|🌟Slugma   |🌟Magcargo  |\n|🌟Swinub   |🌟Piloswine |\n|🌟Corsola  |🌟Remoraid  |\n|🌟Octillery|🌟Delibird  |\n|🌟Mantine  |🌟Skarmory  |\n|🌟Houndour |🌟Houndoom  |\n|🌟Kingdra  |🌟Phanpy    |\n|🌟Donphan  |🌟Porygon2  |\n|🌟Stantler |🌟Smeargle  |\n|🌟Tyrogue  |🌟Hitmontop |\n|🌟Smoochum |🌟Elekid    |\n|🌟Magby    |🌟Miltank   |\n|🌟Blissey  |🌟Raikou    |\n|🌟Entei    |🌟Suicune   |\n|🌟Larvitar |🌟Pupitar   |\n|🌟Tyranitar|🌟Lugia     |\n|🌟Ho-Oh    |🌟Celebi    |\n+------------+------------+`"
  await tbot.send_message(event.chat_id, TEXT)
  
