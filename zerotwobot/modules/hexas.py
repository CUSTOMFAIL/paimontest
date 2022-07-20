import html
import random
import time

import zerotwobot.modules.fun_strings as fun_strings
from zerotwobot import dispatcher
from zerotwobot.modules.disable import DisableAbleCommandHandler
from zerotwobot.modules.helper_funcs.chat_status import is_user_admin
from zerotwobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

    
def nexttour(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "COMING SOON",
    )

def prizepool(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Prize pool for dice tour\n\n1st- 15k + X MOD FOR A MONTH\n2nd- 10k\n3rd- 5k",
    )
    
__help__ = """
 • `/hexa`*:* About Hexa
 • `/types`*:* List all types and sub commands
 • `/type(typename)`*:* About that type
 • `/ptype`*:* Use and see
 • `/data(pokename)`*:* About that pokemon
 • `natures`*:* List of all Natures and sub commands
 • `/gen1`*:* List of Generation 1 Pokemon
 • `/gen2`*:* List of Generation 2 Pokemon
 • `/gen3`*:* List of Generation 3 Pokemon
 • `/gen4`*:* List of Generation 4 Pokemon
 • `/gen5`*:* List of Generation 5 Pokemon
 • `/gen6`*:* List of Generation 6 Pokemon
 • `/gen7`*:* List of Generation 7 Pokemon
 • `/tournament`*:* About the Active Tournament
 • `/nexttour`*:* About next tour
 `THERE ARE ALSO SOME SPECIAL COMMANDS`
 `■ /{POKEMONNAME} - To get best natures of that pokemon currently there are 150 pokemon added. For example /charmander`
 `■ /{TYPENAME} - To know about that type. For example - /fire`
 `■ /{NATURENAME - To know about that nature. For example - /lonely`
"""

NEXTTOUR_HANDLER = DisableAbleCommandHandler("nexttour", nexttour, run_async=True)
PRIZEPOOL_HANDLER = DisableAbleCommandHandler("prizepool", prizepool, run_async=True)

dispatcher.add_handler(NEXTTOUR_HANDLER)
dispatcher.add_handler(PRIZEPOOL_HANDLER)


__mod_name__ = "Hexa"
