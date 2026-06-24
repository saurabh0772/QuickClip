import time
import subprocess
from quickclip_core.config import OS
from quickclip_core.storage import add_clip
from quickclip_core.viewer import generate_viewer

def get_clipboard_text() -> str:
    """Read plain-text from the system clipboard, cross-platform."""
    if OS == "Windows":
        try:
            import pyperclip
            return pyperclip.paste() or ""
        except Exception:
            pass

    if OS == "Linux":
        for cmd in (
            ["wl-paste", "-n"],
            ["xclip", "-selection", "clipboard", "-o"],
            ["xsel", "--clipboard", "--output"],
        ):
            try:
                res = subprocess.run(cmd, capture_output=True, text=True, check=True)
                return res.stdout or ""
            except (subprocess.SubprocessError, FileNotFoundError):
                pass

    # Generic / macOS fallback
    try:
        import pyperclip
        return pyperclip.paste() or ""
    except Exception as e:
        print(f"⚠️ Clipboard read error: {e}")
        if OS == "Linux":
            print("💡 Install xclip or wl-clipboard:")
            print("   Debian/Ubuntu: sudo apt install xclip wl-clipboard")
        return ""

def clipboard_monitor():
    """Background thread: polls clipboard for text every 0.5 s."""
    try:
        last_text = get_clipboard_text()
    except Exception:
        last_text = ""

    while True:
        try:
            time.sleep(0.5)
            current = get_clipboard_text()
            if current and current.strip() and current != last_text:
                last_text = current
                if add_clip(current):
                    generate_viewer()
                    print(f"  ✅ Clipboard: {current[:60].replace(chr(10),' ')}...")
        except Exception:
            pass
