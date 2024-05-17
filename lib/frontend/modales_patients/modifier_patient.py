import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from tkinter import messagebox #géré message d'erreur
from lib.bdd_manager import BDDManager

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class ModaleModifierPatient(tk.Toplevel):
    def __init__(self, bdd_manager: BDDManager, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#9BBFDA")
        self.bdd_manager = bdd_manager
        self.resizable(False, False)
        self.title("Modifier Patient")
        self.grab_set()

        # Récupérer les informations du patient sélectionné
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

        # Labels et champs d'entrée pour le nom, le prénom et le numéro de téléphone
        self.label_nom = ttk.Label(self, text="Nom:", background="#9BBFDA")
        self.label_nom.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_nom = ttk.Entry(self)
        self.entry_nom.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_prenom = ttk.Label(self, text="Prénom:", background="#9BBFDA")
        self.label_prenom.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_prenom = ttk.Entry(self)
        self.entry_prenom.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_num_tel = ttk.Label(self, text="Numéro de téléphone:", background="#9BBFDA")
        self.label_num_tel.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_num_tel = ttk.Entry(self)
        self.entry_num_tel.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Ajout des boutons radio pour la civilité
        self.label_civilite = ttk.Label(self, text="Civilité:", background="#9BBFDA")
        self.label_civilite.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.civilite_value = tk.IntVar()
        self.radio_homme = ttk.Radiobutton(self, text="Homme", variable=self.civilite_value, value=1)
        self.radio_homme.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.radio_femme = ttk.Radiobutton(self, text="Femme", variable=self.civilite_value, value=2)
        self.radio_femme.grid(row=4, column=2, padx=10, pady=10, sticky="w")

        self.radio_non_binaire = ttk.Radiobutton(self, text="Non-binaire", variable=self.civilite_value, value=3)
        self.radio_non_binaire.grid(row=4, column=3, padx=10, pady=10, sticky="w")

        # Bouton pour enregistrer les modifications
        self.button_save = ttk.Button(
            self,
            text="Enregistrer les modifications",
            command=self.save_modifications
        )
        self.button_save.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    def update_patient_selected(self, patient_selected):
        patients = self.bdd_manager.get_all_patients()
        for patient in patients:
            if patient["nom"] == patient_selected:
                # Mettre à jour les champs avec les informations du patient sélectionné
                self.entry_nom.delete(0, tk.END)
                self.entry_nom.insert(0, patient["nom"])
                self.entry_prenom.delete(0, tk.END)
                self.entry_prenom.insert(0, patient["prenom"])
                self.entry_num_tel.delete(0, tk.END)
                self.entry_num_tel.insert(0, patient["num_tel"])
                # Mettre à jour les boutons radio en fonction de la civilité du patient
                self.civilite_value.set(patient["civilite"])
                self.selected_patient_id = patient["ref_patient"]

    def save_modifications(self):
        # Récupérer les valeurs entrées par l'utilisateur
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        num_tel = self.entry_num_tel.get()
        civilite = self.civilite_value.get()

        # Valider les valeurs
        if not all([nom, prenom, num_tel]):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        if not num_tel.isdigit() or len(num_tel) != 10:
            messagebox.showerror("Erreur",
                                 "Le numéro de téléphone doit contenir uniquement des chiffres et être de 10 chiffres.")
            return

        # Enregistrer les modifications dans la base de données
        self.bdd_manager.modifier_patient(nom, prenom, num_tel, civilite, self.selected_patient_id)

        self.destroy()