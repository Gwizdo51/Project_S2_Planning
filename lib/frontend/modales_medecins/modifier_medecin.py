import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from lib.bdd_manager import BDDManager
from tkinter import messagebox #géré message d'erreur

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class ModaleModifierMedecin(tk.Toplevel):
    def __init__(self, bdd_manager: BDDManager, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#9BBFDA")
        self.bdd_manager = bdd_manager
        self.resizable(False, False)
        self.title("Modifier Médecin")
        self.grab_set()

        medecins = self.bdd_manager.get_all_medecins()
        self.medecin_names = [medecin["nom"] for medecin in medecins]
        self.medecin_ids = [medecin["ref_medecin"] for medecin in medecins]

        self.selected_medecin = tk.StringVar(self)
        self.selected_medecin.set("Sélectionnez un médecin")
        self.medecin_dropdown = ttk.OptionMenu(
            self,
            self.selected_medecin,
            self.selected_medecin.get(),
            *self.medecin_names,
            command=self.update_medecin_selected
        )
        self.medecin_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.label_nom = ttk.Label(self, text="Nom:", background="#9BBFDA")
        self.label_nom.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_prenom = ttk.Label(self, text="Prénom:", background="#9BBFDA")
        self.label_prenom.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.label_specialite = ttk.Label(self, text="Spécialité:", background="#9BBFDA")
        self.label_specialite.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.label_num_tel = ttk.Label(self, text="Numéro de téléphone:", background="#9BBFDA")
        self.label_num_tel.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.entry_nom = ttk.Entry(self)
        self.entry_nom.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.entry_prenom = ttk.Entry(self)
        self.entry_prenom.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.entry_specialite = ttk.Entry(self)
        self.entry_specialite.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.entry_num_tel = ttk.Entry(self)
        self.entry_num_tel.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.button_save = ttk.Button(
            self,
            text="Enregistrer les modifications",
            command=self.save_modifications
        )
        self.button_save.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    def update_medecin_selected(self, medecin_selected):
        medecins = self.bdd_manager.get_all_medecins()
        for medecin in medecins:
            if medecin["nom"] == medecin_selected:
                self.entry_nom.delete(0, tk.END)
                self.entry_nom.insert(0, medecin["nom"])
                self.entry_prenom.delete(0, tk.END)
                self.entry_prenom.insert(0, medecin["prenom"])
                self.entry_specialite.delete(0, tk.END)
                self.entry_specialite.insert(0, medecin["specialite"])
                self.entry_num_tel.delete(0, tk.END)
                self.entry_num_tel.insert(0, medecin["num_tel"])
                self.horaire_lundi =medecin["horaires_lundi"]
                self.horaire_mardi =medecin["horaires_mardi"]
                self.horaire_mercredi = medecin["horaires_mercredi"]
                self.horaire_jeudi = medecin["horaires_jeudi"]
                self.horaire_vendredi = medecin["horaires_vendredi"]
                self.horaire_samedi = medecin["horaires_samedi"]
                self.horaire_dimanche = medecin["horaires_dimanche"]
                self.selected_medecin_id = medecin["ref_medecin"]

    def save_modifications(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        specialite = self.entry_specialite.get()
        num_tel = self.entry_num_tel.get()

        # Basic validation
        if not all([nom, prenom, specialite, num_tel]):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        # Additional validation for phone number format
        if not num_tel.isdigit() or len(num_tel) != 10:
            messagebox.showerror("Erreur",
                                 "Le numéro de téléphone doit contenir uniquement des chiffres et être de 10 chiffres.")
            return

        # Enregistrement des modifications dans la base de données
        self.bdd_manager.modifier_medecin(nom, prenom, num_tel, specialite, self.horaire_lundi, self.horaire_mardi,
                                          self.horaire_mercredi, self.horaire_jeudi, self.horaire_vendredi,
                                          self.horaire_samedi, self.horaire_dimanche, self.selected_medecin_id)

        self.destroy()


