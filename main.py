import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class DesktopPet:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.geometry("300x300+-80+100")
        self.root.wm_attributes('-transparentcolor', 'black')

        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='black', highlightthickness=0)
        self.canvas.pack()

        self.sprite = self.load_animation("assets/defaultIdle")
        self.sprite_index = 0
        self.sprite_img = self.canvas.create_image(150, 150, image=self.sprite[self.sprite_index])

        self.animate()

    def load_animation(self, folder):
        frames = []
        folder_path = resource_path(folder)
        if os.path.exists(folder_path):
            for file in sorted(os.listdir(folder_path)):
                if file.endswith((".png", ".gif")):
                    path = os.path.join(folder_path, file)
                    img = Image.open(path).resize((105, 105))
                    frames.append(ImageTk.PhotoImage(img))
        return frames

    def animate(self):
        if self.sprite:
            self.sprite_index = (self.sprite_index + 1) % len(self.sprite)
            self.canvas.itemconfig(self.sprite_img, image=self.sprite[self.sprite_index])
        self.root.after(100, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopPet(root)
    root.mainloop()
