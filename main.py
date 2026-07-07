# ==========================================================
# main.py
# Our Main Window for the FeelGoodButton App
# Written in teacher mode so beginners can learn!
# Coded by Jose "Joe" Ruiz
# ==========================================================

# First, we import the PySide6 tools we need.
# QApplication runs our whole app.
# QWidget is the base class for windows.
# QVBoxLayout helps us center our button.
# QMediaPlayer + QAudioOutput let us play sounds.
# QUrl helps us load local files.
# Qt gives us window flags, alignment flags, mouse buttons, etc.
# Path helps us build safe file paths.

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt, QUrl, QPoint
from pathlib import Path
import random
import sys

# Import our custom RoundButton widget
from round_button import RoundButton


# ==============================================================
# PATH SETUP
# ==============================================================
# BASE_DIR points to the folder where this script lives.
# SOUNDS_DIR points to the "sounds" folder inside the project.

BASE_DIR = Path(__file__).resolve().parent
SOUNDS_DIR = BASE_DIR / "sounds"


# ==============================================================
# MainWindow Class
# This creates our tiny borderless window with one round button.
# ==============================================================

class MainWindow(QWidget):
    """
    A small, friendly window that holds our RoundButton.
    When the button is clicked, we play (or stop) a random sound!
    """

    def __init__(self):
        super().__init__()

        # --------------------------------------------------------------
        # WINDOW STYLE
        # We make the window BORDERLESS so it looks like a floating toy.
        # Qt6 explicit enums:
        #   Qt.WindowType.FramelessWindowHint
        #   Qt.WindowType.WindowStaysOnTopHint
        # --------------------------------------------------------------
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )

        # Set a nice small size
        self.resize(200, 200)

        # Give the window a soft background color
        self.setStyleSheet("background-color: #222222; border-radius: 20px;")

        # --------------------------------------------------------------
        # LAYOUT
        # We use a vertical layout to center our round button.
        # Qt6 explicit enum: Qt.AlignmentFlag.AlignCenter
        # --------------------------------------------------------------
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --------------------------------------------------------------
        # CREATE OUR ROUND BUTTON
        # NEW: We pass a custom color so VSCode does not flag anything.
        # --------------------------------------------------------------
        self.button = RoundButton("Feel Good", color="#ff0000")
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

        # ------------------------------------------------------------
        # AUTO-SCAN THE SOUNDS FOLDER
        # This line finds EVERY .mp3 file inside the "sounds" folder.
        # It does not matter how many files you add — the app will
        # automatically detect them without changing any code.
        #
        # Example:
        #   sounds/
        #       happy1.mp3
        #       happy2.mp3
        #       laugh.mp3
        #       ding.mp3
        #
        # All of these will be loaded automatically.
        # ------------------------------------------------------------
        self.sounds = list(SOUNDS_DIR.glob("*.mp3"))

        # SAFETY CHECK:
        # If the folder is empty, the app will not crash.
        # Instead, we simply disable the button.
        if not self.sounds:
            print("No MP3 files found in the sounds folder!")
            self.button.setEnabled(False)

        # Connect the button click to our play_sound function
        self.button.clicked.connect(self.play_sound)

        # ------------------------------------------------------------
        # WINDOW DRAGGING SUPPORT
        # Frameless windows cannot be dragged unless we add this.
        # ------------------------------------------------------------
        self._drag_position = QPoint()

    # ================================================================
    # PLAY SOUND FUNCTION
    # NEW: This now acts like a TOGGLE.
    # If sound is playing → clicking stops it.
    # If sound is stopped → clicking plays a random sound.
    # ================================================================

    def play_sound(self):
        """Play or stop a random sound."""

        # If already playing, stop immediately
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.stop()
            return

        # Pick a random sound from the auto-scanned list
        sound_path = random.choice(self.sounds)

        # Convert Path -> QUrl
        url = QUrl.fromLocalFile(str(sound_path))

        self.player.setSource(url)
        self.player.play()

    # ================================================================
    # ESC KEY CLOSES THE APP
    # Frameless windows have no close button, so we add our own.
    # ================================================================

    def keyPressEvent(self, event):
        """Close the app when ESC is pressed."""
        if event.key() == Qt.Key.Key_Escape:
            QApplication.quit()

    # ================================================================
    # WINDOW DRAGGING (for frameless windows)
    # ================================================================

    def mousePressEvent(self, event):
        """Record the mouse position when the user clicks."""
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_position = event.globalPosition().toPoint()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """Move the window while dragging with the left mouse button."""
        if event.buttons() & Qt.MouseButton.LeftButton:
            new_pos = event.globalPosition().toPoint()
            offset = new_pos - self._drag_position
            self.move(self.pos() + offset)
            self._drag_position = new_pos
        super().mouseMoveEvent(event)


# =====================================================================
# APP STARTUP
# This is the part that launches the app.
# =====================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
