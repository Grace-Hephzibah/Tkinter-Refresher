import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore. SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("400x400")
root.resizable(False, False)
root.title("Label")

label = ttk.Label(root, text = "Hello", padding = 20)
label.config(font = ("Segoe UI", 20))
label.pack()

root.mainloop()
