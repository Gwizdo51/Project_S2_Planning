import tkinter as tk
from tkinter import ttk


# https://python-forum.io/thread-40930.html
# https://pythonassets.com/posts/create-a-new-window-in-tk-tkinter/
class SecondaryWindow(tk.Toplevel):

    def __init__(self, callback=None, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
        self.config(width=300, height=90)
        self.resizable(False, False)
        self.title("Enter your name")
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=20, y=20, width=260)
        self.button_close = ttk.Button(
            self,
            text="Done!",
            command=self.button_close_click
        )
        self.button_close.place(x=20, y=50, width=260)
        # self.focus()
        self.entry_name.focus()
        self.grab_set()

    def button_close_click(self):
        if self.callback:
            self.callback(self.entry_name.get())
        self.destroy()


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config(width=400, height=300)
        self.title("Main Window")
        self.button_open = ttk.Button(
            self,
            text="Request name",
            command=self.open_secondary_window
        )
        self.button_open.place(x=50, y=50)
        self.label_name = ttk.Label(self, text="no name entered yet")
        self.label_name.place(x=50, y=150)

    def open_secondary_window(self):
        self.secondary_window = SecondaryWindow(callback=self.enter_name)

    def enter_name(self, name):
        self.label_name["text"] = f"Your name is: {name}"


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
