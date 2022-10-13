from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Bot Status And More Bots", url="https://t.me/+hbc28odEPwU4MDk9")],
        [
            InlineKeyboardButton("How to Use", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("Bots Channel", url="https://t.me/MaximXBots")],
    ]

    START = """
Hey Bro {}

Welcome To I𝗓υɱi 和泉 {} 

If You Don't Trust This Bot 😒, 
❶ Stop Reading This Message 🚫
❷ Delete This Chat Bro 🗑️

🫵 Still Reading!? 
You Can Use Me To Generate Pyrogram New V2 And Telethon String Session. Use Below Buttons To Learn More !

🧑‍💻 By @MaximXRobot 
    """

    HELP = """
❏ 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬
┣ /about - About The Bot 🤖
┣ /help - This Message 🏖️
┣ /start - Start the Bot 😴
┣ /generate - Generate Session ☁️
┣ /cancel - Cancel The process 🚫
┗ /restart - Cancel The process 😁
"""

    ABOUT = """
**About This Bot** 

Telegram Bot To Generate Pyrogram And Telethon String Session By @MaximXRobot

❏ 𝐌𝐚𝐱𝐢𝐦 𝐗 𝐁𝐨𝐭𝐬
┣ ☁️ Source Code : [Click Here](https://t.me/+vBu5aXlocTkwNGM1)
┣ 🔥 Framework : [Pyrogram](https://docs.pyrogram.org)
┗ 🗣️ Language : [Python](https://www.python.org)

❏ 🧑‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ━┓
┗ @MaximXRobot
    """
