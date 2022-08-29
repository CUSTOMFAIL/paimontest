import html

from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, CallbackQueryHandler
from telegram.utils.helpers import mention_html

from zerotwobot import DRAGONS, dispatcher
from zerotwobot.modules.disable import DisableAbleCommandHandler
from zerotwobot.modules.helper_funcs.chat_status import (
    bot_admin,
    can_pin,
    can_promote,
    connection_status,
    user_admin,
    ADMIN_CACHE,
)

from zerotwobot.modules.helper_funcs.extraction import (
    extract_user,
    extract_user_and_text,
)
from zerotwobot.modules.log_channel import loggable
from zerotwobot.modules.helper_funcs.alternate import send_message



@connection_status
@bot_admin
@can_promote
@user_admin
@loggable
def promote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    user_id = extract_user(message, args)
    promoter = chat.get_member(user.id)


    if message.from_user.id == 1087968824:
        
        message.reply_text(
            text="You are an anonymous admin.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Click to prove Admin.",
                            callback_data=f"admin_=promote={user_id}",
                        ),
                    ],
                ],
            ),
        )

        return

    elif (
        not (promoter.can_promote_members or promoter.status == "creator")
        and user.id not in DRAGONS
    ):
        message.reply_text("You don't have the necessary rights to do that!")
        return

    if not user_id:
        message.reply_text(
            "You don't seem to be referring to a user or the ID specified is incorrect..",
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "administrator" or user_member.status == "creator":
        message.reply_text("How am I meant to promote someone that's already an admin?")
        return

    if user_id == bot.id:
        message.reply_text("I can't promote myself! Get an admin to do it for me.")
        return

    # set same perms as bot - bot can't assign higher perms than itself!
    bot_member = chat.get_member(bot.id)

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            # can_promote_members=bot_member.can_promote_members,
            can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
            can_manage_chat=bot_member.can_manage_chat,
            can_manage_voice_chats=bot_member.can_manage_voice_chats
        )
    except BadRequest as err:
        if err.message == "User_not_mutual_contact":
            message.reply_text("I can't promote someone who isn't in the group.")
        else:
            message.reply_text("An error occured while promoting.")
        return

    bot.sendMessage(
        chat.id,
        f"Sucessfully promoted <b>{user_member.user.first_name or user_id}</b>!",
        parse_mode=ParseMode.HTML,
    )

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#PROMOTED\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
    )

    return log_message



@connection_status
@bot_admin
@can_promote
@user_admin
@loggable
def demote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user

    user_id = extract_user(message, args)

    if message.from_user.id == 1087968824:
    
        message.reply_text(
            text="You are an anonymous admin.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Click to prove Admin.",
                            callback_data=f"admin_=demote={user_id}",
                        ),
                    ],
                ],
            ),
        )

        return


    if not user_id:
        message.reply_text(
            "You don't seem to be referring to a user or the ID specified is incorrect..",
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "creator":
        message.reply_text("This person CREATED the chat, how would I demote them?")
        return

    if not user_member.status == "administrator":
        message.reply_text("Can't demote what wasn't promoted!")
        return

    if user_id == bot.id:
        message.reply_text("I can't demote myself! Get an admin to do it for me.")
        return

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_voice_chats=False,
        )

        bot.sendMessage(
            chat.id,
            f"Sucessfully demoted <b>{user_member.user.first_name or user_id}</b>!",
            parse_mode=ParseMode.HTML,
        )

        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#DEMOTED\n"
            f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
            f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
        )

        return log_message
    except BadRequest:
        message.reply_text(
            "Could not demote. I might not be admin, or the admin status was appointed by another"
            " user, so I can't act upon them!",
        )
        return



@user_admin
def refresh_admin(update, _):
    try:
        ADMIN_CACHE.pop(update.effective_chat.id)
    except KeyError:
        pass

    update.effective_message.reply_text("Admins cache refreshed!")



