import tkinter as tk
from tkinter import ttk

def create_radio_button(parent, text, variable, value, command=None):
    button = ttk.Radiobutton(parent, text=text, variable=variable, value=value, command=command)
    return button

def option_selectionné():
    print("Option sélectionnée :", choix_var.get())

root = tk.Tk()
choix_var = tk.StringVar()

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
for option in options:
    create_radio_button(root, option, choix_var, option, command=option_selectionné).pack()

root.mainloop()
