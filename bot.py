import env
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="String-Bot"),
)


if __name__ == "__main__":
    print("Starting The Bot")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH Is Not Valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN Is Not Valid.")
    uname = app.get_me().username
    print(f"@{uname} Is Now Running!")
    idle()
    app.stop()
    print("Bot Stopped. Take Care Yourself!")
