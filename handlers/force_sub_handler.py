# (c) @AbirHasan2005

import asyncio
from typing import (
    Union
)
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def get_invite_link(bot: Client, chat_id: Union[str, int]):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=chat_id)
        return invite_link
    except FloodWait as e:
        print(f"Sleep of {e.value}s caused by FloodWait ...")
        await asyncio.sleep(e.value)
        return await get_invite_link(bot, chat_id)


async def handle_force_sub(bot: Client, cmd: Message):
    if Config.UPDATES_CHANNEL and Config.UPDATES_CHANNEL.startswith("-100"):
        channel_chat_id = int(Config.UPDATES_CHANNEL)
    elif Config.UPDATES_CHANNEL and (not Config.UPDATES_CHANNEL.startswith("-100")):
        channel_chat_id = Config.UPDATES_CHANNEL
    else:
        return 200
    try:
        user = await bot.get_chat_member(chat_id=channel_chat_id, user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Jnanesh](https://t.me/alonekingjnanesh).",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await get_invite_link(bot, chat_id=channel_chat_id)
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**<b>Please Join Below all Channel to to get File 📤!\n\nಮೊದಲು ಕೆಲ್ಗಡೆ ಇರುವ ಚಾನಲ್ ಗೆ ಸೆರು ನಂತರ ಫೈಲ್ ದೊರೆಯುತದೆ</b>**\n\n",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔥 SUBSCRIBE MY YOUTUBE CHANNEL", url="https://youtube.com/@Jnentertainment.?si=-xZOdUGBD3yxLjgW")
                    ],
                    [
                        InlineKeyboardButton("Channel 1️⃣", url="https://t.me/+a7O4p16NVFwwYzBl")
                    ]
                    [
                        InlineKeyboardButton("Channel 2️⃣", url=invite_link.invite_link)
                    ]
                    [
                        InlineKeyboardButton("Channel 3️⃣", url="https://t.me/+1jkEblWjr9g0YmI1")
                    ]
                    [
                        InlineKeyboardButton("Channel 4️⃣", url="https://t.me/+nlo1GNVDGIczZWE9")
                    ]
                    [
                        InlineKeyboardButton("Channel 5️⃣", url="https://t.me/ROCKERS_ADULT")
                    ]
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshForceSub")
                    ]
                ]
            )
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Jnanesh](https://t.me/alonekingjnanesh).",
            disable_web_page_preview=True
        )
        return 200
    return 200
