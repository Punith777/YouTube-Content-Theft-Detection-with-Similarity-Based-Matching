# image_utils.py
import imagehash
from PIL import Image
import torch
from torchvision import transforms
from transformers import CLIPProcessor, CLIPModel
import numpy as np

def calculate_phash_similarity(img1_path, img2_path):
    h1 = imagehash.average_hash(Image.open(img1_path))
    h2 = imagehash.average_hash(Image.open(img2_path))
    return 100 - (h1 - h2) * 100 / 64

device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_clip_embedding(img_path):
    image = Image.open(img_path).convert("RGB")
    inputs = clip_processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        return clip_model.get_image_features(**inputs).cpu().numpy()

def cosine_sim(emb1, emb2):
    dot = np.dot(emb1, emb2.T)
    return dot.flatten()[0] / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
