import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from lib.bdd_manager import BDDManager
from lib.frontend.utils import LabeledEntry
import tkinter.messagebox as mb  #géré message d'erreur


ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class ModaleNouveauMedecin(tk.Toplevel):
    def __init__(self, bdd_manager: BDDManager, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#9BBFDA")
        self.bdd_manager = bdd_manager
        self.resizable(False, False)
        self.title("Nouveaux Patient")
        self.grab_set()
        self.nom_patient = ""
        self.prenom_patient = ""
        self.tel_patient = ""

        self.entry_nom = LabeledEntry(self, label="Nom", style="Custom.TEntry")
        self.entry_nom.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_prenom = LabeledEntry(self, label="Prénom", style="Custom.TEntry")
        self.entry_prenom.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_tel = LabeledEntry(self, label="Téléphone", style="Custom.TEntry")
        self.entry_tel.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_spe = LabeledEntry(self, label="Spécialité", style="Custom.TEntry")
        self.entry_spe.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.button_stocker = ttk.Button(
            self,
            text="Valider",
            command=self.valider_donnees,
            style="Custom.TButton",
        )
        self.button_stocker.grid(row=6, column=1, padx=10, pady=10, sticky="we")

    def valider_donnees(self):
        nom_patient = self.entry_nom.get() if self.entry_nom.get() != self.entry_nom.label else ""
        prenom_patient = self.entry_prenom.get() if self.entry_prenom.get() != self.entry_prenom.label else ""
        tel_patient = self.entry_tel.get() if self.entry_tel.get() != self.entry_tel.label else ""
        spe_medecin = self.entry_spe.get() if self.entry_spe.get() != self.entry_spe.label else ""

        if len(nom_patient) == 0 or len(spe_medecin) == 0 or len(prenom_patient) == 0 or len(tel_patient) != 10:  # message d'erreur
            mb.showerror("Erreur de saisie", "Veuillez remplir correctement tous les champs correctement.")
            return

        print("Nom:", nom_patient)
        print("Prénom:", prenom_patient)
        print("Téléphone:", tel_patient)
        print("Spécialité:", spe_medecin)

        # ajouter RDV
        self.bdd_manager.ajout_medecin(nom_patient, prenom_patient, tel_patient, spe_medecin)