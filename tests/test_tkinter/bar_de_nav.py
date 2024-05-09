import tkinter as tk
from tkinter import ttk


def create_button(parent, text, command):
    button = ttk.Button(parent, text=text, command=command)
    return button


class Application(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("400x300")

        # Création de la barre de navigation
        self.nav_bar = ttk.Frame(self)
        self.nav_bar.pack(side="top", fill="x")

        # Création des boutons de navigation
        self.button1 = create_button(self.nav_bar, "Page 1", self.open_page1)
        self.button1.pack(side="left", padx=10, pady=5)

        self.button2 = create_button(self.nav_bar, "Page 2", self.open_page2)
        self.button2.pack(side="left", padx=10, pady=5)

        self.button3 = create_button(self.nav_bar, "Page 3", self.open_page3)
        self.button3.pack(side="left", padx=10, pady=5)

    def open_page1(self):
        # Affichage de la page 1
        self.clear_content()
        label = ttk.Label(self, text="Contenu de la page 1")
        label.pack()

    def open_page2(self):
        # Affichage de la page 2
        self.clear_content()
        label = ttk.Label(self, text="Contenu de la page 2")
        label.pack()

    def open_page3(self):
        # Affichage de la page 3
        self.clear_content()
        label = ttk.Label(self, text="Contenu de la page 3")
        label.pack()

    def clear_content(self):
        # Effacement du contenu précédent
        for widget in self.winfo_children():
            if widget != self.nav_bar:
                widget.destroy()


if __name__ == "__main__":
    app = Application("Ma fenêtre avec barre de navigation")
    app.mainloop()
