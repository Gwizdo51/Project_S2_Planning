import tkinter as tk
from tkinter import ttk
from lib.frontend.modales_planning.nouveau_patient import ModaleNouveauPatient
from lib.bdd_manager import BDDManager
import sys
from pathlib import Path


ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

def configurer_entree(entree, texte_par_defaut):  #fonction pour mettre un "placeholder"
    entree.insert(0, texte_par_defaut)
    entree.bind("<FocusIn>", lambda event: entree.delete(0, tk.END))
    entree.bind("<FocusOut>", lambda event: entree.insert(0, texte_par_defaut) if not entree.get() else None)

class ModaleNouveauRDV(tk.Toplevel):
    def __init__(self, bdd_manager: BDDManager, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#9BBFDA")
        self.bdd_manager = bdd_manager
        self.resizable(False, False)
        self.title("Nouveaux Rendez-vous")
        self.grab_set()
        self.secondary_window = None

        patients = self.bdd_manager.get_all_patients()
        patient_names = [patient["nom"] for patient in patients]

        self.selected_patient = tk.StringVar(self)
        self.selected_patient.set("Sélectionnez un patient")
        self.patient_dropdown = ttk.OptionMenu(self, self.selected_patient, *patient_names)  # menu_déroulant_patient
        self.patient_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.button_new_patient = ttk.Button(
            self,
            text="Nouveau patient",
            command=self.open_nouveau_patient
        )
        self.button_new_patient.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # style pour les champs de texte
        self.style = ttk.Style()
        self.style.configure("Custom.TEntry", background="blue",padding=[10,10,10,10], font=("Arial", 12))
        self.style.configure("Custom.TButton",
                                foreground="black",
                                background="blue",
                                font=("Inter", 12),
                                padding=[10,10,10,10],
                                justify="center")

        self.entry_heure_debut = ttk.Entry(self, style="Custom.TEntry")
        self.entry_heure_debut.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        configurer_entree(self.entry_heure_debut, "Heure Début (HH:MM)")


        self.heure_debut = ""

        self.entry_duree = ttk.Entry(self, style="Custom.TEntry")
        self.entry_duree.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        configurer_entree(self.entry_duree, "Durée (HH:MM)")

        self.duree = ""   # Variable pour stocker la durée saisie

        self.button_stocker = ttk.Button(
            self,
            text="Valider",
            command=self.valider_donnees,  # Appel de la méthode valider_donnees de la classe
            style="Custom.TButton",
        )
        self.button_stocker.grid(row=4, column=0, padx=10, pady=10, sticky="we")

    def open_nouveau_patient(self):
        self.secondary_window = ModaleNouveauPatient()

    def stocker_duree(self):
        self.duree = self.entry_duree.get()

    def stocker_heure_debut(self):
        self.heure_debut = self.entry_heure_debut.get()

    def valider_donnees(self):
        self.stocker_duree()
        self.stocker_heure_debut()