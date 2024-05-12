import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from lib.frontend.modales_planning.nouveau_patient import ModaleNouveauPatient

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.bdd_manager import BDDManager

class ModaleNouveauRDV(tk.Toplevel):
    def __init__(self, bdd_manager: BDDManager, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#9BBFDA")
        self.bdd_manager = bdd_manager
        self.resizable(False, False)
        self.title("Nouveaux Rendez-vous")
        self.grab_set()

        patients = self.bdd_manager.get_all_patients()
        patient_names = [patient["nom"] + " " + patient["prenom"] for patient in patients]


        self.selected_patient = tk.StringVar(self) #Créer un menu déroulant
        self.selected_patient.set("Sélectionnez un patient")
        self.patient_dropdown = ttk.OptionMenu(self, self.selected_patient, *patient_names)
        self.patient_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.button_new_patient = ttk.Button(
            self,
            text="Nouveau patient",
            command=self.open_nouveau_patient
        )
        self.button_new_patient.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    def open_nouveau_patient(self):
        self.secondary_window = ModaleNouveauPatient()



    # def get_all_patient_names(self):
    #     return self.bdd_manager.get_all_patient_names()
