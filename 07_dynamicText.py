import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore. SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("600x200")
root.resizable(False, False)
root.title("Dynamic Label")

greet = tk.StringVar()

label = ttk.Label(root, textvariable = greet, padding = 20)
greet.set("This text is to greet you!")
label.config(font = ("Segoe UI", 20))
label.pack()

root.mainloop()
