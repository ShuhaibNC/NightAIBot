from pyrogram import Client
import config
import logging
import asyncio
from aiohttp import web
from route import routes
import os
import asyncio

logging.basicConfig(level=logging.INFO)

plugins = dict(root='plugins')


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
    
loop = asyncio.get_event_loop()
web_app = loop.run_until_complete(web_server())
web_runner = web.AppRunner(web_app)
loop.run_until_complete(web_runner.setup())
loop.create_task(web.TCPSite(web_runner, "0.0.0.0", 8080).start())


Client(
    'Msonedlbot',
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=plugins
).run()