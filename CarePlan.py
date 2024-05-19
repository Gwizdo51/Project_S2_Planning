import tkinter as tk
from tkinter import ttk

from lib.bdd_manager import BDDManager
from lib.frontend.onglet_planning import OngletPlanning
from lib.frontend.onglet_patients import OngletPatients
from lib.frontend.onglet_medecins import OngletMedecins
from lib.frontend.utils import configure_styles


class Application(tk.Tk):
    """Classe responsable de la fenêtre principale de l'application.
    """

    onglets = {
        "Planning": OngletPlanning,
        "Patients": OngletPatients,
        "Médecins": OngletMedecins
    }

    def __init__(self):
        super().__init__()
        # configure les styles de l'application
        configure_styles()
        self.bdd_manager = BDDManager()
        self.config(bg="#9BBFDA")
        self.title("CarePlan")
        # taille de la fenêtre
        self.geometry("800x600")
        # taille fixe
        self.resizable(False, False)
        # notebook pour les onglets
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        for nom_onglet in self.onglets.keys():
            nouvel_onglet = self.onglets[nom_onglet](self.notebook, self.bdd_manager)
            self.notebook.add(nouvel_onglet, text=nom_onglet)
        # remplir la fenêtre avec le contenu du notebook
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # lancer l'application
        self.mainloop()


if __name__ == "__main__":
    Application()
