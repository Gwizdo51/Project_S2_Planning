import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb  # For error message handling
import sys
from pathlib import Path

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.frontend.modales_planning.nouveau_patient import ModaleNouveauPatient
from lib.bdd_manager import BDDManager


def configurer_entree(entree, texte_par_defaut):
    entree.default_text = texte_par_defaut
    entree.insert(0, texte_par_defaut)
    entree.bind("<FocusIn>", lambda event: clear_entry(entree))
    entree.bind("<FocusOut>", lambda event: restore_default_text(entree))


def clear_entry(entree):
    if entree.get() == entree.default_text:
        entree.delete(0, tk.END)


def restore_default_text(entree):
    if entree.get() == "":
        entree.insert(0, entree.default_text)


class ModaleNouveauRDV(tk.Toplevel):
    def __init__(self, bdd_manager: BDDManager, ref_medecin, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#9BBFDA")
        self.bdd_manager = bdd_manager
        self.ref_medecin = ref_medecin
        self.resizable(False, False)
        self.title("Nouveau Rendez-vous")
        self.grab_set()
        self.secondary_window = None
        self.date = ""
        self.heure_debut = ""
        self.date_heure_debut = ""

        patients = self.bdd_manager.get_all_patients()
        self.patient_names = [patient["nom"] for patient in patients]
        self.patient_ids = [patient["ref_patient"] for patient in patients]

        self.patient_names.insert(0, "Sélectionnez un patient")
        self.selected_patient = tk.StringVar(self)
        self.selected_patient.set(self.patient_names[0])
        self.patient_dropdown = ttk.OptionMenu(
            self,
            self.selected_patient,
            *self.patient_names,
            command=self.update_patient_selected
        )
        self.patient_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.button_new_patient = ttk.Button(
            self,
            text="Nouveau patient",
            command=self.open_nouveau_patient
        )
        self.button_new_patient.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_date = ttk.Entry(self, style="Custom.TEntry")
        self.entry_date.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.default_date_text = "Date (AAAA-MM-JJ)"
        configurer_entree(self.entry_date, self.default_date_text)

        self.entry_heure_debut = ttk.Entry(self, style="Custom.TEntry")
        self.entry_heure_debut.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.default_heure_text = "Heure (HH:MM:SS)"
        configurer_entree(self.entry_heure_debut, self.default_heure_text)

        self.entry_duree = ttk.Entry(self, style="Custom.TEntry")
        self.entry_duree.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.default_duree_text = "Durée (HH:MM)"
        configurer_entree(self.entry_duree, self.default_duree_text)

        self.button_stocker = ttk.Button(
            self,
            text="Valider",
            command=self.valider_donnees,
            style="Custom.TButton",
        )
        self.button_stocker.grid(row=5, column=0, padx=10, pady=10, sticky="we")

    def update_patient_selected(self, event):
        self.selected_patient.set(event)

    def open_nouveau_patient(self):
        self.grab_release()
        self.secondary_window = ModaleNouveauPatient(self.bdd_manager)

    def stocker_duree(self):
        self.duree = self.entry_duree.get() if self.entry_duree.get() != self.default_duree_text else ""

    def stocker_heure_debut(self):
        self.heure_debut = self.entry_heure_debut.get() if self.entry_heure_debut.get() != self.default_heure_text else ""

    def stocker_date(self):
        self.date = self.entry_date.get() if self.entry_date.get() != self.default_date_text else ""

    def stocker_date_et_heure_debut(self):
        self.date_heure_debut = self.date + " " + self.heure_debut

    def valider_donnees(self):
        self.stocker_duree()
        self.stocker_heure_debut()
        self.stocker_date()
        self.stocker_date_et_heure_debut()

        if not self.date or not self.heure_debut or not self.duree or self.selected_patient.get() == "Sélectionnez un patient":
            mb.showerror("Erreur de saisie",
                         "Veuillez remplir correctement tous les champs (date, heure, durée, patient).")
            return

        selected_index = self.patient_names.index(self.selected_patient.get())
        ref_patient = self.patient_ids[selected_index]

        print("Date et heure de début:", self.date_heure_debut)
        print("Durée:", self.duree)
        print("ID du patient sélectionné:", ref_patient)
        print("ID du médecin:", self.ref_medecin)

        self.bdd_manager.ajout_rdv(self.date_heure_debut, self.duree, ref_patient, self.ref_medecin)

        # Close the window after adding the appointment
        self.destroy()
