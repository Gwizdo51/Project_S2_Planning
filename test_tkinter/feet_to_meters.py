import tkinter as tk
from tkinter import ttk


def is_float(something: str):
    try:
        float(something)
        result = True
    except:
        result = False
    return result

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
        # if the color of the text is gray (the label), delete it and write in black
        if str(self.cget("foreground")) == "gray":
            # print("default text detected")
            self.delete(0, "end")
            # self.insert(0, "")
            self.config(foreground="black")

    def on_unfocus(self, event):
        # if the field is empty, fill with label in gray
        if not self.get():
            self.insert(0, self.label)
            self.config(foreground="gray")


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Feet to meters converter")
        # handle resizing
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # main frame
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(2, weight=1)
        # variables
        self.feet = tk.StringVar()
        self.meters = tk.StringVar()
        # text entry
        # self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)
        self.feet_entry = LabeledEntry(self.mainframe, label="value", width=7, textvariable=self.feet)
        # self.feet_entry.config(foreground="gray")
        self.feet_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
        # "calculate" button
        self.calculate_button = ttk.Button(self.mainframe, text="Calculate", command=self.calculate)
        # print(self.calculate_button.configure())
        self.calculate_button.grid(column=2, row=2, sticky=tk.W)
        # https://stackoverflow.com/questions/53580507/disable-enable-button-in-tkinter
        # "state" = "normal" or "disabled"
        # print(self.calculate_button["state"])
        # self.calculate_button["state"] = "disabled"
        # labels
        self.meters_label = ttk.Label(self.mainframe, textvariable=self.meters)
        self.meters_label.grid(column=1, row=1, sticky=(tk.W, tk.E))
        self.static_labels = {}
        self.static_labels["label_0"] = ttk.Label(self.mainframe, text="feet")
        self.static_labels["label_0"].grid(column=2, row=0, sticky=tk.W)
        self.static_labels["label_1"] = ttk.Label(self.mainframe, text="is equivalent to")
        self.static_labels["label_1"].grid(column=0, row=1, sticky=tk.E)
        self.static_labels["label_2"] = ttk.Label(self.mainframe, text="meters")
        self.static_labels["label_2"].grid(column=2, row=1, sticky=tk.W)
        # grid config
        for child in self.mainframe.winfo_children():
            # print(child)
            # print(type(child))
            # print(child == self.static_labels["label_2"])
            child.grid_configure(padx=5, pady=5)
            # pass
        # keyboard focus on text entry
        # self.feet_entry.focus()
        # bind "enter" key to self.calculate
        self.bind("<Return>", self.calculate)
        # run app
        self.mainloop()

    def calculate(self, *args):
        # print(repr(self.feet.get()))
        value = self.feet.get().replace(",", ".")
        if is_float(value):
            # print("ok")
            value = float(value)
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        else:
            # print("not ok")
            self.meters.set("")


if __name__ == "__main__":
    Application()
    # app.mainloop()
    # print(dir(app))
    # app.row
