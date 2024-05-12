import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from lib.bdd_manager import BDDManager

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
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
class ModaleNouveauPatient(tk.Toplevel):
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

        # style pour les champs de texte
        self.style = ttk.Style()
        self.style.configure("Custom.TEntry", background="blue", padding=[20, 10, 20, 10], font=("Arial", 12))
        self.style.configure("Custom.TButton", foreground="black", background="blue", font=("Inter", 12),
                             padding=[10, 10, 10, 10], justify="center")

        self.entry_nom = ttk.Entry(self, style="Custom.TEntry")
        self.entry_nom.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.default_nom_text = "Nom"
        configurer_entree(self.entry_nom, self.default_nom_text)

        self.entry_prenom = ttk.Entry(self, style="Custom.TEntry")
        self.entry_prenom.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.default_prenom_text = "Prénom"
        configurer_entree(self.entry_prenom, self.default_prenom_text)

        self.entry_tel = ttk.Entry(self, style="Custom.TEntry")
        self.entry_tel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.default_tel_text = "Téléphone"
        configurer_entree(self.entry_tel, self.default_tel_text)

        self.button_stocker = ttk.Button(
            self,
            text="Valider",
            command=self.valider_donnees,  # Appel de la méthode valider_donnees de la classe
            style="Custom.TButton",
        )
        self.button_stocker.grid(row=3, column=0, padx=10, pady=10, sticky="we")

    def stocker_nom(self):
        if self.entry_nom.get() != self.default_nom_text:
            self.nom_patient = self.entry_nom.get()
        else:
            self.nom_patient = ""

    def stocker_prenom(self):
        if self.entry_prenom.get() != self.default_prenom_text:
            self.prenom_patient = self.entry_prenom.get()
        else:
            self.prenom_patient = ""

    def stocker_tel(self):
        if self.entry_tel.get() != self.default_tel_text:
            self.tel_patient = self.entry_tel.get()
        else:
            self.tel_patient = ""

    def valider_donnees(self):
        self.stocker_nom()
        self.stocker_prenom()
        self.stocker_tel()
