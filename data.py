from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🖤 sᴜᴩᴩᴏʀᴛ 🖤", url="https://t.me/LegendSupport"),
         InlineKeyboardButton("🌹 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🌹", url="https://t.me/XH4REEF_L4DK4_43"),
        ],
    ]

    START = """
Hᴇʏ {},
Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
Sᴏᴜʀᴄᴇ : [ɢɪᴛʜᴜʙ](https://github.com/TeamLegend77/StringLegendBot)
Mᴀᴅᴇ ᴡɪᴛʜ 🥀 ʙʏ : [𝗥𝗢𝗠𝗘𝗢](https://t.me/XH4REEF_L4DK4_43) !
    """
