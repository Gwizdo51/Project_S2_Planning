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

        patients = self.bdd_manager.get_all_patients()
        self.patient_names = [patient["nom"] for patient in patients]
        self.patient_ids = [patient["ref_patient"] for patient in patients]

        self.selected_patient = tk.StringVar(self)
        self.selected_patient.set("Sélectionnez un patient")
        self.patient_dropdown = ttk.OptionMenu(
            self,
            self.selected_patient,
            self.selected_patient.get(),
            *self.patient_names,
            command=self.update_patient_selected
        )
        self.patient_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.label_nom = ttk.Label(self, text="Nom:")
        self.label_nom.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_prenom = ttk.Label(self, text="Prénom:")
        self.label_prenom.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.label_num_tel = ttk.Label(self, text="Numéro de téléphone:")
        self.label_num_tel.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.label_nom_patient = ttk.Label(self)
        self.label_nom_patient.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_prenom_patient = ttk.Label(self)
        self.label_prenom_patient.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_num_tel_patient = ttk.Label(self)
        self.label_num_tel_patient.grid(row=4, column=1, padx=10, pady=10, sticky="w")


        self.button_modif_patient = ttk.Button(
            self,
            text="Modifier patient",
            command=self.open_modif_patient
        )
        self.button_modif_patient.grid(row=8, column=9, padx=10, pady=10, sticky="w")

    def update_patient_selected(self, patient_selected):
        patients = self.bdd_manager.get_all_patients()
        for patient in patients:
            if patient["nom"] == patient_selected:
                self.label_nom_patient.config(text=patient["nom"])
                self.label_prenom_patient.config(text=patient["prenom"])
                self.label_num_tel_patient.config(text=patient["num_tel"])
                break

    def open_modif_patient(self):
        ModaleModifierPatient(self.bdd_manager)