@connection_status
@bot_admin
@can_promote
@user_admin
def set_title(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args

    chat = update.effective_chat
    message = update.effective_message

    user_id, title = extract_user_and_text(message, args)

    if message.from_user.id == 1087968824:
    
        message.reply_text(
            text="You are an anonymous admin.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Click to prove Admin.",
                            callback_data=f"admin_=title={user_id}={title}",
                        ),
                    ],
                ],
            ),
        )

        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if not user_id:
        message.reply_text(
            "You don't seem to be referring to a user or the ID specified is incorrect..",
        )
        return

    if user_member.status == "creator":
        message.reply_text(
            "This person CREATED the chat, how can I set custom title for him?",
        )
        return

    if user_member.status != "administrator":
        message.reply_text(
            "Can't set title for non-admins!\nPromote them first to set custom title!",
        )
        return

    if user_id == bot.id:
        message.reply_text(
            "I can't set my own title myself! Get the one who made me admin to do it for me.",
        )
        return

    if not title:
        message.reply_text("Setting blank title doesn't do anything!")
        return

    if len(title) > 16:
        message.reply_text(
            "The title length is longer than 16 characters.\nTruncating it to 16 characters.",
        )

    try:
        bot.setChatAdministratorCustomTitle(chat.id, user_id, title)
    except BadRequest:
        message.reply_text("Either they aren't promoted by me or you set a title text that is impossible to set.")
        return

    bot.sendMessage(
        chat.id,
        f"Sucessfully set title for <code>{user_member.user.first_name or user_id}</code> "
        f"to <code>{html.escape(title[:16])}</code>!",
        parse_mode=ParseMode.HTML,
    )



@bot_admin
@can_pin
@user_admin
@loggable
def pin(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    is_group = chat.type != "private" and chat.type != "channel"
    prev_message = update.effective_message.reply_to_message

    is_silent = True
    if len(args) >= 1:
        is_silent = not (
            args[0].lower() == "notify"
            or args[0].lower() == "loud"
            or args[0].lower() == "violent"
        )

    if not prev_message:
        message.reply_text("Please reply to message which you want to pin.")
        return
    
    if message.from_user.id == 1087968824:

        message.reply_text(
            text="You are an anonymous admin.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Click to prove Admin.",
                            callback_data=f"admin_=pin={prev_message.message_id}={is_silent}",
                        ),
                    ],
                ],
            ),
        )

        return

    if prev_message and is_group:
        try:
            bot.pinChatMessage(
                chat.id, prev_message.message_id, disable_notification=is_silent,
            )
        except BadRequest as excp:
            if excp.message == "Chat_not_modified":
                pass
            else:
                raise
        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#PINNED\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}"
        )

        return log_message



@bot_admin
@can_pin
@user_admin
@loggable
def unpin(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    if message.from_user.id == 1087968824:

        message.reply_text(
            text="You are an anonymous admin.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Click to prove Admin.",
                            callback_data=f"admin_=unpin",
                        ),
                    ],
                ],
            ),
        )

        return


    try:
        bot.unpinChatMessage(chat.id)
    except BadRequest as excp:
        if excp.message == "Chat_not_modified":
            pass
        elif excp.message == "Message to unpin not found":
            message.reply_text("No pinned message found")
            return
        else:
            raise

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNPINNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}"
    )

    return log_message

@bot_admin
@can_pin
@user_admin
@loggable
def unpinall(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    admin_member = chat.get_member(user.id)
    print(user)

    if message.from_user.id == 1087968824:

        message.reply_text(
            text="You are an anonymous admin.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Click to prove Admin.",
                            callback_data=f"admin_=unpinall",
                        ),
                    ],
                ],
            ),
        )

        return
    elif (
            not admin_member.status == "creator"
            and user.id not in DRAGONS
        ):
            message.reply_text("Only chat OWNER can unpin all messages.")
            return


    try:
        bot.unpin_all_chat_messages(chat.id)
    except BadRequest as excp:
        if excp.message == "Chat_not_modified":
            pass
        else:
            raise

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNPINNED_ALL\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}"
    )

    return log_message

@bot_admin
@user_admin
@connection_status
def invite(update: Update, context: CallbackContext):
    bot = context.bot
    chat = update.effective_chat

    if chat.username:
        update.effective_message.reply_text(f"https://t.me/{chat.username}")
    elif chat.type in [chat.SUPERGROUP, chat.CHANNEL]:
        bot_member = chat.get_member(bot.id)
        if bot_member.can_invite_users:
            invitelink = bot.exportChatInviteLink(chat.id)
            update.effective_message.reply_text(invitelink)
        else:
            update.effective_message.reply_text(
                "I don't have access to the invite link, try changing my permissions!",
            )
    else:
        update.effective_message.reply_text(
            "I can only give you invite links for supergroups and channels, sorry!",
        )



