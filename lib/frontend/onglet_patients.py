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

        self.patients = self.bdd_manager.get_all_patients()
        self.patient_names = [patient["nom"] for patient in self.patients]
        self.patient_ids = [patient["ref_patient"] for patient in self.patients]

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

        self.label_civilite = ttk.Label(self, text="Civilité:")
        self.label_civilite.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.label_num_tel = ttk.Label(self, text="Numéro de téléphone:")
        self.label_num_tel.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.label_nom_patient = ttk.Label(self)
        self.label_nom_patient.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_prenom_patient = ttk.Label(self)
        self.label_prenom_patient.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_civilite_patient = ttk.Label(self)
        self.label_civilite_patient.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.label_num_tel_patient = ttk.Label(self)
        self.label_num_tel_patient.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.button_modif_patient = ttk.Button(
            self,
            text="Modifier patient",
            command=self.open_modif_patient
        )
        self.button_modif_patient.grid(row=8, column=0, padx=10, pady=10, sticky="w")

        self.button_suppr_patient = ttk.Button(
            self,
            text="Supprimer patient",
            command=self.supprimer_patient
        )
        self.button_suppr_patient.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    def update_patient_selected(self, patient_selected):
        for patient in self.patients:
            if patient["nom"] == patient_selected:
                self.label_nom_patient.config(text=patient["nom"])
                self.label_prenom_patient.config(text=patient["prenom"])
                # Affichage de la civilité en fonction de la valeur stockée dans la base de données
                if patient["civilite"] == 0:
                    self.label_civilite_patient.config(text="Monsieur")
                elif patient["civilite"] == 1:
                    self.label_civilite_patient.config(text="Madame")
                else:
                    self.label_civilite_patient.config(text="Non-binaire")
                self.label_num_tel_patient.config(text=patient["num_tel"])
                self.selected_patient_id = patient["ref_patient"]
                break

    def open_modif_patient(self):
        ModaleModifierPatient(self.bdd_manager)

    def supprimer_patient(self):
        # Supprimer le patient sélectionné dans la base de données
        if hasattr(self, 'selected_patient_id'):
            self.bdd_manager.supprimer_patient(self.selected_patient_id)

            # Mettre à jour la liste des patients et l'interface
            self.patients = self.bdd_manager.get_all_patients()
            self.patient_names = [patient["nom"] for patient in self.patients]
            self.patient_dropdown["menu"].delete(0, "end")
            for patient_name in self.patient_names:
                self.patient_dropdown["menu"].add_command(
                    label=patient_name,
                    command=lambda value=patient_name: self.selected_patient.set(value)
                )

            # Réinitialiser les labels
            self.label_nom_patient.config(text="")
            self.label_prenom_patient.config(text="")
            self.label_civilite_patient.config(text="")
            self.label_num_tel_patient.config(text="")
            self.selected_patient.set("Sélectionnez un patient")

