import sys
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie, QFont

# ---------------- Text To Speech ----------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------- GUI ----------------
class JarvisUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JARVIS AI")
        self.setGeometry(250, 100, 600, 600)
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()

        # Animation GIF
        self.label_animation = QLabel(self)
        self.label_animation.setAlignment(Qt.AlignCenter)
        movie = QMovie("processing.gif")   # <-- put your GIF same folder
        self.label_animation.setMovie(movie)
        movie.start()

        # Text Box
        self.label_text = QLabel("Hello Boss, I am Jarvis.\nHow may I assist you?")
        self.label_text.setAlignment(Qt.AlignCenter)
        self.label_text.setStyleSheet("color: cyan;")
        self.label_text.setFont(QFont("Arial", 17))

        layout.addWidget(self.label_animation)
        layout.addWidget(self.label_text)

        self.setLayout(layout)

        # Start Voice Loop
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.listen_command)
        self.timer.start(3000)

    # ---------------- Voice Recognition ----------------
    def listen_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You Said:", command)
            self.label_text.setText(f"Command: {command}")
            self.process_command(command)

        except:
            pass

    # ---------------- Command Processing ----------------
    def process_command(self, command):

        if "open youtube" in command:
            speak("Opening YouTube Boss")
            self.label_text.setText(">>> Opening YouTube 🔥")
            webbrowser.open("https://youtube.com")

        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            self.label_text.setText(f">>> Playing {song} 🎧")
            pywhatkit.playonyt(song)

        elif "wikipedia" in command or "search" in command:
            topic = command.replace("wikipedia", "").replace("search", "")
            speak(f"Searching {topic}")
            result = wikipedia.summary(topic, sentences=2)
            self.label_text.setText(f">>> {result}")
            speak(result)

        elif "time" in command:
            from datetime import datetime
            now = datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")
            self.label_text.setText(f">>> Time: {now}")

        elif "hello jarvis" in command or "hi jarvis" in command:
            speak("Hello Boss")
            self.label_text.setText(">>> Hello Boss 👋")

        elif "bye" in command or "shutdown" in command or "stop" in command:
            speak("Goodbye Boss, shutting down.")
            self.label_text.setText(">>> SHUTTING DOWN 🛑")
            QTimer.singleShot(2000, exit)


# ---------------- Run the App ----------------
app = QApplication(sys.argv)
UI = JarvisUI()
UI.show()
speak("Hello Boss, I am Jarvis. How may I help you?")
sys.exit(app.exec_())
