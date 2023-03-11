#pylint:disable=E0401
from pyrogram import *
import config

plugins = dict(root='plugins')

Client(
    'NightAIBot',
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=plugins
).run()