@connection_status
def adminlist(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat] -> unused variable
    user = update.effective_user  # type: Optional[User]
    args = context.args # -> unused variable
    bot = context.bot

    if update.effective_message.chat.type == "private":
        send_message(update.effective_message, "This command only works in Groups.")
        return

    chat = update.effective_chat
    chat_id = update.effective_chat.id
    chat_name = update.effective_message.chat.title # -> unused variable

    try:
        msg = update.effective_message.reply_text(
            "Fetching group admins...", parse_mode=ParseMode.HTML,
        )
    except BadRequest:
        msg = update.effective_message.reply_text(
            "Fetching group admins...", quote=False, parse_mode=ParseMode.HTML,
        )

    administrators = bot.getChatAdministrators(chat_id)
    text = "Admins in <b>{}</b>:".format(html.escape(update.effective_chat.title))

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        if user.first_name == "":
            name = "☠ Deleted Account"
        else:
            name = "{}".format(
                mention_html(
                    user.id, html.escape(user.first_name + " " + (user.last_name or "")),
                ),
            )

        if user.is_bot:
            administrators.remove(admin)
            continue

        # if user.username:
        #    name = escape_markdown("@" + user.username)
        if status == "creator":
            text += "\n 👑 Creator:"
            text += "\n<code> • </code>{}\n".format(name)

            if custom_title:
                text += f"<code> ┗━ {html.escape(custom_title)}</code>\n"

    text += "\n🔱 Admins:"

    custom_admin_list = {}
    normal_admin_list = []

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        if user.first_name == "":
            name = "☠ Deleted Account"
        else:
            name = "{}".format(
                mention_html(
                    user.id, html.escape(user.first_name + " " + (user.last_name or "")),
                ),
            )
        # if user.username:
        #    name = escape_markdown("@" + user.username)
        if status == "administrator":
            if custom_title:
                try:
                    custom_admin_list[custom_title].append(name)
                except KeyError:
                    custom_admin_list.update({custom_title: [name]})
            else:
                normal_admin_list.append(name)

    for admin in normal_admin_list:
        text += "\n<code> • </code>{}".format(admin)

    for admin_group in custom_admin_list.copy():
        if len(custom_admin_list[admin_group]) == 1:
            text += "\n<code> • </code>{} | <code>{}</code>".format(
                custom_admin_list[admin_group][0], html.escape(admin_group),
            )
            custom_admin_list.pop(admin_group)

    text += "\n"
    for admin_group, value in custom_admin_list.items():
        text += "\n🚨 <code>{}</code>".format(admin_group)
        for admin in value:
            text += "\n<code> • </code>{}".format(admin)
        text += "\n"

    try:
        msg.edit_text(text, parse_mode=ParseMode.HTML)
    except BadRequest:  # if original message is deleted
        return

