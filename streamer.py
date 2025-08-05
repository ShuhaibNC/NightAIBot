import os
import asyncio

async def start_streamer():
    os.environ['IN'] = "https://segment.yuppcdn.net/110322/channel24/playlist.m3u8"
    os.environ['OUT'] = "rtmps://dc5-1.rtmp.t.me/s/1666122378:RxvW87rHe6xQPT4FbWTvYQ"
    os.environ['JPG'] = "https://upload.wikimedia.org/wikipedia/commons/c/c5/Spectrogram-19thC.png"

    process = await asyncio.create_subprocess_exec(
        "python3", "streamer.py",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    async def log_output(stream, name):
        while True:
            line = await stream.readline()
            if not line:
                break
            print(f"[{name}] {line.decode().rstrip()}")

    asyncio.create_task(log_output(process.stdout, "STREAM OUT"))
    asyncio.create_task(log_output(process.stderr, "STREAM ERR"))

# Inside your bot runner or startup logic
# await start_streamer() if already inside an async function