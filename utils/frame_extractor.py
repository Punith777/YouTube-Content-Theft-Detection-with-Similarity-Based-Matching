# frame_extractor.py
import ffmpeg
import os

def extract_frame(video_path, time_sec=5):
    frame_path = f"frame_{os.path.basename(video_path)}_{time_sec}.jpg"
    ffmpeg.input(video_path, ss=time_sec).output(frame_path, vframes=1).run(overwrite_output=True, quiet=True)
    return frame_path
