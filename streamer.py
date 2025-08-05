import os
import subprocess

# Set your input/output/image here
os.environ['IN'] = "https://stream-155.zeno.fm/dtr207bhb8zuv?zt=eyJhbGciOiJIUzI1NiJ9.eyJzdHJlYW0iOiJkdHIyMDdiaGI4enV2IiwiaG9zdCI6InN0cmVhbS0xNTUuemVuby5mbSIsInJ0dGwiOjUsImp0aSI6IjlDdm1YR2VDUlYtV3dadGt4dUtnakEiLCJpYXQiOjE3NTQ0MDA3ODAsImV4cCI6MTc1NDQwMDg0MH0.9q8TDnEXHZcWxiE0goPhDMIX1S59qSlcsyMRRZDGay8"
os.environ['OUT'] = "rtmps://dc5-1.rtmp.t.me/s/1666122378:RxvW87rHe6xQPT4FbWTvYQ"
os.environ['JPG'] = "https://upload.wikimedia.org/wikipedia/commons/c/c5/Spectrogram-19thC.png"

def stream_audio_with_image(input_audio_url, output_rtmp, image_url):
    command = [
        "ffmpeg",
        "-re",
        "-loop", "1",
        "-i", image_url,
        "-i", input_audio_url,
        "-shortest",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-ar", "44100",
        "-ac", "2",
        "-b:a", "128k",
        "-f", "flv",
        output_rtmp
    ]

    try:
        print("🔴 Starting FFmpeg stream...")
        print("Audio In :", input_audio_url)
        print("Image    :", image_url)
        print("Out RTMP :", output_rtmp)
        subprocess.run(command)
    except KeyboardInterrupt:
        print("🛑 Stopped by user.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    input_audio_url = os.getenv("IN")
    output_rtmp = os.getenv("OUT")
    image_url = os.getenv("JPG")

    if not input_audio_url or not output_rtmp:
        print("❌ Environment variables IN or OUT not set.")
        exit(1)

    stream_audio_with_image(input_audio_url, output_rtmp, image_url)
