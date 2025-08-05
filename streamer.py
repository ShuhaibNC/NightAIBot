import os
import subprocess

# Set your input/output here
os.environ['IN'] = "https://cloud.revma.ihrhls.com/zc1961?rj-org=n03b-e2&rj-ttl=5&rj-tok=AAABmHqPQbgA4AzSaHsd58L7kQ"
os.environ['OUT'] = "rtmps://dc5-1.rtmp.t.me/s/1666122378:RxvW87rHe6xQPT4FbWTvYQ"

def stream_audio_with_black_background(input_audio_url, output_rtmp):
    command = [
        "ffmpeg",
        "-re",
        "-f", "lavfi",
        "-i", "color=c=black:s=1280x720:r=25",
        "-i", input_audio_url,
        "-shortest",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-vf", "drawtext=text='Background Play':fontcolor=white:fontsize=70:x=(w-text_w)/2:y=(h-text_h)/2",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-tune", "zerolatency",
        "-c:a", "aac",
        "-ar", "44100",
        "-ac", "2",
        "-b:a", "128k",
        "-f", "flv",
        output_rtmp
    ]

    try:
        print("🔴 Starting FFmpeg stream with background text...")
        print("Audio In :", input_audio_url)
        print("Out RTMP :", output_rtmp)
        subprocess.run(command)
    except KeyboardInterrupt:
        print("🛑 Stopped by user.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    input_audio_url = os.getenv("IN")
    output_rtmp = os.getenv("OUT")

    if not input_audio_url or not output_rtmp:
        print("❌ Environment variables IN or OUT not set.")
        exit(1)

    stream_audio_with_black_background(input_audio_url, output_rtmp)
