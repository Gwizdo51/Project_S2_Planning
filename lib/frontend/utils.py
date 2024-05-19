import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


# https://www.reddit.com/r/learnpython/comments/6tw5ve/tkinter_entry_box_how_to_declare_a_light_grey/
class LabeledEntry(ttk.Entry):

    def __init__(self, master=None, label="", **kwargs):
        super().__init__(master=master, **kwargs)
        self.label = label
        self.insert(0, self.label)
        self.config(foreground="gray")
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.on_unfocus)

    def on_focus(self, event):
        # print("focused")
        # text_color = self.cget("foreground")
        # print(repr(text_color))
        # if the color of the text is gray (the label), delete it and write the input in black
        if str(self.cget("foreground")) == "gray":
            # print("default text detected")
            self.delete(0, tk.END)
            # self.insert(0, "")
            self.config(foreground="black")

    def on_unfocus(self, event):
        # if the field is empty, fill with label in gray
        if not self.get():
            self.insert(0, self.label)
            self.config(foreground="gray")


def configure_styles():
    style = ttk.Style()
    style.configure("Custom.TEntry", background="blue", padding=[20, 10, 20, 10], font=("Arial", 12))
    style.configure("Custom.TButton",
                    foreground="black",
                    background="blue",
                    font=("Inter", 12),
                    padding=[10, 10, 10, 10],
                    justify="center")
    style.configure("Multiline.TButton", justify="center")
    style.configure("Multiline.TRadiobutton", justify="center")
