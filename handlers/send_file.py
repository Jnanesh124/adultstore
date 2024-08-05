# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64
from utils import check_verification, get_token

async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"**🔎Also Join Below My Channel:**\n"
            f"<b>𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐌𝐨𝐯𝐢𝐞𝐬  🕶\nhttps://t.me/+66Rsf3q0p3c2M2Nl\n\n𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐇𝐃 𝐌𝐨𝐯𝐢𝐞𝐬  🍿\nhttps://t.me/+1z2A8ZxGkEM1N2Q1\n\n𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠 𝐌𝐨𝐯𝐢𝐞𝐬 𝐇𝐃 📸\nhttps://t.me/+8K8gz7k6Ry05YzZl\n\nOnline Streaming group 💜\nhttps://t.me/+oQT1f1iF4fU4ZGVl\n\n18+ banned Movies 🔞\nhttps://t.me/+3xxIFZXTj9E1M2E1\n\n𝐑𝐨𝐜𝐤𝐞𝐫𝐬 𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐓𝐯 𝐒𝐞𝐫𝐢𝐚𝐥𝐬 📺\nhttps://t.me/Rockers_TV_Serials\n\nSex porn nudi adult video 🔞🔥\nhttps://t.me/+Ce98xoyvoLcwYThl\n\n𝐉𝐃 𝐈𝐏𝐋 𝐌𝐚𝐭𝐜𝐡 𝐑𝐞𝐩𝐨𝐫𝐭 ⁱᵖˡ ᵐᵃᵗᶜʰ📢\nhttps://t.me/+rNwi4b0VLU1iODU1</b>\n\n",
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await reply_forward(message, file_id)


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    if not await check_verification(client, message.from_user.id) and VERIFY == True:
        btn = [[
            InlineKeyboardButton("Verify", url=await get_token(client, message.from_user.id, f"https://telegram.me/{BOT_USERNAME}?start="))
        ],[
            InlineKeyboardButton("How To Open Link & Verify", url=VERIFY_TUTORIAL)
        ]]
        await message.reply_text(
            text="<b>You are not verified !\nKindly verify to continue !</b>",
            protect_content=True,
            reply_markup=InlineKeyboardMarkup(btn)
        )
        return
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    await asyncio.sleep(2)
