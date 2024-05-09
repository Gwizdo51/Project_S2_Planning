import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        # disable resizing
        self.resizable(False, False)
        # window title
        self.title("Test command on radio button selection")
        # main frame
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        # radio button associated variable
        self.radio_var = tk.StringVar(value="0")
        # radio buttons
        self.radio_button_option_0 = ttk.Radiobutton(self.mainframe, text="option 0", variable=self.radio_var, value="0", command=self.check_var_value)
        self.radio_button_option_1 = ttk.Radiobutton(self.mainframe, text="option 1", variable=self.radio_var, value="1", command=self.check_var_value)
        self.radio_button_option_2 = ttk.Radiobutton(self.mainframe, text="option 2", variable=self.radio_var, value="2", command=self.check_var_value)
        self.radio_button_option_0.grid(column=0, row=0)
        self.radio_button_option_1.grid(column=0, row=1)
        self.radio_button_option_2.grid(column=0, row=2)
        # check self.radio_var button
        self.check_button = ttk.Button(self.mainframe, text="check", command=self.check_var_value)
        self.check_button.grid(column=0, row=3)
        # run app
        self.mainloop()

    def check_var_value(self):
        print("self.radio_var = '" + self.radio_var.get() + "'")


if __name__ == "__main__":
    Application()
