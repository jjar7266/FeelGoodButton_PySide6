# ==========================================================
# main.py
# Our Main Window for the FeelGoodButton App
# Written in teacher mode so beginners can learn!
# Coded by Jose "Joe" Ruiz
# ==========================================================

# First, we import the PySide6 tools we need.
# QApplication runs our whole app.
# QWidget is the base class for windows.
# QVBoxLayout helps us center our button
# QMediaPlayer + QAudioOutput let us paly sounds.
# random helps us pick a random sound.

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt, QUrl
import random
import sys

# Import our custom RoundButton widget
from round_button import RoundButton


# ==============================================================
# MainWindow Class
# This creates our tiny borderless window with one round button.
# ==============================================================

class MainWindow(QWidget):
    """
    A small, friendly window that holds our RoundButton.
    When the button is clicked, we play a random sound!
    """

    def __init__(self):
        super().__init__()

        # --------------------------------------------------------------
        # WINDOW STYLE
        # We make the window BORDERLESS so it looks like a floating toy.
        # --------------------------------------------------------------
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |  # No title bar
            Qt.WindowType.WindowStaysOnTopHint   # Always on top
        )

        # Set a nice small size
        self.resize(200, 200)

        # Give the window a soft background color
        self.setStyleSheet("background-color: #222222; border-radius: 20px;")

        # --------------------------------------------------------------
        # LAYOUT
        # We use a vertical layout to center our round button.
        # --------------------------------------------------------------
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create our round button
        self.button = RoundButton("Feel Good")
        self.button.setFixedSize(150, 150)  # Make it nice and round

        # Add the button to the layout
        layout.addWidget(self.button)

        # Apply the layout to the window
        self.setLayout(layout)

        # ------------------------------------------------------------
        # SOUND SYSTEM
        # We create a media player and audio output.
        # ------------------------------------------------------------
        self.player = QMediaPlayer()
        self.audio  = QAudioOutput()
        self.player.setAudioOutput(self.audio)

        # List of sound files (you can add more!)
        # Make sure these files exist in your project folder.
        self.sounds = [
            "sounds/feelgood1.mp3",
            "sounds/feelgood2.mp3",
            "sounds/feelgood3.mp3"
        ]

        # Connect the button click to our play_sound function
        self.button.clicked.connect(self.play_sound)

    # ================================================================
    # PLAY SOUND FUNCTION
    # This picks a random sound and plays it.
    # ================================================================

    def play_sound(self):
        """Pick a random sound and play it."""
        sound_file = random.choice(self.sounds)
        url = QUrl.fromLocalFile(sound_file)
        self.player.setSource(url)
        self.player.play()


# =====================================================================
# APP STARTUP
# This is the part that launches the app.
# =====================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    
