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

# Web server for route integration

async def start_streamer():
    # Use env vars: IN and OUT (set from outside or load them here)
    os.environ['IN'] = "https://segment.yuppcdn.net/110322/channel24/playlist.m3u8"
    os.environ['OUT'] = "rtmps://dc5-1.rtmp.t.me/s/1666122378:RxvW87rHe6xQPT4FbWTvYQ"

    process = await asyncio.create_subprocess_exec(
        "python3", "streamer.py",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # Optional: log stdout/stderr
    async def log_output(stream, name):
        while True:
            line = await stream.readline()
            if not line:
                break
            print(f"[{name}] {line.decode().rstrip()}")

    asyncio.create_task(log_output(process.stdout, "STDOUT"))
    asyncio.create_task(log_output(process.stderr, "STDERR"))

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
    
loop = asyncio.get_event_loop()
web_app = loop.run_until_complete(web_server())
web_runner = web.AppRunner(web_app)
loop.run_until_complete(web_runner.setup())
loop.create_task(web.TCPSite(web_runner, "0.0.0.0", 8080).start())
loop.create_task(start_streamer())


Client(
    'NightAIBot',
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=plugins
).run()