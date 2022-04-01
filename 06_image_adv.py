import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("1000x1000")
root.resizable(False, False)
root.title("Label Image")

image = Image.open("logo.jpg").resize((300, 300))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo, padding=5, compound = "right")
# compound = centre, right, top, bottom, left

# To change image
# label['image'] = photo

label.pack()

root.mainloop()
