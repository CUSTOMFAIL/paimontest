import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/gen1"))
async def awake(event):
  TEXT = f"`🌟Bulbasaur |🌟Ivysaur\n🌟Venusaur  |🌟Charmander\n🌟Charmeleon|🌟Charizard\n🌟Squirtle  |🌟Wartortle\n🌟Blastoise |🌟Caterpie\n🌟Metapod   |🌟Butterfree\n🌟Weedle    |🌟Kakuna\n🌟Beedrill  |🌟Pidgey\n🌟Pidgeotto |🌟Pidgeot\n🌟Rattata   |🌟Raticate\n🌟Spearow   |🌟Fearow\n🌟Ekans     |🌟Arbok\n🌟Pikachu   |🌟Raichu\n🌟Sandshrew |🌟Sandslash\n🌟Nidoran♀  |🌟Nidorina\n🌟Nidoqueen |🌟Nidoran♂\n🌟Nidorino  |🌟Nidoking\n🌟Clefairy  |🌟Clefable\n🌟Vulpix    |🌟Ninetales \n🌟Jigglypuff|🌟Wigglytuff\n🌟Zubat     |🌟Golbat\n🌟Oddish    |🌟Gloom\n🌟Vileplume |🌟Paras\n🌟Parasect  |🌟Venonat\n🌟Venomoth  |🌟Diglett\n🌟Dugtrio   |🌟Meowth\n🌟Persian   |🌟Psyduck\n🌟Golduck   |🌟Mankey\n🌟Primeape  |🌟Growlithe\n🌟Arcanine  |🌟Poliwag\n🌟Poliwhirl |🌟Poliwrath\n🌟Abra      |🌟Kadabra\n🌟Alakazam  |🌟Machop\n🌟Machamp   |🌟Machoke\n🌟Farfetch'd|🌟Bellsprout\n🌟Weepinbell|🌟Victreebel\n🌟Tentacool |🌟Tentacruel\n🌟Geodude   |🌟Graveler\n🌟Golem     |🌟Ponyta\n🌟Rapidash  |🌟Slowpoke\n🌟Slowbro   |🌟Magnemite\n🌟Magneton  |🌟Doduo\n🌟Dodrio    |🌟Seel\n🌟Dewgong   |🌟Grimer\n🌟Muk       |🌟Shellder\n🌟Cloyster  |🌟Gastly\n🌟Haunter   |🌟Gengar\n🌟Onix      |🌟Drowzee\n🌟Hypno     |🌟Krabby\n🌟Kingler   |🌟Voltorb\n🌟Electrode |🌟Exeggcute\n🌟Exeggutor |🌟Cubone\n🌟Marowak   |🌟Hitmonlee\n🌟Hitmonchan|🌟Lickitung\n🌟Koffing   |🌟Weezing\n🌟Rhyhorn   |🌟Rhydon\n🌟Chansey   |🌟Tangela\n🌟Kangaskhan|🌟Horsea\n🌟Seadra    |🌟Goldeen\n🌟Seaking   |🌟Staryu\n🌟Starmie   |🌟Mr.Mime\n🌟Scyther   |🌟Jynx\n🌟Electabuzz|🌟Magmar\n🌟Pinsir    |🌟Tauros\n🌟Magikarp  |🌟Gyarados\n🌟Lapras    |🌟Ditto\n🌟Eevee     |🌟Vaporeon\n🌟Jolteon   |🌟Flareon\n🌟Porygon   |🌟Omanyte\n🌟Omastar   |🌟Kabuto\n🌟Kabutops  |🌟Aerodactyl\n🌟Snorlax   |🌟Articuno\n🌟Zapdos    |🌟Moltres\n🌟Dratini   |🌟Dragonair\n🌟Dragonite |🌟Mewtwo\n🌟Mew`"
  await tbot.send_message(event.chat_id, TEXT)
