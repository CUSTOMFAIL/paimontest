from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from Zerotwobot import pbot


@pbot.on_message(filters.command(["cum", "editor"]))
async def photo(client: pbot, message: Message):
   await client.send_message(
      chat_id=message.chat.id,
      text="Select your required mode from below!ㅤㅤ",
      reply_markup=InlineKeyboardMarkup(
           [
                    [
                        InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                        InlineKeyboardButton(text="GEN2", callback_data="gen2"),
                        InlineKeyboardButton(text="GEN3", callback_data="gen3"),
                    ],
                    [
                        InlineKeyboardButton(text="GEN4", callback_data="gen4"),
                    ],
                ]
            ),
            reply_to_message_id=message.reply_to_message_id,
        )
    
@pbot.on_callback_query()
async def cb_handler(client: pbot, query: CallbackQuery):
        if query.data == "gen1":
            await query.message.edit_text(
                "**OKM GEN1**ㅤㅤㅤㅤ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            )
                        ],
                    ]
                ),
            )
        elif query.data == "gen2":
            await query.message.edit(
                "**OWO GEN2**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            )
                        ],
                    ]
                ),
            )
        elif query.data == "gen3":
            await query.message.edit(
                "**OWO GEN3**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN4", callback_data="gen4"
                            )
                        ],
                    ]
                ),
            ) 
        elif query.data == "gen4":
            await query.message.edit(
                "**OWO GEN4**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="GEN1", callback_data="gen1"),
                            InlineKeyboardButton(
                                text="GEN2", callback_data="gen2"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="GEN3", callback_data="gen3"
                            )
                        ],
                    ]
                ),
            )


__mod_name__ = "Img Editor​ 📸"

__help__ = """
❍ `/edit` : To edit the image.
❍ `/editor` : To edit the imiage.
Note: Remove BG doesn't work, dev will fix it later.
"""
