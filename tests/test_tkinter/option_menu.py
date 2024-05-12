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
        # options menu
        self.options = ["option 1", "option 2", "option 3"]
        self.selected_option = tk.StringVar()
        self.options_menu = ttk.OptionMenu(self.mainframe, self.selected_option, self.options[0], *self.options, command=self.update_selected_option)
        # print(self.selected_option.get())
        self.options_menu.grid(column=0, row=0)
        # run app
        self.mainloop()

    def update_selected_option(self, selected_option):
        print(self.selected_option.get())
        print(selected_option)


if __name__ == "__main__":
    Application()
