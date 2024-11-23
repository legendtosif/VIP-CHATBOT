from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER, nexichat


START_BOT = [
    
    [
        InlineKeyboardButton(text="❍ 𝐘ᴏᴜʀ 𝐂ᴏᴍᴍᴀɴᴅ ❍", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(
            text="❍ 𝐀ᴅᴅ 𝐌ᴇ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ❍",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="❍ 𝐇ᴇʟᴘ ❍", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="❍ 𝐀ʙᴏᴜᴛ ❍", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(text="❍ 𝐘ᴏᴜʀ 𝐂ᴏᴍᴍᴀɴᴅ ❍", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(
            text="❍ 𝐂ʟᴏ𝐬ᴇ ❍",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="❍ 𝐁ᴀᴄᴋ ❍", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 ᴛᴏᴏʟs 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="❍ 𝐂ʟᴏ𝐬ᴇ ❍", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="❍ 𝐂ʟᴏ𝐬ᴇ ❍", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="❍ 𝐁ᴀᴄᴋ ❍", callback_data="SBACK"),
        InlineKeyboardButton(text="❍ 𝐂ʟᴏ𝐬ᴇ ❍", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="❍ 𝐁ᴀᴄᴋ ❍", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="❍ 𝐂ʟᴏ𝐬ᴇ ❍", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="❍ 𝐇ᴇʟᴘ ❍", callback_data="HELP"),
        InlineKeyboardButton(text="❍ 𝐂ʟᴏ𝐬ᴇ ❍", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(text="❍ 𝐘ᴏᴜʀ 𝐂ᴏᴍᴍᴀɴᴅ ❍", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="❍ 𝐂ʟᴏ𝐬ᴇ ❍", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🍾 ᴏᴡɴᴇʀ 🍾", user_id=OWNER),
    ],
    [
        InlineKeyboardButton(text="🐳 ᴜᴘᴅᴀᴛᴇs 🐳", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="❍ 𝐁ᴀᴄᴋ ❍", callback_data="BACK"),
    ],
]
