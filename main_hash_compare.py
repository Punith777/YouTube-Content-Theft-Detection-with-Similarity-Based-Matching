# main_hash_compare.py
from utils.downloader import download_video
from utils.frame_extractor import extract_frame
from utils.image_utils import calculate_phash_similarity
import os

ORIGINAL_VIDEO = "dQw4w9WgXcQ"
COPY_VIDEO = "oHg5SJYRHA0"

original_path = download_video(ORIGINAL_VIDEO, "original")
copy_path = download_video(COPY_VIDEO, "copy")

timestamps = [5, 15, 30]
total = 0

for t in timestamps:
    f1 = extract_frame(original_path, t)
    f2 = extract_frame(copy_path, t)
    similarity = calculate_phash_similarity(f1, f2)
    print(f"Similarity at {t}s: {similarity:.2f}%")
    total += similarity
    os.remove(f1)
    os.remove(f2)

avg = total / len(timestamps)
print(f"Average Similarity: {avg:.2f}%")
if avg > 70:
    print("⚠️ Potential copy detected!")
