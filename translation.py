import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hᴇʏ {},{}</b>

<b><blockquote><i>⚡ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ⚡
🔥 ɪ ᴄᴀɴ ꜰᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ꜰʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ</i></blockquote>

🛑 ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ</b>"""


  HELP_TXT = """<b><u>🛠️ HELP</b></u>

<u>**📚 Available commands:**</u>

<b><blockquote>⏣ __/start - check I'm alive__ 
⏣ __/forward - forward messages__
⏣ __/unequify - delete duplicate messages in channels__
⏣ __/settings - configure your settings__
⏣ __/reset - reset your settings__</blockquote></b>
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
  
<b>► __Add A Bot Or Userbot__
► __Add Atleast One To Channel (Your Bot/Userbot Must Be Admin In There)
► __You Can Add Chats Or Bots By Using /settings__
► __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
► __Then use /forward to forward messages__</b>"""
  
  ABOUT_TXT = """<b><blockqoute>
╭───────────⍟
├◈ ᴍy ɴᴀᴍᴇ : <a href=https://t.me/forward_2xbot>Forward 2xBot</a>
├◈ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/Bots_Administrator>⚡ Bots Administrator</a> 
├◈ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ: <a href=https://t.me/Magic_botz>Magic 🪄 Botz</a>   
├◈ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org/>Pʏᴛʜᴏɴ 𝟹</a>
├◈ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com/>Mᴏɴɢᴏ DB</a>
├◈ Bot Vᴇʀꜱɪᴏɴ: V-2.8.1
╰───────────────⍟</blockquote></b>"""
  
  FEATURES_TXT = """<b><u>Bot ⚡ Features</u>
  
<blockquote><b>► __Forward message from public channel to your channel without admin permission. if the channel is private need admin permission__
► __Forward message from private channel to your channel by using userbot(user must be member in there)__
► __custom caption__
► __custom button__
► __support restricted chats__
► __skip duplicate messages__
► __filter type of messages__
► __skip messages based on extensions & keywords & size__</b></blockquote>
"""
  
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPING NUMBER ❫</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """<b><blockquote>╭────❰ <u>Forwarded Status</u> ❱────❍
┃
┣⊸<b>🕵 ғᴇᴄʜᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>✅ sᴜᴄᴄᴇғᴜʟʟʏ ғᴡᴅ :</b> <code>{}</code>
┣⊸<b>👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>🗑️ ᴅᴇʟᴇᴛᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>🪆 sᴋɪᴘᴘᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>📊 sᴛᴀᴛᴜs  :</b> <code>{}</code>
┣⊸<b>⏳ ᴘʀᴏɢʀᴇss  :</b> <code>{}</code> %
┣⊸<b>⏰ ᴇᴛᴀ :</b> <code>{}</code>
┃
╰────⌊ <b>{}</b> ⌉───❍</blockquote></b>"""

  TEXT1 = """<b><blockquote>
╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs ❱➠
║╭━━━━━━━━━━━━━━━➣
║┃
║┣⪼**🕵 ғᴇᴄʜᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**✅ sᴜᴄᴄᴇғᴜʟʟʏ ғᴡᴅ :** `{}`
║┃
║┣⪼**👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍsɢ :** `{}`
║┃
║┣⪼**🗑️ ᴅᴇʟᴇᴛᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**🪆 sᴋɪᴘᴘᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**📊 sᴛᴀᴛᴜs  :** `{}`
║┃
║┣⪼**⏳ ᴘʀᴏɢʀᴇss :** `{}`
║┃
║┣⪼**⏰ ᴇᴛᴀ :** `{}`
║┃
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ **{}** ❱➠</b></blockquote> """

  DUPLICATE_TEXT = """<b><blockquote>
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ ❱</b></blockquote>
"""
  DOUBLE_CHECK = """<b><blockquote><u>DOUBLE CHECKING ⚠️</b></u>
<code>Before forwarding the messages Click the Yes button only after checking the following</code></blockquote>

<blockquote><b>★ YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>★ FROM CHANNEL:</b> `{from_chat}`
<b>★ TO CHANNEL:</b> `{to_chat}`
<b>★ SKIP MESSAGES:</b> `{skip}`</blockquote>

<b><blockquote><i>° [{botname}](t.me/{botuname}) must be admin in **TARGET CHAT**</i> (`{to_chat}`)
<i>° If the **SOURCE CHAT** is private your userbot must be member or your bot must be admin in there also</b></blockquote></i>

<b><blockquote>If the above is checked then the yes button can be clicked</b></blockquote>"""
