import tkinter as tk
from tkinter import ttk


# https://python-forum.io/thread-40930.html
# https://pythonassets.com/posts/create-a-new-window-in-tk-tkinter/
class SecondaryWindow(tk.Toplevel):

    def __init__(self, callback=None, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
        # self.config(width=560, height=500)
        self.geometry("500x500")
        # disable resizing
        self.resizable(False, False)
        self.title("Enter your name")
        self.entry_name = ttk.Entry(self)
        # self.entry_name.place(x=20, y=20, width=260)
        self.entry_name.grid(column=0, row=0, sticky=(tk.E, tk.W))
        self.button_new_window = ttk.Button(
            self,
            text="New window",
            command=self.button_new_window_click
        )
        self.button_new_window.grid(column=0, row=1, sticky=(tk.E, tk.W))
        self.button_close = ttk.Button(
            self,
            text="Done!",
            command=self.button_close_click
        )
        # self.button_close.place(x=20, y=50, width=260)
        self.button_close.grid(column=0, row=2, sticky=(tk.E, tk.W, tk.N))
        # make content fill space
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        # self.focus()
        self.entry_name.focus()
        self.grab_set()

    def button_close_click(self):
        if self.callback:
            self.callback(self.entry_name.get())
        self.destroy()

    def button_new_window_click(self):
        TertiaryWindow()


class TertiaryWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()
        # disable resizing
        self.resizable(False, False)
        self.title("KEKW")
        self.button_close = ttk.Button(
            self,
            text="Done!",
            command=self.button_close_click
        )
        self.button_close.grid(column=0, row=0, padx=10, pady=10)
        self.focus()
        self.grab_set()

    def button_close_click(self):
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
        # self.secondary_window = SecondaryWindow(callback=self.enter_name)
        SecondaryWindow(callback=self.enter_name)

    def enter_name(self, name):
        self.label_name["text"] = f"Your name is: {name}"


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
