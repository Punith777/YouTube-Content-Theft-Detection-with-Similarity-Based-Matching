# search_youtube.py
import requests

def search_youtube(query, api_key, max_results=5):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults={max_results}&key={api_key}"
    return requests.get(url).json()
