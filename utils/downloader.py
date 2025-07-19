# downloader.py
import os

def download_video(video_id, output_name):
    os.system(f"yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' https://youtu.be/{video_id} -o {output_name}.mp4 -q")
    return f"{output_name}.mp4"
