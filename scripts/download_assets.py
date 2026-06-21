import requests
import os

PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY")

def download_videos(query, folder, count=3):
    os.makedirs(folder, exist_ok=True)
    url = f"https://pixabay.com/api/videos/?key={PIXABAY_API_KEY}&q={query}&per_page=20&video_type=film"
    response = requests.get(url).json()
    
    downloaded = 0
    for i, hit in enumerate(response.get("hits", [])):
        if downloaded >= count:
            break
        try:
            video_url = hit["videos"]["medium"]["url"]
            filename = f"{folder}/{query.replace('+', '_')}_{i}.mp4"
            r = requests.get(video_url, timeout=60)
            with open(filename, "wb") as f:
                f.write(r.content)
            print(f"Downloaded: {filename}")
            downloaded += 1
        except Exception as e:
            print(f"Error: {e}")

def download_music(query, folder, count=3):
    os.makedirs(folder, exist_ok=True)
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&per_page=20&media_type=music"
    response = requests.get(url).json()
    
    downloaded = 0
    for i, hit in enumerate(response.get("hits", [])):
        if downloaded >= count:
            break
        try:
            music_url = hit.get("audio", {}).get("url", "")
            if not music_url:
                continue
            filename = f"{folder}/music_{query.replace('+', '_')}_{i}.mp3"
            r = requests.get(music_url, timeout=60)
            with open(filename, "wb") as f:
                f.write(r.content)
            print(f"Downloaded: {filename}")
            downloaded += 1
        except Exception as e:
            print(f"Error: {e}")

# 8 animations
print("Downloading animations...")
download_videos("rain+night", "animations/videos", 3)
download_videos("ocean+waves+night", "animations/videos", 2)
download_videos("forest+night", "animations/videos", 2)
download_videos("stars+night+sky", "animations/videos", 1)

# 7 music
print("Downloading music...")
download_music("meditation+sleep", "animations/music", 3)
download_music("relaxing+ambient", "animations/music", 2)
download_music("calm+piano", "animations/music", 1)
download_music("nature+sounds", "animations/music", 1)

print("All done! 15 files downloaded!")
