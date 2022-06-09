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

def tournament(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "💥 GRAND SLAM CHAMPIONSHIP 💥\n\n💫 GYMS ARE AWAITING 💫\n\nRULES -: 7 GYMS OF 7 REGIONS ( KANTO, JOHTO, HOENN, SINNOH, UNAVO, KALOS, ALOLA).\n\n✅️ PRIZE POLL:-\n    1) 25K\n    2) 20k\n    3)15k\n\n✅️ TOURNAMENT STARTS FROM - 10 JUNE\n\n✅️ PARTICIPANTS ARE ALLOWED TO APPLY TILL 10 JUNE\n\n✅️DETAILS -: THERE WILL BE 7 GYMS AND 7 GYM LEADERS USING POKES OF THAT REGION ( POKES WHICH IS FROM THAT REGION )\n\n✅️ 4V4 MATCH ( GYM LEADER CHOICE IT MAY INCREASE TO 5 OR 6)\n\n✅️TO JOIN THIS TOUR JOIN - @killers69 AND PAY 550 PD TO @A_S_ROWDY\n\n✅️ IF U DEFEATED 5 GYM LEADERS OF ANY REGION U WILL BE QUALIFIED FOR NEXT ROUND\n\n✅️ MEGA MAY BE ALLOWED OR MAY NOT BE DEPENDS ON GYM LEADER\n\n✅️ DUPLICATES BANNED\n\n✅️ GYM LEADER ARE EVEN ALLOWED TO BAN LEGENDARY OR ITS MEGA FOR OR SOME 0L OR ITS MEGA FORM...\n\n✅️ WE WILL GIVE U GYM LEADER LIST WITH RESPECT TO THERE REGIONAL GYMS...\n\n✅️ U MAY USE @officerjennyprobot for gym details. \n\n✅️ WE WILL GIVE U GYM BADGES AFTER EACH GYM U SUCCESSFULLY MANAGE TO BEAT.\n\n✅️ IF U FAIL TO BEAT A GYM U WILL HAVE 3 TRIES LEFT FOR EACH WITH YOU BUT U CANNOT CHALLENGE SAME GYM TWICE A DAY.\n\n✅️ U MUST GET 5 GYM BADGES IN 14 DAYS TO QUALIFY FOR NEXT ROUND\n\n✅️ ROUND 2 WILL BE BETWEEN QUALIFIED PARTICIPANTS. THIS ROUND WILL BE OF 4 DAYS\n\n✅️ USE /gyms IN @officerjennyprobot TO GET INFO ABOUT GYMS AND SUB COMMANDS.\n\n✅️ IF U STILL HAVE DOUBTS CONTACT @A_S_ROWDY.  ",
    )
    
def gyms(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Here are the list of all gyms with sub commands\n\n1}KANTO - use /kantogym\n2}JHOTO - Use /jhotogym\n3}HOENN - Use /hoenngym\n4}SINNOH - Use /sinnohgym\n5}UNOVA - Use /unovagym\n6}KALOS - Use /kalosgym\n7}ALOLA - Use /alolagym",
    )

def prizepool(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "PRIZE POOL FOR ACTIVE TOURNAMENT\n\n    1} 25K💵\n    2} 20K💵\n    3}15K💵\n",
    )
    
__help__ = """
 • `/tournament`*:* About the Active Tournament
 • `/prizepool`*:* About the prize poll in Active tournament
 • `/gyms`*:* List of Gyms in active tour
 • `/kantogym`*:* Rules about Kanto gym and Gym Leader
 • `/jhotogym`*:* Rules about Jhoto gym and Gym leader
 • `/hoenngym`*:* Rules about Hoenn gym and Gym Leader
 • `/sinnohgym`*:* Rules about Sinnoh gym and Gym Leader
 • `/unovagym`*:* Rules about Unova gym and Gym Leader
 • `/kalosgym`*:* Rules about Kalos gym and Gym Leader
 • `/alolagym`*:* Rules about Alola gym and Gym Leader
"""

TOURNAMENT_HANDLER = DisableAbleCommandHandler("tournament", tournament, run_async=True)
GYMS_HANDLER = DisableAbleCommandHandler("gyms", gyms, run_async=True)
PRIZEPOOL_HANDLER = DisableAbleCommandHandler("prizepool", prizepool, run_async=True)

dispatcher.add_handler(TOURNAMENT_HANDLER)
dispatcher.add_handler(GYMS_HANDLER)
dispatcher.add_handler(PRIZEPOOL_HANDLER)

__mod_name__ = "Tour"
