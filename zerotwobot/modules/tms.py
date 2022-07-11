import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/tms"))
async def awake(event):
  TEXT = f"`+━━+━━━━━━━━━+━━━+━━━+━+\n|TM|    NAME   |PWR|ACC|TYP|\n+━━+━━━━━━━━━+━━━+━━━+━+\n|02|Dragon claw| 80|100|🐉P|\n|03|Psyshock   | 80|100|🔮S|\n|09|Venoshock  | 65|100|☣️S|\n|10|Hiddenpower| 60|100|✴️S|\n|13|Ice Beam   | 90|100|❄️S|\n|14|Blizzard   |110| 70|❄️S|\n|15|Hyper Beam |150| 90|✴️S|\n|22|Solar Beam |120|100|🍃S|\n|23|Smack Down | 50|100|🧱P|\n|24|Thunderbolt| 90|100|⚡️S|\n|25|Thunder    |110| 70|⚡️P|\n|26|Earthquake |100|100|⛰P|\n|28|Leech Life | 80|100|🐞P|\n|29|Psychic    | 90|100|🔮S|\n|30|Shadow Ball| 80|100|👁‍🗨S|\n|31|Brick Break| 75|100|🥊P|\n|34|Sludge Wave| 95|100|☣️S|\n|35|Flamethrowr| 90|100|🔥S|\n|36|Sludge Bomb| 90|100|☣️S|\n|38|Fire Blast |110| 85|🔥S|\n|39|Rock Tomb  | 60| 95|🧱P|\n|40|Aerial Ace | 60|100|🌪P|\n|42|Facade     | 70|100|✴️P|\n|43|FlameCharge| 50|100|🔥P|\n|46|Thief      | 60|100|⚫️P|\n|47|Low Sweep  | 65|100|🥊P|\n|48|Round      | 60|100|✴️S|\n|49|EchoedVoice| 40|100|✴️S|\n|50|Ovearheat  |130| 90|🔥S|\n|51|Steel Wings| 70| 90|🛡P|\n|52|Focus Blast|120| 70|🥊S|\n|53|Energy Ball| 90|100|🍃S|\n|54|False swipe| 40|100|✴️P|\n|55|Scald      | 80|100|💧S|\n|57|Charge Beam| 50| 90|⚡️S|\n|58|Sky Drop   | 60|100|🌪P|\n|59|BrutalSwing| 60|100|⚫️P|\n|62|Acrobatics | 55|100|🌪P|\n|65|Shadow Claw| 70|100|👁‍🗨P|\n|66|Payback    | 50|100|⚫️P|\n|67|SmartStrike| 70|100|🛡P|\n|68|Giga Impact|150| 90|✴️P|\n|71|Stone Edge |100| 80|🧱P|\n|72|Volt Switch| 70|100|⚡️S|\n|76|Fly        | 90| 95|🌪P|\n|78|Bulldoze   | 60|100|⛰P|\n|79|FrostBreath| 60| 90|❄️S|\n|80|Rock Slide | 75| 90|🧱P|\n|81|X-Scissor  | 80|100|🐞P|\n|82|Dragon Tail| 60| 90|🐉P|\n|83|Infestation| 70|100|🐞S|\n|84|Poison Jab | 80|100|☣️P|\n|85|Dream Eater|100|100|🔮S|\n|89|U-Turn     | 70|100|🐞P|\n|91|Flash Canon| 80|100|🛡S|\n|93|Wild Charge| 90|100|⚡️P|\n|94|Surf       | 90|100|💧S|\n|95|Snarl      | 55| 95|⚫️S|\n|97|Dark Pulse | 80|100|⚫️S|\n|98|Waterfall  | 80|100|💧P|\n|99|DazlingGlem| 80|100|🧚S|\n+━━+━━━━━━━━━+━━+━━━+━━+`"
  await tbot.send_message(event.chat_id, TEXT)