@loggable
def admin_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    bot = context.bot
    message = update.effective_message
    chat = update.effective_chat
    admin_user = query.from_user

    splitter = query.data.replace("admin_", "").split("=")
    print(splitter)

    if splitter[1] == "promote":

        promoter = chat.get_member(admin_user.id)

        if (
            not (promoter.can_promote_members or promoter.status == "creator")
            and admin_user.id not in DRAGONS
        ):
            query.answer("You don't have the necessary rights to do that!", show_alert=True)
            return

        try:
            user_id = int(splitter[2])
        except ValueError:
            user_id = splitter[2]
            message.edit_text("You don't seem to be referring to a user or the ID specified is incorrect...")
            return

        
        try:
            user_member = chat.get_member(user_id)
        except:
            return

        if user_member.status == "administrator" or user_member.status == "creator":
            message.edit_text("How am I meant to promote someone that's already an admin?")
            return

        bot_member = chat.get_member(bot.id)

        try:
            bot.promoteChatMember(
                chat.id,
                user_id,
                can_change_info=bot_member.can_change_info,
                can_post_messages=bot_member.can_post_messages,
                can_edit_messages=bot_member.can_edit_messages,
                can_delete_messages=bot_member.can_delete_messages,
                can_invite_users=bot_member.can_invite_users,
                # can_promote_members=bot_member.can_promote_members,
                can_restrict_members=bot_member.can_restrict_members,
                can_pin_messages=bot_member.can_pin_messages,
                can_manage_chat=bot_member.can_manage_chat,
                can_manage_voice_chats=bot_member.can_manage_voice_chats
            )
        except BadRequest as err:
            if err.message == "User_not_mutual_contact":
                message.edit_text("I can't promote someone who isn't in the group")
            else:
                message.edit_text("An error occured while promoting.")
            return

        message.edit_text(
            f"Sucessfully promoted <b>{user_member.user.first_name or user_id}</b>!",
            parse_mode=ParseMode.HTML,
        )
        query.answer("Done")

        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#PROMOTED\n"
            f"<b>Admin:</b> {mention_html(admin_user.id, admin_user.first_name)}\n"
            f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
        )

        return log_message

    elif splitter[1] == "demote":

        demoter = chat.get_member(admin_user.id)

        if (
            not (demoter.can_promote_members or demoter.status == "creator")
            and admin_user.id not in DRAGONS
        ):
            query.answer("You don't have the necessary rights to do that!", show_alert=True)
            return

        try:
            user_id = int(splitter[2])
        except:
            user_id = splitter[2]
            message.edit_text("You dont't seem to be referring to a user or the ID specified is incorrect..")
            return

        
        
        try:
            user_member = chat.get_member(user_id)
        except:
            return

        if user_member.status == "creator":
            message.edit_text("This person CREATED the chat, how would I demote them?")
            return

        if not user_member.status == "administrator":
            message.edit_text("Can't demote what wasn't promoted!")
            return

        if user_id == bot.id:
            message.edit_text("I can't demote myself!, Get an admin to do it for me.")
            return

        try:
            bot.promoteChatMember(
                chat.id,
                user_id,
                can_change_info=False,
                can_post_messages=False,
                can_edit_messages=False,
                can_delete_messages=False,
                can_invite_users=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_voice_chats=False,
            )

            message.edit_text(
                f"Sucessfully demoted <b>{user_member.user.first_name or user_id}</b>!",
                parse_mode=ParseMode.HTML,
            )
            query.answer("Done")

            log_message = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#DEMOTED\n"
                f"<b>Admin:</b> {mention_html(admin_user.id, admin_user.first_name)}\n"
                f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
            )

            return log_message
        except BadRequest:
            message.edit_text(
                "Could not demote. I might not be admin, or the admin status was appointed by another"
                " user, so I can't act upon them!",
            )
            return
            
    elif splitter[1] == "title":
        title = splitter[3]

        admin_member = chat.get_member(admin_user.id)

        if (
            not (admin_member.can_promote_members or admin_member.status == "creator")
            and admin_user.id not in DRAGONS
        ):
            query.answer("You don't have the necessary rights to do that!")
            return

        try:
            user_id = int(splitter[2])
        except:
            message.edit_text(
                    "You don't seem to be referring to a user or the ID specified is incorrect..",
            )
            return
            

        try:
            user_member = chat.get_member(user_id)
        except:
            return           

        if user_member.status == "creator":
            message.edit_text(
                "This person CREATED the chat, how can I set custom title for him?",
            )
            return

        if user_member.status != "administrator":
            message.edit_text(
                "Can't set title for non-admins!\nPromote them first to set custom title!",
            )
            return

        if user_id == bot.id:
            message.edit_text(
                "I can't set my own title myself! Get the one who made me admin to do it for me.",
            )
            return

        if not title:
            message.edit_text("Setting blank title doesn't do anything!")
            return

        if len(title) > 16:
            message.edit_text(
                "The title length is longer than 16 characters.\nTruncating it to 16 characters.",
            )

        try:
            bot.setChatAdministratorCustomTitle(chat.id, user_id, title)
        except BadRequest:
            message.edit_text("Either they aren't promoted by me or you set a title text that is impossible to set.")
            return

        message.edit_text(
            text=f"Sucessfully set title for <code>{user_member.user.first_name or user_id}</code> "
            f"to <code>{html.escape(title[:16])}</code>!",
            parse_mode=ParseMode.HTML,
        )
            
    elif splitter[1] == "pin":

        admin_member = chat.get_member(admin_user.id)

        if (
            not (admin_member.can_pin_messages or admin_member.status == "creator")
            and admin_user.id not in DRAGONS
        ):
            query.answer("You don't have the necessary rights to do that!", show_alert=True)
            return


        try:
            message_id = int(splitter[2])
        except:
            return

        is_silent = bool(splitter[3])
        is_group = chat.type != "private" and chat.type != "channel"

        if is_group:
            try:
                bot.pinChatMessage(
                    chat.id, message_id, disable_notification=is_silent,
                )
            except BadRequest as excp:
                if excp.message == "Chat_not_modified":
                    pass
                else:
                    raise
            
            message.edit_text("Done Pinned.")

            log_message = (
                f"<b>{html.escape(chat.title)}</b>\n"
                f"#PINNED\n"
                f"<b>Admin:</b> {mention_html(admin_user.id, html.escape(admin_user.first_name))}"
            )

            return log_message

    elif splitter[1] == "unpin":

        admin_member = chat.get_member(admin_user.id)

        if (
            not (admin_member.can_pin_messages or admin_member.status == "creator")
            and admin_user.id not in DRAGONS
        ):
            query.answer("You don't have the necessary rights to do that!", show_alert=True)
            return

        try:
            bot.unpinChatMessage(chat.id)
        except BadRequest as excp:
            if excp.message == "Chat_not_modified":
                pass
            elif excp.message == "Message to unpin not found":
                message.edit_text("No pinned message found")
                return
            else:
                raise
        

        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#UNPINNED\n"
            f"<b>Admin:</b> {mention_html(admin_user.id, html.escape(admin_user.first_name))}"
        )

        return log_message

    elif splitter[1] == "unpinall":
        admin_member = chat.get_member(admin_user.id)

        if (
            not admin_member.status == "creator"
            and admin_user.id not in DRAGONS
        ):
            query.answer("Only chat OWNER can unpin all messages.")
            return

        try:
            bot.unpin_all_chat_messages(chat.id)
        except BadRequest as excp:
            if excp.message == "Chat_not_modified":
                pass
            else:
                raise
        
        message.edit_text("Done UnPinned All messages.")
        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#UNPINNED_ALL\n"
            f"<b>Admin:</b> {mention_html(admin_user.id, html.escape(admin_user.first_name))}"
        )

        return log_message


