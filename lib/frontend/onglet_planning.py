import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.bdd_manager import BDDManager
from lib.frontend.modales_planning.resume_rdv import ModaleResumeRDV
from lib.frontend.modales_planning.modifier_rdv import ModaleModifierRDV
from lib.frontend.modales_planning.nouveau_rdv import ModaleNouveauRDV
from lib.frontend.modales_planning.nouveau_patient import ModaleNouveauPatient
from lib.frontend.modales_planning.etat_consultations import ModaleEtatConsultations
from lib.frontend.modales_planning.modifier_horaires import ModaleModifierHoraires


class OngletPlanning(ttk.Frame):

    def __init__(self, master, bdd_manager: BDDManager):
        super().__init__(master, borderwidth=10, relief="solid" )
        self.bdd_manager = bdd_manager
        self.content = ttk.Label(self, text="Contenu de l'onglet Planning")
        self.content.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.button_open = tk.Button(
            self,
            text="état de consultation",
            command=self.open_etat_consultation,
            font=("Arial", 12), background="#305F82", bd=0, relief="flat", width=16, height=2
        )
        self.button_open.place(x=30, y=250)

        self.button_nouveau_rdv = tk.Button(
            self,
            text="Nouveaux RDV",
            command=self.open_nouveau_rdv,
            font=("Arial", 12), background="#305F82", bd=0, relief="flat", width=16, height=2
        )
        self.button_nouveau_rdv.place(x=30, y=150)


    def open_etat_consultation(self):
        self.secondary_window = ModaleEtatConsultations()

    def open_nouveau_rdv(self):
        self.secondary_window = ModaleNouveauRDV()