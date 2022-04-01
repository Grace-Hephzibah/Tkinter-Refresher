import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore. SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Tkinter Template")

text = tk.Text(root, height = 8)
text.insert(1.0, "Why is this disabled XD")

text.pack()

root.mainloop()