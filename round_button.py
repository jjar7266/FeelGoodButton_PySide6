# ===========================================================
# round_button.py
# Our Custom Round Button Widget
# Written in teacher mode so beginners can learn!
# Coded by Jose "Joe" Ruiz
# ===========================================================

# Import the PySide6 tools we need.
# QPushButton is the normal button class.
# QPainter helps us draw shapes (like circles!).
# QColor lets us pick colors.
# Qt gives us alignment flags, mouse buttons, cursor shapes, etc.

from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QPainter, QBrush, QPen, QColor
from PySide6.QtCore import Qt, QRectF


# ============================================================
# RoundButton Class
# This class creates a BUTTON that is ROUND instead of square.
# We draw it ourselves using QPainter.
#
# NEW FEATURES:
#   ✔ Custom color support (bright red, blue, anything!)
#   ✔ Automatic hover color (lighter)
#   ✔ Automatic press color (darker)
#   ✔ All Qt6 enums fully qualified (VSCode‑safe)
#   ✔ Fully commented for beginners
# ============================================================

class RoundButton(QPushButton):
    """
    A friendly, round button that changes color when you hover
    or click it. Perfect for our FeelGoodButton project!
    """

    def __init__(self, text="Feel Good", color="#ff0000", parent=None):
        """
        NEW: Added a 'color' parameter so the user can choose
        any button color they want. Default is bright red (#ff0000).
        """

        # Call the QPushButton constructor so it sets itself up.
        super().__init__(text, parent)

        # Save the chosen base color
        self.base_color = QColor(color)

        # Make the mouse cursor turn into a pointing hand.
        # Qt6 requires the explicit enum namespace:
        # Qt.CursorShape.PointingHandCursor
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # These booleans help us know what the mouse is doing.
        self._hovering = False
        self._pressed  = False

        # ---------------------------------------------------------
        # COLORS!
        # Instead of hard-coding green, we now generate colors
        # based on the user's chosen base color.
        #
        # QColor.lighter(120) makes the color 20% lighter.
        # QColor.darker(120) makes the color 20% darker.
        # ---------------------------------------------------------
        self.normal_color = self.base_color
        self.hover_color  = self.base_color.lighter(120)
        self.press_color  = self.base_color.darker(120)
        self.text_color   = QColor("#FFFFFF")     # White text

        # Remove the default button border and background
        # so we can draw our own circle.
        self.setStyleSheet("border: none; background: transparent;")

    # ==============================================================
    # MOUSE EVENTS
    # These functions let us know when the mouse enters,
    # leaves, presses, or releases the button.
    # ==============================================================

    def enterEvent(self, event):
        # Mouse moved over the button
        self._hovering = True
        self.update()  # Redraw the button
        super().enterEvent(event)

    def leaveEvent(self, event):
        # Mouse moved away from the button
        self._hovering = False
        self.update()
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        # Mouse clicked the button
        # Qt6 explicit enum: Qt.MouseButton.LeftButton
        if event.button() == Qt.MouseButton.LeftButton:
            self._pressed = True
            self.update()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # Mouse released the button
        if self._pressed:
            self._pressed = False
            self.update()
        super().mouseReleaseEvent(event)

    # ===============================================================
    # PAINTING THE BUTTON
    # This is where the magic happens!
    # We draw a circle and put text in the middle.
    # ===============================================================

    def paintEvent(self, event):
        # QPainter is our "paintbrush" for drawing.
        painter = QPainter(self)

        # Qt6 explicit enum: QPainter.RenderHint.Antialiasing
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Pick the right color depending on what the mouse is doing.
        if self._pressed:
            color = self.press_color
        elif self._hovering:
            color = self.hover_color
        else:
            color = self.normal_color

        # Create a rectangle the size of the button.
        # We will draw a circle inside this rectangle.
        rect = QRectF(0, 0, self.width(), self.height())

        # Draw the circle
        painter.setBrush(QBrush(color))

        # Qt6 explicit enum: Qt.PenStyle.NoPen
        painter.setPen(QPen(Qt.PenStyle.NoPen))
        painter.drawEllipse(rect)

        # Draw the text in the center of the circle
        painter.setPen(QPen(self.text_color))

        # Qt6 explicit enum: Qt.AlignmentFlag.AlignCenter
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, self.text())
