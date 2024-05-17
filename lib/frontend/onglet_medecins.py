import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from lib.bdd_manager import BDDManager
from lib.frontend.modales_medecins.nouveau_medecin import ModaleNouveauMedecin
from lib.frontend.modales_medecins.modifier_medecin import ModaleModifierMedecin

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class OngletMedecins(ttk.Frame):

    def __init__(self, master, bdd_manager: BDDManager):
        super().__init__(master, borderwidth=10, relief="solid")
        self.bdd_manager = bdd_manager

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

        self.label_nom = ttk.Label(self, text="Nom:")
        self.label_nom.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_prenom = ttk.Label(self, text="Prénom:")
        self.label_prenom.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.label_specialite = ttk.Label(self, text="Spécialité:")
        self.label_specialite.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.label_num_tel = ttk.Label(self, text="Numéro de téléphone:")
        self.label_num_tel.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.label_nom_medecin = ttk.Label(self)
        self.label_nom_medecin.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_prenom_medecin = ttk.Label(self)
        self.label_prenom_medecin.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_specialite_medecin = ttk.Label(self)
        self.label_specialite_medecin.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.label_num_tel_medecin = ttk.Label(self)
        self.label_num_tel_medecin.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.button_new_medecin = ttk.Button(
            self,
            text="Nouveau médecin",
            command=self.open_nouveau_medecin
        )
        self.button_new_medecin.grid(row=8, column=10, padx=10, pady=10, sticky="w")

        self.button_modif_medecin = ttk.Button(
            self,
            text="Modifier médecin",
            command=self.open_modif_medecin
        )
        self.button_modif_medecin.grid(row=8, column=9, padx=10, pady=10, sticky="w")

        self.button_suppr_medecin = ttk.Button(
            self,
            text="Supprimer médecin",
            command=self.supprimer_medecin
        )
        self.button_suppr_medecin.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    def update_medecin_selected(self, medecin_selected):
        for medecin in self.bdd_manager.get_all_medecins():
            if medecin["nom"] == medecin_selected:
                self.label_nom_medecin.config(text=medecin["nom"])
                self.label_prenom_medecin.config(text=medecin["prenom"])
                self.label_specialite_medecin.config(text=medecin["specialite"])
                self.label_num_tel_medecin.config(text=medecin["num_tel"])
                self.selected_medecin_id = medecin["ref_medecin"]
                break

    def open_nouveau_medecin(self):
        ModaleNouveauMedecin(self.bdd_manager)

    def open_modif_medecin(self):
        ModaleModifierMedecin(self.bdd_manager)

    def supprimer_medecin(self):
        if hasattr(self, 'selected_medecin_id'):
            self.bdd_manager.supprimer_medecin(self.selected_medecin_id)

            # Mettre à jour la liste des médecins et l'interface
            self.medecins = self.bdd_manager.get_all_medecins()
            self.medecin_names = [medecin["nom"] for medecin in self.medecins]
            self.medecin_dropdown["menu"].delete(0, "end")
            for medecin_name in self.medecin_names:
                self.medecin_dropdown["menu"].add_command(
                    label=medecin_name,
                    command=lambda value=medecin_name: self.selected_medecin.set(value)
                )

            # Réinitialiser les labels
            self.label_nom_medecin.config(text="")
            self.label_prenom_medecin.config(text="")
            self.label_specialite_medecin.config(text="")
            self.label_num_tel_medecin.config(text="")
            self.selected_medecin.set("Sélectionnez un médecin")
