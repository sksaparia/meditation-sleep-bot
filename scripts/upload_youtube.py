import os
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

VIDEOS = [
    "Deep Sleep Music 😴 | Rain Sounds | 1 Hour",
    "Relaxing Sleep Music 🌧️ | Stress Relief | 1 Hour",
    "Peaceful Sleep Music 🌙 | Calm Your Mind | 1 Hour",
    "Sleep Instantly 💤 | Rain & Music | 1 Hour",
    "Deep Relaxation Music ✨ | Fall Asleep Fast | 1 Hour",
    "Healing Sleep Music 💫 | Nature Sounds | 1 Hour",
    "Calm Mind Music 🌿 | Rain Sounds | 1 Hour",
    "Anxiety Relief Music 💆 | Peaceful Sleep | 1 Hour",
    "Beautiful Sleep Music 🌸 | Relaxing Sounds | 1 Hour",
    "Night Meditation Music 🌃 | Deep Sleep | 1 Hour",
    "Stress Relief Music 🍃 | Rain Sounds | 1 Hour",
    "Gentle Sleep Music ☁️ | Calm Night | 1 Hour",
    "Ocean Sleep Music 🌊 | Deep Relaxation | 1 Hour",
    "Forest Sleep Music 🌲 | Nature Sounds | 1 Hour",
    "Moonlight Sleep Music 🌕 | Peaceful Night | 1 Hour",
    "Starlight Sleep Music ⭐ | Calm Music | 1 Hour",
    "Waterfall Sleep Music 💧 | Stress Relief | 1 Hour",
    "Midnight Calm Music 🌑 | Deep Sleep | 1 Hour",
    "Inner Peace Music 🕊️ | Sleep Sounds | 1 Hour",
    "Positive Energy Music 🌈 | Relaxing Night | 1 Hour",
    "Mountain Sleep Music 🏔️ | Nature Sounds | 1 Hour",
    "Garden Sleep Music 🌺 | Peaceful Music | 1 Hour",
    "Wind Sleep Music 🌬️ | Calm Sounds | 1 Hour",
    "White Noise Sleep 🤍 | Deep Rest | 1 Hour",
    "Thunder Sleep Music ⛈️ | Rain Sounds | 1 Hour",
    "Bamboo Forest Music 🎋 | Asian Calm | 1 Hour",
    "Crystal Bowl Music 🔮 | Healing Sounds | 1 Hour",
    "Piano Sleep Music 🎹 | Soft Music | 1 Hour",
    "Guitar Sleep Music 🎸 | Relaxing Night | 1 Hour",
    "Flute Sleep Music 🎵 | Peaceful Sleep | 1 Hour",
]

TAGS = [
    "sleep music", "relaxing music", "calm music",
    "deep sleep", "meditation music", "sleep aid",
    "stress relief", "anxiety relief", "peaceful music",
    "rain sounds", "nature sounds", "sleep sounds"
]

def get_youtube_service():
    creds = google.oauth2.credentials.Credentials(
        token=None,
        refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
        client_id=os.environ["YOUTUBE_CLIENT_ID"],
        client_secret=os.environ["YOUTUBE_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token"
    )
    return build("youtube", "v3", credentials=creds)

def upload_video(youtube, video_file, title):
    description = f"""{title}

Welcome to Nature's Hush — your daily sanctuary for deep sleep and relaxation.

🌧️ Perfect for sleep, study, and relaxation
💤 Helps with insomnia and anxiety
🎧 Best experienced with headphones or speaker
🔔 Subscribe for daily sleep music

#{title.split()[0]}Sleep #DeepSleep #RelaxingMusic #SleepMusic #CalmMusic #RainSounds #NatureSounds #Meditation #StressRelief #AnxietyRelief
"""

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": TAGS,
            "categoryId": "10",
            "defaultLanguage": "en"
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(
        video_file,
        mimetype="video/mp4",
        resumable=True,
        chunksize=1024*1024*5
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = request.execute()
    print(f"✅ Uploaded! Video ID: {response['id']}")
    print(f"✅ Title: {title}")
    return response['id']

day = int(os.environ.get("DAY_OFFSET", 0)) % len(VIDEOS)
title = VIDEOS[day]

youtube = get_youtube_service()
upload_video(youtube, "output.mp4", title)
