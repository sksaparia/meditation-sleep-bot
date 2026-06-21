import requests
import os

PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY")

def download_videos(query, folder, count=25):
    os.makedirs(folder, exist_ok=True)
    url = f"https://pixabay.com/api/videos/?key={PIXABAY_API_KEY}&q={query}&per_page=50&video_type=film"
    response = requests.get(url).json()
    
    downloaded = 0
    for i, hit in enumerate(response.get("hits", [])):
        if downloaded >= count:
            break
        try:
            video_url = hit["videos"]["medium"]["url"]
            filename = f"{folder}/{query.replace('+', '_')}_{i}.mp4"
            if not os.path.exists(filename):
                r = requests.get(video_url, timeout=30)
                with open(filename, "wb") as f:
                    f.write(r.content)
                print(f"Downloaded: {filename}")
                downloaded += 1
        except Exception as e:
            print(f"Error: {e}")

def download_music(query, folder, count=25):
    os.makedirs(folder, exist_ok=True)
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&per_page=50&media_type=music"
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
            if not os.path.exists(filename):
                r = requests.get(music_url, timeout=30)
                with open(filename, "wb") as f:
                    f.write(r.content)
                print(f"Downloaded: {filename}")
                downloaded += 1
        except Exception as e:
            print(f"Error: {e}")

# 50 animations download karo
print("Downloading animations...")
download_videos("rain+night", "animations/videos", 15)
download_videos("ocean+waves+night", "animations/videos", 10)
download_videos("forest+night", "animations/videos", 10)
download_videos("stars+night+sky", "animations/videos", 10)
download_videos("candle+fire+night", "animations/videos", 5)

# 50 music download karo  
print("Downloading music...")
download_music("meditation+sleep", "animations/music", 15)
download_music("relaxing+ambient", "animations/music", 15)
download_music("calm+piano", "animations/music", 10)
download_music("nature+sounds", "animations/music", 10)

print("All done!")
