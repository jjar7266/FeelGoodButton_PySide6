# ===========================================================
# round_button.py
# Our Custom Round Button Widget
# Written in teacher mode so beginners can learn!
# Coded by Jose "Joe" Ruiz
# ===========================================================

# First, we import the PySide6 tools we need.
# QPushButton is the normal button class.
# QPainter helps us draw shapes (like circles!).
# QColor lets us pick colors.
# Qt gives us alignment and mouse button info.

# Import modules

from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QPainter, QBrush, QPen, QColor
from PySide6.QtCore import Qt, QRectF


# ============================================================
# RoundButton Class
# This class creates a BUTTON that is ROUND instead of square.
# We will draw it ourselves using QPainter.
# ============================================================

class RoundButton(QPushButton):
    """
    A friendly, round button that changes color when you hover
    or click it. Perfect for our FeelGoodButton project!
    """

    def __init__(self, text="Feel Good", parent=None):
        # Call the QPushBUtton constructor so it sets itself up.
        super().__init__(text, parent)

        # Make the mouse cursor turn into a pointing hand
        # so it feels like a real clickable button.
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # These booleans help us know what the mouse is doing.
        self._hovering = False
        self._pressed  = False

        # ---------------------------------------------------------
        # COLORS!
        # These are the colors our button will use.
        # You can change them to anything you like.
        # ---------------------------------------------------------
        self.normal_color = QColor("#4CAF50")     # Regular green
        self.hover_color  = QColor("#66BB6A")     # Lighter green
        self.press_color  = QColor("#388E3C")     # Darker green
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
        painter.setPen(QPen(Qt.PenStyle.NoPen))  # No border line
        painter.drawEllipse(rect)

        # Draw the text in the center of the circle
        painter.setPen(QPen(self.text_color))
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, self.text())