__help__ = """
 • `/admins`*:* list of admins in the chat

*Admins only:*
 • `/pin`*:* silently pins the message replied to - add `'loud'` or `'notify'` to give notifs to users
 • `/unpin`*:* unpins the currently pinned message
 • `/unpinall`*:* unpins all the pinned message (only OWNER can do.)
 • `/invitelink`*:* gets invitelink
 • `/promote`*:* promotes the user replied to
 • `/demote`*:* demotes the user replied to
 • `/title <title here>`*:* sets a custom title for an admin that the bot promoted
 • `/admincache`*:* force refresh the admins list
"""

ADMINLIST_HANDLER = DisableAbleCommandHandler("admins", adminlist, run_async=True)

PIN_HANDLER = CommandHandler("pin", pin, filters=Filters.chat_type.groups, run_async=True)
UNPIN_HANDLER = CommandHandler("unpin", unpin, filters=Filters.chat_type.groups, run_async=True)
UNPINALL_HANDLER = CommandHandler("unpinall", unpinall, filters=Filters.chat_type.groups, run_async=True)

INVITE_HANDLER = DisableAbleCommandHandler("invitelink", invite, run_async=True)

PROMOTE_HANDLER = DisableAbleCommandHandler(("jenny promote", [""]), promote, run_async=True)
DEMOTE_HANDLER = DisableAbleCommandHandler("demote", demote, run_async=True)

SET_TITLE_HANDLER = CommandHandler("title", set_title, run_async=True)
ADMIN_REFRESH_HANDLER = CommandHandler(
    "admincache", refresh_admin, filters=Filters.chat_type.groups, run_async=True
)
ADMIN_CALLBACK_HANDLER = CallbackQueryHandler(admin_callback, run_async=True, pattern=r"admin_")

dispatcher.add_handler(ADMINLIST_HANDLER)
dispatcher.add_handler(PIN_HANDLER)
dispatcher.add_handler(UNPIN_HANDLER)
dispatcher.add_handler(UNPINALL_HANDLER)
dispatcher.add_handler(INVITE_HANDLER)
dispatcher.add_handler(PROMOTE_HANDLER)
dispatcher.add_handler(DEMOTE_HANDLER)
dispatcher.add_handler(SET_TITLE_HANDLER)
dispatcher.add_handler(ADMIN_REFRESH_HANDLER)
dispatcher.add_handler(ADMIN_CALLBACK_HANDLER)

__mod_name__ = "Admin"
__command_list__ = [
    "adminlist",
    "admins",
    "invitelink",
    "promote",
    "demote",
    "admincache",
]
__handlers__ = [
    ADMINLIST_HANDLER,
    PIN_HANDLER,
    UNPIN_HANDLER,
    INVITE_HANDLER,
    PROMOTE_HANDLER,
    DEMOTE_HANDLER,
    SET_TITLE_HANDLER,
    ADMIN_REFRESH_HANDLER,
]
