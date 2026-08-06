from gtts import gTTS
import platform
import subprocess

# Read text from file
with open("abc.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Convert text to speech
tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

# Detect OS and play the audio
os_name = platform.system()

if os_name == "Windows":
    subprocess.run(["cmd", "/c", "start", "", "voice.mp3"], shell=True)
elif os_name == "Darwin":  # macOS
    subprocess.run(["afplay", "voice.mp3"])
elif os_name == "Linux":
    subprocess.run(["xdg-open", "voice.mp3"])