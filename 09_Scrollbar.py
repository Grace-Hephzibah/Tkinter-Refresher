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

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

text = tk.Text(root, height = 8)
text.grid(row = 0, column = 0, sticky = "ew")
text.insert("1.0", "Hi there!")

text_scroll = ttk.Scrollbar(root, orient = "vertical", command = text.yview)
text_scroll.grid(row = 0, column = 1, sticky = "ns")
text["yscrollcommand"] = text_scroll.set

root.mainloop()