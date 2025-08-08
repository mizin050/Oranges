import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import random
import pyperclip
from chatbot import ask_pet
from voice_listen import listen_background

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class DesktopAssistant:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.geometry("300x300+100+100")
        self.root.wm_attributes('-transparentcolor', 'black')
        self.last_response = None
        self.pet_talking_enabled = True

        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='black', highlightthickness=0)
        self.canvas.pack()

        self.animations = self.load_animations()
        self.sprite = self.animations.get("idle_default", [])[0:1]
        self.sprite_index = 0
        self.sprite_img = self.canvas.create_image(150, 150, image=self.sprite[self.sprite_index])

        self.animate()
        self.root.after(25000, self.switch_idle_randomly)

    def animate(self):
        if not self.sprite:
            return
        self.sprite_index = (self.sprite_index + 1) % len(self.sprite)
        self.canvas.itemconfig(self.sprite_img, image=self.sprite[self.sprite_index])
        self.root.after(100, self.animate)

    def switch_idle_randomly(self):
        if random.random() < 0.85 or not self.animations["idle_alts"]:
            self.sprite = self.animations["idle_default"]
        else:
            self.sprite = random.choice(self.animations["idle_alts"])
        self.sprite_index = 0
        self.root.after(25000, self.switch_idle_randomly)

    def load_animations(self):
        animations = {}

        def load_frames(folder):
            path = resource_path(folder)
            frames = []
            if not os.path.exists(path): return frames
            for file in sorted(os.listdir(path)):
                if file.lower().endswith(('.png', '.gif')):
                    full_path = os.path.join(path, file)
                    img = Image.open(full_path).convert("RGBA")
                    img = img.resize((105, 105), Image.NEAREST)
                    frames.append(ImageTk.PhotoImage(img))
            return frames

        animations["idle_default"] = load_frames("assets/defaultIdle")
        animations["idle_alts"] = []

        for i in range(1, 9):
            alt_path = f"assets/idle{i}"
            if os.path.isdir(resource_path(alt_path)):
                frames = load_frames(alt_path)
                if frames:
                    animations["idle_alts"].append(frames)

        return animations
    
    def show_text_bubble(self, message):
        bubble = tk.Toplevel(self.root)
        bubble.overrideredirect(True)
        x = self.root.winfo_rootx() + 160
        y = self.root.winfo_rooty() + 40
        bubble.geometry(f"+{x}+{y}")

        label = tk.Label(
            bubble,
            text=message,
            bg="white",
            fg="black",
            font=("Arial", 10),
            wraplength=200,
            relief="solid",
            borderwidth=1,
            padx=6,
            pady=4
        )
        label.pack()
        bubble.lift()
        bubble.attributes("-topmost", True)
        bubble.after(5000, bubble.destroy)

    def handle_voice_input(self, text):
        text = text.lower().strip()
        print("You said:", text)

        if "answer this" in text or "what's on clipboard" in text:
            clipboard_text = pyperclip.paste().strip()

            if clipboard_text:
                self.show_text_bubble("Reading clipboard... *meow*")
                try:
                    response = ask_pet(clipboard_text)
                    self.last_response = response
                    self.show_text_bubble(response)
                except Exception as e:
                    if "503" in str(e):
                        self.show_text_bubble("*yawn* The server is taking a catnap right now. Try again in a minute.")
                    else:
                        self.show_text_bubble("*hiss* Something went wrong with my brain. Try again?")
            else:
                self.show_text_bubble("Clipboard is empty. What am I supposed to read? *tail flick*")
            return

        if "copy that" in text or "copy last response" in text:
            if self.last_response:
                pyperclip.copy(self.last_response)
                self.show_text_bubble("Copied it. Happy now?")
            else:
                self.show_text_bubble("Nothing to copy, genius.")
            return

        if "lock computer" in text or "lock screen" in text:
            self.show_text_bubble("Locking your computer 🔒")
            self.lock_computer()
            return

        if "kill yourself" in text or "go to sleep" in text or "exit pet" in text:
            self.show_text_bubble("Goodbye! 👋")
            self.shutdown_pet()
            return

        if "stop talking" in text:
            self.pet_talking_enabled = False
            self.show_text_bubble("Okay, I'll stay quiet.")
            return

        if "start talking" in text:
            self.pet_talking_enabled = True
            self.show_text_bubble("I'm back! Missed me?")
            return

        if self.pet_talking_enabled:
            self.show_text_bubble(f"You: {text}", user=True)
            try:
                response = ask_pet(text)
                self.last_response = response
                self.show_text_bubble(response)
            except Exception as e:
                if "503" in str(e):
                    self.show_text_bubble("*yawn* The server is taking a catnap right now. Try again in a minute.")
                else:
                    self.show_text_bubble("*hiss* Something went wrong with my brain. Try again?")
        else:
            print("Pet is muted — no response.")

    def lock_computer(self):
        if sys.platform == 'win32':
            os.system('rundll32.exe user32.dll,LockWorkStation')
        # Add support for other platforms if needed

    def shutdown_pet(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    assistant = DesktopAssistant(root)

    # Start voice listener in background
    listen_background(callback=assistant.handle_voice_input)

    assistant.show_text_bubble("Hey! I'm listening 👂")
    root.mainloop()
