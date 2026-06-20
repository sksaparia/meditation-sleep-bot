import subprocess
import os

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

def create_video(animation_file, music_file, output_file, duration=3600):
    subprocess.run([
        "ffmpeg",
        "-stream_loop", "-1", "-i", animation_file,
        "-stream_loop", "-1", "-i", music_file,
        "-t", str(duration),
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "192k",
        "-y",
        output_file
    ])

day = int(os.environ.get("DAY_OFFSET", 0)) % len(VIDEOS)
title = VIDEOS[day]

print(f"Creating: {title}")
create_video(
    "animations/rain_loop.mp4",
    "animations/music.mp3",
    "output.mp4",
    duration=3600
)
print(f"Done! Video ready: {title}")
