import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.bdd_manager import BDDManager


class ModaleEtatConsultations(tk.Toplevel):

    def __init__(self, bdd_manager: BDDManager, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#CCE2F3")
        self.bdd_manager = bdd_manager
        self.resizable(False, False)
        self.title("État des consultations")
        self.grab_set()
        self.focus()
        self.label_title = ttk.Label(self, text="État des consultations", font=("Helvetica", 14, "bold"),
                                     background="#CCE2F3")
        self.label_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.button_close = ttk.Button(
            self,
            text="❌",  # Bouton "Fermer"
            command=self.destroy,
            width=3
        )
        self.button_close.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.canvas = tk.Canvas(self, bg="#CCE2F3", highlightthickness=0)
        self.canvas.create_line(0, 10, 1800, 10, fill="#000000")  # Ligne horizontale
        self.canvas.grid(row=1, columnspan=2, sticky="ew")
