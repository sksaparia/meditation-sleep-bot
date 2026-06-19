import os
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCRIPTS_TITLES = [
    "Deep Sleep Meditation 😴 | Calm Your Mind Tonight",
    "Rain Sound Relaxation 🌧️ | Fall Asleep Fast",
    "Body Scan Sleep Meditation 🌙 | Release All Tension",
    "Midnight Calm Meditation ✨ | Peaceful Sleep Music",
    "Forest Sleep Journey 🌲 | Nature Sleep Meditation",
    "Ocean Wave Sleep 🌊 | Deep Relaxation Tonight",
    "Anxiety Release Meditation 💆 | Sleep Without Worry",
    "Gratitude Sleep Meditation 🙏 | Peaceful Night Rest",
    "Healing Sleep Meditation 💫 | Restore Your Body Tonight",
    "White Light Relaxation 🤍 | Deep Sleep Meditation",
    "Stress Release Sleep 🌿 | Let Go and Rest Tonight",
    "Mindful Breathing Sleep 🧘 | 4-4-4 Breathing Technique",
    "Peaceful Night Meditation 🌃 | Calm Sleep Music",
    "Cloud Visualization Sleep ☁️ | Float Into Deep Rest",
    "Mountain Peace Meditation 🏔️ | Calm Lake Sleep Music",
    "Moonlight Sleep Meditation 🌕 | Healing Night Energy",
    "Inner Peace Journey 🕊️ | Deep Relaxation Sleep",
    "Tension Release Meditation 💤 | Full Body Relaxation",
    "Positive Dreams Meditation 🌈 | Beautiful Sleep Tonight",
    "Energy Reset Sleep 🔋 | Recharge Your Body Tonight",
    "Letting Go Sleep Meditation 🍃 | Release and Rest",
    "Deep Rest Meditation 🌑 | Sleep Mode Activated",
    "Comfort Sleep Meditation 🛏️ | Most Relaxing Sleep Aid",
    "Night Sky Meditation ⭐ | Count Stars to Sleep",
    "Gentle Wind Sleep 🌬️ | Carry Stress Away Tonight",
    "Garden of Rest Meditation 🌸 | Peaceful Night Garden",
    "Sound of Silence Meditation 🤫 | Deep Peaceful Sleep",
    "Waterfall Calm Meditation 💧 | Constant Sound for Sleep",
    "Starlight Sleep Meditation 🌟 | Healing Energy Tonight",
    "Final Rest Meditation 🌙 | Your Time to Sleep Now",
]

TAGS = [
    "sleep meditation", "relaxation", "calm music",
    "deep sleep", "meditation", "sleep aid",
    "stress relief", "anxiety relief", "peaceful sleep",
    "sleep sounds", "bedtime meditation"
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

def upload_video(youtube, video_file, title, description, tags):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "22",
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
        resumable=True
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = request.execute()
    print(f"Uploaded! Video ID: {response['id']}")
    return response['id']

day = int(os.environ.get("DAY_OFFSET", 0)) % len(SCRIPTS_TITLES)
title = SCRIPTS_TITLES[day]

description = f"""{title}

Welcome to Sleep & Calm — your daily meditation channel for deep sleep and relaxation.

🌙 Listen every night before bed
💤 Perfect for insomnia and anxiety
🎧 Best with headphones or speaker

#SleepMeditation #DeepSleep #Relaxation #CalmMusic #MeditationForSleep

Subscribe for daily sleep meditations 🔔
"""

youtube = get_youtube_service()
upload_video(youtube, "output.mp4", title, description, TAGS)
