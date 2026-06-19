from gtts import gTTS
import subprocess
import os

SCRIPTS = [
    ("Deep Sleep Meditation", "Close your eyes... take a deep breath in... and slowly breathe out... let your body become heavy... feel every muscle relaxing... you are safe... you are calm... drift into peaceful sleep..."),
    ("Rain Sound Relaxation", "Listen to the gentle rain falling softly... each drop washes away your stress... your mind becomes still and quiet... breathe slowly... you are completely relaxed... sleep is coming to you now..."),
    ("Body Scan Sleep", "Begin at your toes... feel them relax completely... move up to your feet... your ankles... your legs are heavy and warm... your entire body is sinking deeper into rest... sleep peacefully now..."),
    ("Midnight Calm", "The night is quiet and peaceful... stars are shining above you... you are wrapped in warmth and safety... every breath takes you deeper into relaxation... let go of all thoughts... sleep deeply..."),
    ("Forest Sleep Journey", "Imagine you are lying in a peaceful forest... birds are singing softly... a gentle breeze touches your face... nature surrounds you with calm energy... breathe in the fresh air... sleep now..."),
    ("Ocean Wave Sleep", "Waves are gently rolling to shore... in and out... in and out... your breathing matches the rhythm of the ocean... slow and steady... your mind is clear and empty... you fall into deep sleep..."),
    ("Anxiety Release Meditation", "Release all worries now... they do not serve you tonight... breathe out tension... breathe in peace... your chest feels lighter... your mind feels free... tonight you sleep without fear or worry..."),
    ("Gratitude Sleep", "Think of one good thing from today... hold it gently in your mind... feel warmth in your heart... you are grateful... you are blessed... with this peaceful feeling carry you into deep restful sleep..."),
    ("Healing Sleep", "As you sleep tonight your body heals... your mind resets... every cell in your body is restoring itself... you wake up tomorrow feeling refreshed and strong... sleep is your superpower... sleep deeply now..."),
    ("White Light Relaxation", "Imagine a warm white light above you... it slowly moves down through your head... your neck... your shoulders... melting away all tension... filling you with peace... you are completely relaxed... sleep now..."),
    ("Stress Release", "Today is over now... whatever happened today is done... you did your best... now it is time to rest... let your shoulders drop... unclench your jaw... soften your hands... breathe and sleep..."),
    ("Mindful Breathing Sleep", "Focus only on your breath... breathe in for four counts... hold for four... breathe out for four... again... in... hold... out... your mind is calm... your body is ready for sleep..."),
    ("Peaceful Night", "The world is quiet now... everyone is resting... you deserve rest too... close your eyes and let darkness comfort you... this is your safe time... your healing time... sleep deeply and peacefully..."),
    ("Cloud Visualization", "Imagine floating on a soft white cloud... it holds you gently... you drift higher into the calm sky... everything below feels small and far away... you feel weightless and free... sleep now..."),
    ("Mountain Peace", "Picture a calm mountain lake at night... the water is perfectly still... reflecting the moonlight... you sit peacefully by the shore... breathing cool fresh air... your heart is quiet... sleep comes easily..."),
    ("Moonlight Sleep", "The moon is shining softly through your window... it watches over you as you sleep... you are protected... you are loved... the silver light brings you calmness and deep healing sleep tonight..."),
    ("Inner Peace Journey", "Go deep inside yourself now... find that quiet place within... it is always there waiting for you... in this place there is no worry... no rush... only stillness and peace... rest here tonight..."),
    ("Tension Release", "Start with your forehead... relax it completely... now your eyes... your cheeks... your jaw... feel the tension leaving your face... moving down through your neck and shoulders... you are melting into rest..."),
    ("Positive Dreams", "Tonight you will have beautiful peaceful dreams... your subconscious mind is ready to take you on a gentle journey... full of color and warmth... close your eyes and welcome wonderful dreams..."),
    ("Energy Reset", "Your body has worked hard today... now it needs to recharge... like a phone plugged in at night... you are restoring your energy... every minute of sleep makes you stronger... sleep fully and deeply..."),
    ("Letting Go Sleep", "Let go of yesterday... let go of tomorrow... there is only this moment... this breath... this peaceful darkness... nothing needs your attention right now... everything can wait... just sleep and restore..."),
    ("Deep Rest", "You are entering deep rest now... your heart rate slows... your breathing deepens... your brain waves shift to sleep mode... your body knows exactly what to do... trust the process... sleep deeply..."),
    ("Comfort Sleep", "You are in the most comfortable position right now... your pillow supports you perfectly... your blanket is warm... everything is just right... you have nothing to do but sleep... enjoy this feeling..."),
    ("Night Sky Meditation", "Look up at the endless night sky in your mind... count the stars slowly... one... two... three... each star takes you deeper into relaxation... by ten you will be fast asleep... four... five... six..."),
    ("Gentle Wind Sleep", "A gentle warm wind blows softly around you... it carries away all stress... all worry... all heaviness from your day... you feel lighter with every breath... the wind sings you to sleep softly..."),
    ("Garden of Rest", "Walk slowly through a beautiful night garden... jasmine flowers fill the air with sweetness... soft grass under your feet... fireflies dancing around you... find your bench and sit... close your eyes... sleep..."),
    ("Sound of Silence", "Listen to the silence around you... in the silence there is peace... in the silence there is safety... breathe into the silence... let it fill your entire body... you are one with the calm night... sleep..."),
    ("Waterfall Calm", "Hear a distant waterfall... the constant sound soothes your mind... it drowns out all other thoughts... just the water... flowing endlessly... peacefully... rhythmically... carrying you into deep sleep now..."),
    ("Starlight Sleep", "Starlight falls gently on you tonight... each ray carries healing energy... filling you with calm and peace... your body absorbs this light... every cell relaxes... you glow with peaceful energy... sleep now..."),
    ("Final Rest", "This is your time now... no phone... no worries... no tomorrow... just you and this moment of peace... you have earned this rest... take it fully... breathe slowly... close your eyes... and sleep..."),
]

def generate_audio(text, filename):
    tts = gTTS(text=text, lang='en', slow=True)
    tts.save(filename)

def create_video(audio_file, animation_file, output_file):
    subprocess.run([
        "ffmpeg", "-stream_loop", "-1",
        "-i", animation_file,
        "-i", audio_file,
        "-shortest",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "192k",
        "-y",
        output_file
    ])

day = int(os.environ.get("DAY_OFFSET", 0)) % len(SCRIPTS)
title, script = SCRIPTS[day]

print(f"Generating: {title}")
generate_audio(script, "audio.mp3")
create_video("audio.mp3", "animations/rain_loop.mp4", "output.mp4")
print(f"Done! Video ready: {title}")
