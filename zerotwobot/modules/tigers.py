import html
import json
import os
from typing import Optional

from zerotwobot import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    SUPPORT_CHAT,
    DEMONS,
    TIGERS,
    WOLVES,
    MEMBERS,
    dispatcher,
)
from zerotwobot.modules.helper_funcs.chat_status import (
    dev_plus,
    sudo_plus,
    whitelist_plus,
)
from zerotwobot.modules.helper_funcs.extraction import extract_user
from zerotwobot.modules.log_channel import gloggable
from telegram import ParseMode, TelegramError, Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import mention_html

@whitelist_plus
def supportlist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML,
    )
    reply = "<b>LIST 𝚇 𝙼𝙾𝙳:</b>\n"
    for each_user in DEMONS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)
    
SUPPORTLIST_HANDLER = CommandHandler(["supportlist", "demons", "xmods"], supportlist, run_async=True)
    
dispatcher.add_handler(SUPPORTLIST_HANDLER)
