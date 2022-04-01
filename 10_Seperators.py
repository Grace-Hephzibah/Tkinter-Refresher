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

ttk.Label(root, orient = "horizontal").pack()
ttk.Label(root, orient = "horizontal").pack(fill = "x")

root.mainloop()