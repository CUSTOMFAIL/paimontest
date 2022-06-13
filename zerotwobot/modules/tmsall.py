import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/tms2"))
async def awake(event):
  TEXT = f"`+━━━━+━━━━━━━━━━━━━━+━━━+━━━+\n| No.|     NAME     |PWR|ACC|\n+━━━━+━━━━━━━━━━━━━━+━━━+━━━+\n|TM02|Dragon claw   | 80|100|\n|TM03|Psyshock      | 80|100|\n|TM09|Venoshock     | 65|100|\n|TM10|Hidden power  | 60|100|\n|TM13|Ice Beam      | 90|100|\n|TM14|Blizzard      |110| 70|\n|TM15|Hyper Beam    |150| 90|\n|TM22|Solar Beam    |120|100|\n|TM23|Smack Down    | 50|100|\n|TM24|Thunderbolt   | 90|100|\n|TM25|Thunder       |110| 70|\n|TM26|Earthquake    |100|100|\n|TM28|Leech Life    | 80|100|\n|TM29|Psychic       | 90|100|\n|TM30|Shadow Ball   | 80|100|\n|TM31|Brick Break   | 75|100|\n|TM34|Sludge Wave   | 95|100|\n|TM35|Flamethrower  | 90|100|\n|TM36|Sludge Bomb   | 90|100|\n|TM38|Fire Blast    |110| 85|\n|TM39|Rock Tomb     | 60| 95|\n|TM40|Aerial Ace    | 60|100|\n|TM42|Facade        | 70|100|\n|TM43|Flame Charge  | 50|100|\n|TM46|Thief         | 60|100|\n|TM47|Low Sweep     | 65|100|\n|TM48|Round         | 60|100|\n|TM49|Echoed Voice  | 40|100|\n|TM50|Ovearheat     |130| 90|\n|TM51|Steel Wings   | 70| 90|\n|TM52|Focus Blast   |120| 70|\n|TM53|Energy Ball   | 90|100|\n|TM54|False swipe   | 40|100|\n|TM55|Scald         | 80|100|\n|TM57|Charge Beam   | 50| 90|\n|TM58|Sky Drop      | 60|100|\n|TM59|Brutal Swing  | 60|100|\n|TM62|Acrobatics    | 55|100|\n|TM65|Shadow Claw   | 70|100|\n|TM66|Payback       | 50|100|\n|TM67|Smart Strike  | 70|100|\n|TM68|Giga Impact   |150| 90|\n|TM71|Stone Edge    |100| 80|\n|TM72|Volt Switch   | 70|100|\n|TM76|Fly           | 90| 95|\n|TM78|Bulldoze      | 60|100|\n|TM79|Frost Breath  | 60| 90|\n|TM80|Rock Slide    | 75| 90|\n|TM81|X-Scissor     | 80|100|\n|TM82|Dragon Tail   | 60| 90|\n|TM83|Infestation   | 70|100|\n|TM84|Poison Jab    | 80|100|\n|TM85|Dream Eater   |100|100|\n|TM89|U-Turn        | 70|100|\n|TM91|Flash Cannon  | 80|100|\n|TM93|Wild Charge   | 90|100|\n|TM94|Surf          | 90|100|\n|TM95|Snarl         | 55| 95|\n|TM97|Dark Pulse    | 80|100|\n|TM98|Waterfall     | 80|100|\n|TM99|Dazzling Gleam| 80|100|\n+━━━━+━━━━━━━━━━━━━━+━━━+━━━+`"
  await tbot.send_message(event.chat_id, TEXT)
