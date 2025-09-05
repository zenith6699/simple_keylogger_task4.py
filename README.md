# 🔑 Simple Python Keylogger (Built-in Modules Only)

> ⚠️ **DISCLAIMER:**  
> This keylogger is intended for **educational purposes only**.  
> Unauthorized use of keyloggers is **illegal and unethical**.  
> Only use this tool on devices you own or have explicit permission to monitor.

---

## 📌 Overview

This is a **simple keylogger written entirely in Python**, using only built-in modules. It captures keystrokes from the user and logs them into a file with timestamps.

---

## 🚀 Features

- Cross-platform support (Windows & Linux/Unix)
- Logs special keys like `[ENTER]`, `[TAB]`, `[ESC]`, etc.
- Timestamps for every key press
- Ethical warning before starting
- Minimal and clean output
- Option to view log after logging

---

## 🧱 Modules Used

- `os`
- `sys`
- `time`
- `datetime`
- `msvcrt` (for Windows)
- `tty`, `termios` (for Unix/Linux)

---

## 💻 How to Run

### 1. Clone or Download
```bash
git clone https://github.com/your-username/simple-keylogger.git
cd simple-keylogger
```

### 2. Run the Script
```bash
python keylogger.py
```

---

## 📂 Output

The script logs all keystrokes into a file named:

```
keylog.txt
```

Example log entry:
```
2025-09-05 23:00:01: H
2025-09-05 23:00:02: e
2025-09-05 23:00:03: [SPACE]
2025-09-05 23:00:04: [ENTER]
```

---

## 📜 Ethical Notice

Before logging begins, the user must consent to the following:

- You are using it on your own machine or have permission
- You understand the legal consequences of unethical use
- You acknowledge this is for learning purposes only

---

## 🛑 Stop Logging

To stop logging:
- Press `ESC` key
- Or press `Ctrl + C` (KeyboardInterrupt)

---

## 👁️ View Log

After logging, you will be asked if you'd like to view the contents of `keylog.txt`.

---

## ✅ Compatibility

- ✅ Python 3.x
- ✅ Windows
- ✅ Linux / Unix
- ❌ macOS (not fully tested, termios behavior may vary)

---

## 📖 License

This project is licensed under the **MIT License**.

---

## 🙏 A Final Note

> Please use responsibly.  
> Learning how these tools work helps us better understand **cybersecurity**, **ethical hacking**, and **digital forensics** — but using them **unethically** can lead to **criminal charges**.

---

**Author:** [Your Name]  
**Date:** 2025
