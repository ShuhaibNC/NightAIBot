import os
import subprocess

def stream_to_telegram(input_url, output_rtmp):
    command = [
        "ffmpeg",
        "-re",
        "-i", input_url,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-tune", "zerolatency",
        "-c:a", "aac",
        "-ar", "44100",
        "-ac", "1",
        "-b:a", "128k",
        "-f", "flv",
        output_rtmp
    ]

    try:
        print("🔴 Starting FFmpeg stream...")
        print("From:", input_url)
        print("To  :", output_rtmp)
        subprocess.run(command)
    except KeyboardInterrupt:
        print("🛑 Stopped by user.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    input_url = os.getenv("IN")
    output_rtmp = os.getenv("OUT")

    if not input_url or not output_rtmp:
        print("❌ Environment variables IN or OUT not set.")
        exit(1)

    stream_to_telegram(input_url, output_rtmp)