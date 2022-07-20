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

def natures(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Nature are a mechanic that influences how a Pokémon stats grow.\nNature effect is limited to only 10%.\nHere are the list of commands\n\n/hardy - About hardy natured pokemon.\n/lonely - About lonely natured pokemon.\n/brave - About brave natured pokemon.\n/adamant - About adamant natured pokemon.\n/naughty - About naughty natured pokemon.\n/bold - About bold natured pokemon.\n/docile - About docile natured pokemon.\n/relaxed - About relaxed natured pokemon.\n/impish - About impish natured pokemon.\n/lax - About lax natured pokemon.\n/modest - About modest natured pokemon.\n/mild - About mild natured pokemon.\n/serious - About serious natured pokemon.\n/quiet - About quiet natured pokemon.\n/rash - About rash natured pokemon.\n/calm - About calm natured pokemon.\n/gentle - About gentle natured pokemon.\n/sassy - About sassy natured pokemon.\n/bashful - About bashful natured pokemon.\n/careful - About careful natured pokemon.\n/timid - About timid natured pokemon.\n/hasty - About hasty natured pokemon.\n/jolly - About jolly natured pokemon.\n/naive - About naive natured pokemon.\n/quirky - About quirky natured pokemon",
    )
    
NATURES_HANDLER = DisableAbleCommandHandler("natures", natures, run_async=True)
    
dispatcher.add_handler(NATURES_HANDLER)
