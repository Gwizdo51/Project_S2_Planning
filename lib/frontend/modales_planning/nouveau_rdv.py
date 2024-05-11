import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from lib.frontend.modales_planning.nouveau_patient import ModaleNouveauPatient

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class ModaleNouveauRDV(tk.Toplevel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#9BBFDA")
        self.resizable(False, False)
        self.title("Nouveaux Rendez-vous")
        self.grab_set()

        self.button_close = ttk.Button(
            self,
            text="❌",  # Bouton "Fermer"
            command=self.destroy,
            width=3
        )
        self.button_close.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        self.button_new_patient = ttk.Button(
            self,
            text="Nouveau patient",
            command=self.open_nouveau_patient
        )
        self.button_new_patient.grid(row=1, column=1, padx=10, pady=10, sticky="e")

    def open_nouveau_patient(self):
        self.secondary_window = ModaleNouveauPatient()
