YouTube Content Theft Detection using AI

This project detects whether a video on YouTube is a copied or reused version of another video using frame comparison, perceptual hashing, CLIP embeddings, and optionally, OpenAI GPT-4 Vision.

✨ Features

🔄 Downloads and compares YouTube videos frame by frame

🎞️ Extracts keyframes at multiple timestamps (5s, 15s, 30s)

🔍 Calculates visual similarity using:

Average Hashing (imagehash)

CLIP Embeddings (transformers)

GPT-4 Vision (Optional)

🔹 Scores similarity between videos

⚠️ Flags potentially copied content

🔍 Searches YouTube via API for potential copies

🌐 Tech Stack

Python

yt-dlp

OpenCV / ffmpeg-python

PIL (Pillow)

imagehash

Transformers (CLIP)

OpenAI API (Optional for vision)

YouTube Data API

📂 Folder Structure

youtube-content-checker/
├── README.md
├── main_hash_compare.py       # pHash-based similarity comparison
├── main_clip_compare.py       # CLIP-based similarity comparison
├── utils/
│   ├── downloader.py
│   ├── frame_extractor.py
│   ├── image_utils.py
├── search_youtube.py          # Optional: search similar videos
├── requirements.txt

🚀 How to Run

1. Install dependencies

pip install -r requirements.txt

2. Set your video IDs

Edit your script to replace:

ORIGINAL_VIDEO = "dQw4w9WgXcQ"
COPY_VIDEO = "oHg5SJYRHA0"

3. Run the script

python main_hash_compare.py
# or
python main_clip_compare.py

🔍 Example Output

Visual Similarity (frame @ 5s): 93.75%
Visual Similarity (frame @ 15s): 91.34%
Average Similarity: 92.55%
⚠️ Potential copy detected!

🎯 Future Enhancements

Integrate audio fingerprinting

Auto-report using YouTube API

Add GUI using Streamlit

Extend support to TikTok / Instagram Reels


  
