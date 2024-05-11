import tkinter as tk
from tkinter import ttk


class EtatDeConsultation(tk.Toplevel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#CCE2F3")
        self.resizable(False, False)
        self.title("État des consultations")

        # Label "État des consultations"
        self.label_title = ttk.Label(self, text="État des consultations", font=("Helvetica", 14, "bold"),
                                     background="#CCE2F3")
        self.label_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.button_close = ttk.Button(
            self,
            text="❌",   # Bouton "Fermer"
            command=self.destroy
        )
        self.button_close.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.canvas = tk.Canvas(self, bg="#CCE2F3", highlightthickness=0)
        self.canvas.create_line(0, 10, 1800, 10, fill="#000000")        # Ligne horizontale
        self.canvas.grid(row=1, columnspan=2, sticky="ew")

        self.grab_set()


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config(width=800, height=600)
        self.title("Fenêtre principale")
        self.button_open = ttk.Button(
            self,
            text="Consulter l'état",
            command=self.open_secondary_window
        )
        self.button_open.place(x=50, y=50)

    def open_secondary_window(self):
        self.secondary_window = EtatDeConsultation()


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
