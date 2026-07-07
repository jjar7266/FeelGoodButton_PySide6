[![Sponsor](https://img.shields.io/badge/Sponsor-❤️-red)](https://github.com/sponsors/jjar7266)

<a href="https://buymeacoffee.com/jjar7266" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174">
</a>

# FeelGoodButton_PySide6

FeelGoodButton_PySide6 is a playful PySide6 desktop app featuring a custom round button that plays random motivational audio clips. Built with clean, modern Python and PySide6 architecture, this tiny morale‑boosting widget is designed to brighten your day with a single click.

The app automatically scans the `sounds/` folder and loads **any number of MP3 files** — no hard‑coding required. Drop in 1 sound or 100 sounds, and the app instantly adapts.

---

## ⭐ Features
- Custom circular PySide6 button
- Hover and press visual effects
- Toggle playback (click to play, click again to stop)
- Auto‑scan sound folder (no manual file listing)
- Lightweight, minimal UI
- Frameless draggable window
- ESC key closes the app
- Clean, class‑based architecture
- Easy to package into a portable desktop app

---

## ⭐ Purpose
FeelGoodButton_PySide6 is a simple, joyful desktop toy meant to deliver a quick boost of positivity.
Press the button → hear a motivational sound → feel good → keep going.

---

## ⭐ Tech Stack
- Python 3.x
- PySide6
- QtMultimedia
- pathlib

---

## ⭐ Installation

```bash
uv venv
source .venv/bin/activate
uv add PySide6
python main.py
```

Place your MP3 files inside the `sounds/` folder.
The app will automatically detect them.

---

## ⭐ Packaging (PyInstaller Example)

```bash
pyinstaller main.py --noconfirm --windowed --add-data "sounds/*.mp3;sounds"
```

---

## ⭐ Upgrade Roadmap (TODO)

This project is intentionally small, fun, and easy to expand.
Below is the official TODO Upgrade List for future development.

### 🎨 LEVEL 1 — Button Visual Upgrades
- Glow Animation — soft halo while sound plays
- Pulse Animation — gentle heartbeat effect
- Random Color Mode — new color on each click
- Color Themes — Calm, Happy, Energy, Chill
- Tiny “X” Close Button — drawn inside the toy window

### 🔊 LEVEL 2 — Sound System Upgrades
- Support More Formats — WAV, OGG, FLAC
- No‑Repeat Randomizer — avoid repeating the last sound
- Sound Categories — organize sounds into folders
- Playlist Mode — play sounds in order
- Shuffle Mode — shuffle all sounds without repeats

### 🪟 LEVEL 3 — Window Behavior Upgrades
- Resize Animation — window grows/shrinks with sound
- Snap‑to‑Edges — magnetic snapping to screen edges
- Shake Animation — shake window when sound stops
- Transparency Mode — window becomes translucent when idle

### ⚙️ LEVEL 4 — Utility / App Features
- Volume Slider — control audio output
- Mini Settings Window — volume, theme, category, play mode
- Sound Name Display — show currently playing sound
- Auto‑Hide Mode — hide window after inactivity
- Startup Position Memory — remember last window position

### 📦 LEVEL 5 — Packaging & Distribution
- PyInstaller Packaging — build a standalone EXE
- Custom App Icon — FeelGoodButton icon
- Installer / Setup Wizard — simple installer for distribution

### 🎮 LEVEL 6 — Game Modes (Optional Fun Stuff)
- Reaction Game Mode — click fast when button lights up
- Memory Mode — guess which sound was played
- Slot Machine Mode — spin colors + sounds
- Combo Mode — repeat sound sequences

---

## ⭐ License
This project is open‑source. Feel free to fork, modify, and build upon it.

---

## 👨‍💻 Author
**Jose "Joe" Ruiz**
Self‑Taught Python & GUI Developer — specializing in modern PySide6 and Tkinter desktop applications
GitHub: [@jjar7266](https://github.com/jjar7266)
Location: Coral Springs, FL, USA
