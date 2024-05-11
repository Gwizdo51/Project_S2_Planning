import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.bdd_manager import BDDManager
from lib.frontend.modales_patients.modifier_patient import ModaleModifierPatient


class OngletPatients(ttk.Frame):

    def __init__(self, master, bdd_manager: BDDManager):
        super().__init__(master, borderwidth=10, relief="solid")
        self.bdd_manager = bdd_manager
        self.content = ttk.Label(self, text="Contenu de l'onglet Patients")
        self.content.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
