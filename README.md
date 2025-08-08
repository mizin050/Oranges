<img width="3188" height="1202" alt="image" src="https://github.com/user-attachments/assets/7ae8f260-d450-4a13-b078-23f995230e91" />

﻿# Oranges - The Desktop Pet 🐱

## Basic Details

### Team Name: Whiskerious

### Team Members
- Team Lead: Mizin Sadikh - Muthoot Institute of Technology and Science
- Member : Mirza Talha Baig - Muthoot Institute of Technology and Science


### Project Description

A charming desktop pet that provides delightful company during your computer sessions. It's a completely unnecessary but adorable addition to your desktop experience.

### The Problem (that doesn't exist)

Let’s be honest, working at your computer can get boring. Sure, you could play music or talk to friends, but where’s the fun in that when you could have a tiny cat hovering on your screen, silently judging your life choices?

### The Solution (that nobody asked for)

So, we built Oranges a snarky little desktop cat that chats with you, reacts to your voice, steals a peek at your clipboard, and throws in a meow or two just to keep you humble.


## Technical Detail
- **Voice Commands** — Talk to your pet and get begrudgingly useful answers.
- **Groq AI Brain** — Powered by LLaMA 3 (`llama3-70b-8192`) for witty, concise responses.
- **Clipboard Reading** — “Answer this” will make it read & reply to your clipboard text.
- **Copy Last Reply** — “Copy that” saves the last sarcastic gem to your clipboard.
- **Computer Locking** — “Lock screen” for instant privacy.
- **Pet Control** — Tell it to “stop talking” or “start talking” as you wish.
- **Animated Sprites** — Cute (and judgmental) idle animations from `assets/`.

### Technologies/Components Used

For Software:

- Python 3.13
- Tkinter (GUI Framework)
- PIL/Pillow (Image Processing)
- PyInstaller (Executable Creation)
- Auto-py-to-exe (Alternative Build Tool)

### Implementation

For Software:
```
# Installation

````bash
# Clone the repository
git clone https://github.com/mizin050/Oranges.git

# Install required packages
pip install -r requirements.txt

# Run

```bash
python main.py
or
Download and run the .exe file
```
### Project Documentation

For Software:

# Screenshots

![alive](first.png)
_existing_

![talking](second.png)
_talking back_

![Default Idle](<assets/defaultIdle/frame(1).png>)
_Oranges in their default idle animation_

### Project Demo

# Video

-[Video Link](https://drive.google.com/file/d/1scU8ZiQAsOZyeKiw_YF2UwJlVDt_jl_W/view?usp=sharing)

# Additional Demos

## 🎙️ Voice Commands & Features
- **`answer this`** / **`what's on clipboard`**  
  Reads the text from your clipboard and responds to it using the AI pet.
- **`copy that`** / **`copy last response`**  
  Copies the pet’s last response to your clipboard.
- **`lock computer`** / **`lock screen`**  
  Locks your computer (Windows supported).
- **`kill yourself`** / **`go to sleep`** / **`exit pet`**  
  Shuts down the desktop pet completely.
- **`stop talking`**  
  Mutes the pet — it will not respond to your voice commands until re-enabled.
- **`start talking`**  
  Unmutes the pet — it resumes responding to voice commands.
- **General speech** (anything else you say)  
  If the pet is not muted, it replies in its sarcastic cat tone.


## Team Contributions
Mizin Sadikh : Cat Brain & Voice
- Integrated Groq API with LLaMA 3 model for sarcastic, short responses
- Wrote chatbot.py logic to handle prompts and responses
- Designed system prompt to give the cat its personality
- Implemented voice recognition with SpeechRecognition.
- Added voice command handling for clipboard reading, copying, locking screen, and muting/unmuting.

Mirza Talha Baig : Cat Body & UI
- Built Tkinter-based floating, transparent, always-on-top pet window
- Added sprite animation system with idle/default and alternate animations
- Implemented speech bubble UI for showing messages
- Managed image loading, resizing, and asset handling from assets/
- Developed random idle animation switching logic

---

Made with ❤️ at TinkerHub Useless Projects

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)
````













