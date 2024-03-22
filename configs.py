# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** [Jnanesh](https://t.me/alonekingjnanesh)


📢 **Updates Channel:** [ಸಿನಿಮಾ ಹಾಲ್](https://t.me/alonekingjnanesh)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @alonekingjnanesh 

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://t.me/jnaneshtn) (love)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐌𝐨𝐯𝐢𝐞𝐬  🕶

t.me/+66Rsf3q0p3c2M2Nl

𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐇𝐃 𝐌𝐨𝐯𝐢𝐞𝐬  🍿

t.me/+1z2A8ZxGkEM1N2Q1

𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠 𝐌𝐨𝐯𝐢𝐞𝐬 𝐇𝐃 📸

t.me/+8K8gz7k6Ry05YzZl

Online Streaming group 💜

t.me/+oQT1f1iF4fU4ZGVl

18+ banned Movies 🔞

t.me/+3xxIFZXTj9E1M2E1

𝐑𝐨𝐜𝐤𝐞𝐫𝐬 𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐓𝐯 𝐒𝐞𝐫𝐢𝐚𝐥𝐬 📺

t.me/Rockers_TV_Serials

Sex porn nudi adult video 🔞🔥

t.me/+Ce98xoyvoLcwYThl

𝐉𝐃 𝐈𝐏𝐋 𝐌𝐚𝐭𝐜𝐡 𝐑𝐞𝐩𝐨𝐫𝐭 ⁱᵖˡ ᵐᵃᵗᶜʰ📢

t.me/+rNwi4b0VLU1iODU1

©️@ROCKERSBACKUP 
"""
