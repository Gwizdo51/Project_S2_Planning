import tkinter as tk

def creer_menu_deroulant(parent, options):
    variable = tk.StringVar(parent)
    variable.set(options[0])

    opt = tk.OptionMenu(parent, variable, *options)
    opt.pack()

options = ["test", "test2", "test3", "test4"]


app = tk.Tk()
app.title("Ma page")
frame = tk.Frame(app)
frame.pack()

creer_menu_deroulant(frame, options)

app.mainloop()
