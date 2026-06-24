# 📋 QuickClip — Clipboard & Screenshot Monitor

QuickClip is a lightweight, cross-platform tool that monitors your clipboard text history and system screenshots, dynamically compiling them into a beautiful, live-updating HTML dashboard. 

It handles background text polling, automatically tracks screenshot directories, and supports active window capture via a global keyboard shortcut.

---

## ✨ Features

- **📝 Clipboard Text Monitoring**: Automatically listens for newly copied text snippets in the background, adding them to your history and highlighting code snippets.
- **📸 Screenshot Watching**: Watches default OS screenshot folders using `watchdog` (relying on low CPU usage event listeners) with a fallback to polling if the package is missing.
- **🖼️ Clipboard Image Monitor**: (macOS/Linux) Captures screenshots directly from clipboard-based tools (like Flameshot or native hotkeys) and saves them locally.
- **⌨️ Active Window Capture Hotkey**: Press **`Ctrl + Alt + Q`** to instantly snap a high-resolution, cropped screenshot of your active window.
- **🖥️ Windows DPI-Awareness**: Prevents coordinate misalignment on high-DPI/display-scaled screens, ensuring active window screenshots fit window bounds perfectly.
- **🌐 Responsive HTML Dashboard**: A beautiful, premium glassmorphism dark dashboard (`viewer.html`) with:
  - Full-text search and filtering.
  - One-click copy for text clips.
  - Persistent scroll position and search queries across reloads.
  - Image lightbox zoom view for screenshots.
  - Focus-triggered and timed auto-reloading.

---

## 📁 Folder Structure

The project is split into a modular format for high readability and maintainability:

```text
e:\py
├── README.md                  # Project documentation
├── quickclip.py               # Root entry point wrapper
└── quickclip_core/            # Package directory
    ├── __init__.py            # Package initialization
    ├── config.py              # Constants, OS settings, and watch directory resolution
    ├── storage.py             # File reading, writing, and base64 thumbnail rendering
    ├── viewer.py              # HTML dashboard template and file compiler
    ├── clipboard.py           # Clipboard text listener daemon thread
    ├── screenshot.py          # Watchdog and clipboard image listeners
    └── listener.py            # Main runner, banner printing, and hotkey listeners
```

---

## 🚀 Getting Started

### 1. Virtual Environment & Installation

Ensure you have Python 3.8+ installed.

#### Step 1: Create a Virtual Environment
```bash
# Create the environment named 'venv'
python -m venv venv
```

#### Step 2: Activate the Virtual Environment
```bash
venv\Scripts\Activate
```

#### Step 3: Install Dependencies
Install the required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```


### 2. Running QuickClip

To start the monitors, run the root wrapper script:

```bash
python quickclip.py
```

Upon launching, the script prints a dashboard status banner showing:
- Active screenshot directories being monitored.
- Saved files directory path.
- The path to the live HTML dashboard file.

### 3. Usage Controls

- **Automatic Logging**: Any plain text you copy or screenshot you take (via standard print-screen tools) is automatically logged.
- **Active Window Capture**: Press **`Ctrl + Alt + Q`** to capture only the active window.
- **Accessing Dashboard**: Open the generated `viewer.html` located in your system's home directory under `~/QuickClip_Notes/viewer.html` in any web browser.
- **Termination**: Press `Ctrl + C` in the console window to safely exit the monitor.

---

## ⚙️ Configuration & Data Storage

All logged data is saved inside your user home directory:

- **Directory Path**: `~/QuickClip_Notes/` (e.g., `C:\Users\Username\QuickClip_Notes` on Windows)
- **`clips.json`**: Stores the raw history of copied text (up to 500 clips).
- **`screenshots.json`**: Stores screenshot metadata and inline base64 thumbnails (up to 200 screenshots).
- **`screenshots/`**: Stores local copy images of captured/detected screenshots.
- **`viewer.html`**: The HTML UI dashboard.
