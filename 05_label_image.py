import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("950x650")
root.resizable(False, False)
root.title("Label Image")

image = Image.open("logo.jpg")
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo, padding=5)
label.pack()

root.mainloop()
