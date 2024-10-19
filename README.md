# Simple_Key_logger
# Python Keylogger (Educational Use Only)

⚠️ **Disclaimer** ⚠️  
This keylogger is intended solely for educational purposes to demonstrate how keylogging works and to understand potential cybersecurity risks. It should only be used on systems that you own or have explicit permission to monitor. The author does not condone illegal or unethical use of this software. Any misuse for unauthorized data collection or spying is strictly prohibited and may lead to legal consequences. Use this tool responsibly and adhere to all applicable laws and regulations.

---

## About

This Python script listens for key presses on the system and prints the captured keystrokes in real-time to the console. It uses the `pynput` library to listen for keyboard events and demonstrates the basic functionality of a keylogger. The script does **not** save the key presses to a file but outputs them directly to the terminal.

## How It Works

- The script listens for all key presses made on the system.
- It captures and prints the keystrokes to the console in real-time.
- The `pynput` library is used to listen for keyboard events.

### Prerequisites

- Python 3.x
- `pynput` library (Install via `pip install pynput`)
