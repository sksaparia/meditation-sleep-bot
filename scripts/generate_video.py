import subprocess
import os

VIDEOS = [
    ("Deep Sleep Music 😴 | Rain Sounds | 8 Hours", "rain"),
    ("Relaxing Sleep Music 🌧️ | Stress Relief | 8 Hours", "rain"),
    ("Peaceful Sleep Music 🌙 | Calm Your Mind | 8 Hours", "rain"),
    ("Sleep Instantly 💤 | Rain & Music | 8 Hours", "rain"),
    ("Deep Relaxation Music ✨ | Fall Asleep Fast | 8 Hours", "rain"),
    ("Healing Sleep Music 💫 | Nature Sounds | 8 Hours", "rain"),
    ("Calm Mind Music 🌿 | Rain Sounds | 8 Hours", "rain"),
    ("Anxiety Relief Music 💆 | Peaceful Sleep | 8 Hours", "rain"),
    ("Beautiful Sleep Music 🌸 | Relaxing Sounds | 8 Hours", "rain"),
    ("Night Meditation Music 🌃 | Deep Sleep | 8 Hours", "rain"),
    ("Stress Relief Music 🍃 | Rain Sounds | 8 Hours", "rain"),
    ("Gentle Sleep Music ☁️ | Calm Night | 8 Hours", "rain"),
    ("Ocean Sleep Music 🌊 | Deep Relaxation | 8 Hours", "rain"),
    ("Forest Sleep Music 🌲 | Nature Sounds | 8 Hours", "rain"),
    ("Moonlight Sleep Music 🌕 | Peaceful Night | 8 Hours", "rain"),
    ("Starlight Sleep Music ⭐ | Calm Music | 8 Hours", "rain"),
    ("Waterfall Sleep Music 💧 | Stress Relief | 8 Hours", "rain"),
    ("Midnight Calm Music 🌑 | Deep Sleep | 8 Hours", "rain"),
    ("Inner Peace Music 🕊️ | Sleep Sounds | 8 Hours", "rain"),
    ("Positive Energy Music 🌈 | Relaxing Night | 8 Hours", "rain"),
    ("Mountain Sleep Music 🏔️ | Nature Sounds | 8 Hours", "rain"),
    ("Garden Sleep Music 🌺 | Peaceful Music | 8 Hours", "rain"),
    ("Wind Sleep Music 🌬️ | Calm Sounds | 8 Hours", "rain"),
    ("White Noise Sleep 🤍 | Deep Rest | 8 Hours", "rain"),
    ("Thunder Sleep Music ⛈️ | Rain Sounds | 8 Hours", "rain"),
    ("Bamboo Forest Music 🎋 | Asian Calm | 8 Hours", "rain"),
    ("Crystal Bowl Music 🔮 | Healing Sounds | 8 Hours", "rain"),
    ("Piano Sleep Music 🎹 | Soft Music | 8 Hours", "rain"),
    ("Guitar Sleep Music 🎸 | Relaxing Night | 8 Hours", "rain"),
    ("Flute Sleep Music 🎵 | Peaceful Sleep | 8 Hours", "rain"),
]

def create_long_video(animation_file, music_file, output_file, duration=28800):
    # 8 ghante = 28800 seconds ka video
    subprocess.run([
        "ffmpeg",
        "-stream_loop", "-1", "-i", animation_file,  # video loop
        "-stream_loop", "-1", "-i", music_file,       # music loop
        "-t", str(duration),                           # 8 hours
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-y",
        output_file
    ])

day = int(os.environ.get("DAY_OFFSET", 0)) % len(VIDEOS)
title, style = VIDEOS[day]

print(f"Creating: {title}")
create_long_video(
    "animations/rain_loop.mp4",
    "animations/music.mp3",
    "output.mp4",
    duration=3600  # 1 hours
)
print(f"Done! Video ready: {title}")
