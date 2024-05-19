import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("grid tests")
        # for item in dir(self):
        #     print(item)
        # print(self.configure().keys())
        # set size
        # self.minsize(width=800, height=600)
        self.geometry("800x600")
        # disable resizing
        self.resizable(False, False)
        # main frame fill the space
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # self.config(width=800, height=600)
        # main frame
        # flat (default), raised, sunken, solid, ridge, or groove
        self.mainframe = ttk.Frame(self)
        # self.mainframe = ttk.Frame(self, borderwidth=10, relief="ridge")
        # self.mainframe = ttk.Frame(self, width=800, height=600)
        # self.mainframe = ttk.Frame(self, width=800, height=600, borderwidth=2, relief="raised")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        # create 4 subframes, each dividing screen in 4 parts
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.frame_1 = ttk.Frame(self.mainframe, borderwidth=2, relief="solid")
        self.frame_1.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame_2 = ttk.Frame(self.mainframe, borderwidth=2, relief="solid")
        self.frame_2.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame_3 = ttk.Frame(self.mainframe, borderwidth=2, relief="solid")
        self.frame_3.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame_4 = ttk.Frame(self.mainframe, borderwidth=2, relief="solid")
        self.frame_4.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        # set style
        # style = ttk.Style()
        # print(style.theme_names())
        # print(style.theme_use())
        # print(self.mainframe.winfo_class())
        # print(self.mainframe["style"])
        # 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'
        # style.theme_use("xpnative")
        # add 2 buttons to the same grid place in a frame -> doesn't work
        # self.frame_1.columnconfigure(0, weight=1)
        # self.frame_1.rowconfigure(0, weight=1)
        # self.button_test_1 = ttk.Button(self.frame_1, text="test 1")
        # self.button_test_1.grid(column=0, row=0, sticky=(tk.N, tk.W))
        # self.button_test_2 = ttk.Button(self.frame_1, text="test 2")
        # self.button_test_1.grid(column=0, row=0, sticky=(tk.E, tk.S))
        # run app
        self.mainloop()


if __name__ == "__main__":
    Application()

    ###

    # root = tk.Tk()

    # content = ttk.Frame(root)
    # frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
    # namelbl = ttk.Label(content, text="Name")
    # name = ttk.Entry(content)

    # onevar = tk.BooleanVar(value=True)
    # twovar = tk.BooleanVar(value=False)
    # threevar = tk.BooleanVar(value=True)

    # one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
    # two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
    # three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
    # ok = ttk.Button(content, text="Okay")
    # cancel = ttk.Button(content, text="Cancel")

    # content.grid(column=0, row=0)
    # frame.grid(column=0, row=0, columnspan=3, rowspan=2)
    # namelbl.grid(column=3, row=0, columnspan=2)
    # name.grid(column=3, row=1, columnspan=2)
    # one.grid(column=0, row=3)
    # two.grid(column=1, row=3)
    # three.grid(column=2, row=3)
    # ok.grid(column=3, row=3)
    # cancel.grid(column=4, row=3)

    # root.mainloop()
