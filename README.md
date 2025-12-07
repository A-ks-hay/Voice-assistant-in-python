# JARVIS Voice Assistant (Python + PyQt5)

This project is a desktop-based AI voice assistant built using Python, PyQt5, and Speech Recognition.
It performs tasks such as opening websites, playing YouTube videos, telling time, searching Wikipedia, and more — similar to Marvel's JARVIS UI system.

# Features

✔️ Voice-activated command processing
✔️ Text-to-speech response (pyttsx3)
✔️ GUI with animated AI GIF
✔️ Commands like:

🎬 Play <song> → Plays on YouTube

🌐 Open YouTube

📖 Search <topic> → Speaks summary from Wikipedia

🕒 Time → Tells current time

👋 Hello Jarvis → Greeting mode

🔴 Shutdown / Bye / Stop → Closes the app

# Requirements / Dependencies

Install these Python libraries before running the assistant:

pip install PyQt5
pip install speechrecognition
pip install pyttsx3
pip install wikipedia
pip install pywhatkit
pip install pyaudio


Note: Windows users may need to install PyAudio manually if it fails:

pip install pipwin
pipwin install pyaudio

Make sure the processing.gif file is in the same folder as the Python script.

# How to Run
python jarvis.py


Once started, JARVIS will greet you and wait for voice commands.

# Supported Voice Commands
Command Example	Action
Open YouTube	Opens youtube.com
Play shape of you	Plays song on YouTube
Search India history	Reads Wikipedia summary
Time	Tells current system time
Hello Jarvis	Assistant replies
Shutdown / Stop / Bye	Close the assistant

# To-Do / Future Ideas

✨ Add weather updates
✨ Add alarm system
✨ Add chatbot mode
✨ Add custom hotword detection (“Hey Jarvis”)
✨ Add system controls (volume, apps, brightness etc.)

# Author

👤 Akshay Kumar
📍 India

⭐ If you like it, upgrade it — make your own version of JARVIS!
