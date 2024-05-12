import tkinter as tk
from tkinter import ttk
from lib.frontend.modales_planning.nouveau_patient import ModaleNouveauPatient
from lib.bdd_manager import BDDManager
import sys
from pathlib import Path

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

# --------------- GESTION DES CHAMPS DE TEXTE ---------------
def configurer_entree(entree, texte_par_defaut):
    entree.default_text = texte_par_defaut  # Stocker le texte par défaut dans une propriété de l'objet Entry
    entree.insert(0, texte_par_defaut)
    entree.bind("<FocusIn>", lambda event: clear_entry(entree))  # Utiliser une fonction séparée pour gérer le focus
    entree.bind("<FocusOut>", lambda event: restore_default_text(entree))  # Utiliser une fonction séparée pour gérer la perte du focus

def clear_entry(entree):
    if entree.get() == entree.default_text:
        entree.delete(0, tk.END)

def restore_default_text(entree):
    if entree.get() == "":
        entree.insert(0, entree.default_text)
# --------------- FIN GESTION DES CHAMPS DE TEXTE ---------------

class ModaleNouveauRDV(tk.Toplevel):
    def __init__(self, bdd_manager: BDDManager, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#9BBFDA")
        self.bdd_manager = bdd_manager
        self.resizable(False, False)
        self.title("Nouveaux Rendez-vous")
        self.grab_set()
        self.secondary_window = None
        self.date = ""
        self.heure_debut = ""
        self.date_heure_debut = ""

        patients = self.bdd_manager.get_all_patients()
        self.patient_names = [patient["nom"] for patient in patients]
        self.patient_ids = [patient["ref_patient"] for patient in patients]

        self.selected_patient = tk.StringVar(self)
        self.selected_patient.set("Sélectionnez un patient")
        self.patient_dropdown = ttk.OptionMenu(self, self.selected_patient, *self.patient_names)
        self.patient_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.button_new_patient = ttk.Button(
            self,
            text="Nouveau patient",
            command=self.open_nouveau_patient
        )
        self.button_new_patient.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # style pour les champs de texte
        self.style = ttk.Style()
        self.style.configure("Custom.TEntry", background="blue",padding=[20,10,20,10], font=("Arial", 12))
        self.style.configure("Custom.TButton",
                                foreground="black",
                                background="blue",
                                font=("Inter", 12),
                                padding=[10,10,10,10],
                                justify="center")

        self.entry_date = ttk.Entry(self, style="Custom.TEntry")
        self.entry_date.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.default_date_text = "Date (AAAA-MM-JJ)"
        configurer_entree(self.entry_date, self.default_date_text)

        self.entry_heure_debut = ttk.Entry(self, style="Custom.TEntry")
        self.entry_heure_debut.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.default_heure_text = "Heure (HH:MM:SS) "
        configurer_entree(self.entry_heure_debut, self.default_heure_text)

        self.heure_debut = ""

        self.entry_duree = ttk.Entry(self, style="Custom.TEntry")
        self.entry_duree.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.default_duree_text = "Durée (HH:MM)"
        configurer_entree(self.entry_duree, self.default_duree_text)

        self.duree = ""   # Variable pour stocker la durée saisie

        self.button_stocker = ttk.Button(
            self,
            text="Valider",
            command=self.valider_donnees,  # Appel de la méthode valider_donnees de la classe
            style="Custom.TButton",
        )
        self.button_stocker.grid(row=5, column=0, padx=10, pady=10, sticky="we")

    def open_nouveau_patient(self):
        self.grab_release()  # Annuler le grab_set
        self.secondary_window = ModaleNouveauPatient(self.bdd_manager)

    def stocker_duree(self):
        if self.entry_duree.get() != self.default_duree_text:
            self.duree = self.entry_duree.get()
        else:
            self.duree = ""

    def stocker_heure_debut(self):
        if self.entry_heure_debut.get() != self.default_heure_text:
            self.heure_debut = self.entry_heure_debut.get()
        else:
            self.heure_debut = ""

    def stocker_date(self):
        if self.entry_date.get() != self.default_date_text:
            self.date = self.entry_date.get()
        else:
            self.date = ""

    def stocker_date_et_heure_debut(self):
            self.date_heure_debut = self.date + " " + self.heure_debut

    def valider_donnees(self):
        self.stocker_duree()
        self.stocker_heure_debut()
        self.stocker_date()
        self.stocker_date_et_heure_debut()

        # Récupération de l'ID du patient
        selected_index = self.patient_names.index(self.selected_patient.get())
        ref_patient = self.patient_ids[selected_index]

        ref_medecin = "1"  # comment récup le medecin sélectionné ?

        # print("Date et heure de début:", self.date_heure_debut)
        # print("Durée:", self.duree)
        # print("ID du patient sélectionné:", ref_patient)
        # print("ID du médecin:", ref_medecin)

        # ajouter RDV
        self.bdd_manager.ajout_rdv(self.date_heure_debut, self.duree, ref_patient, ref_medecin)
