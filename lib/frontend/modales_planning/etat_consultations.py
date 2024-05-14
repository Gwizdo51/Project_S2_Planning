import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from tkinter import messagebox #géré message d'erreur

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.bdd_manager import BDDManager

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class ModaleEtatConsultations(tk.Toplevel):
    def __init__(self, bdd_manager: BDDManager, **kwargs):
        super().__init__(**kwargs)
        self.config(width=800, height=600, bg="#CCE2F3")
        self.bdd_manager = bdd_manager
        self.resizable(False, False)
        self.title("État des consultations")
        self.grab_set()
        self.focus()
        self.label_title = ttk.Label(self, text="État des consultations", font=("Helvetica", 14, "bold"),
                                     background="#CCE2F3")
        self.label_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Récupération de l'historique de tous les médecins
        self.resultats = self.bdd_manager.historique()

        # Création de l'en-tête du tableau
        ttk.Label(self, text="Nom du médecin", font=("Helvetica", 12, "bold"), background="#CCE2F3").grid(row=2,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        ttk.Label(self, text="Nombre de rendez-vous", font=("Helvetica", 12, "bold"), background="#CCE2F3").grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=5,
                                                                                                                 sticky="w")
        ttk.Label(self, text="Durée totale des rendez-vous", font=("Helvetica", 12, "bold"), background="#CCE2F3").grid(
            row=2, column=2, padx=10, pady=5, sticky="w")

        # Affichage de l'historique de tous les médecins
        row = 3
        for resultat in self.resultats:
            nom_medecin = resultat[0] + " " + resultat[1]  # Index 0 pour nom, index 1 pour prénom
            ttk.Label(self, text=nom_medecin, font=("Helvetica", 10), background="#CCE2F3").grid(row=row, column=0,
                                                                                                 padx=10, pady=2,
                                                                                                 sticky="w")

            nb_rdv = resultat[2]  # Index 2 pour nombre de rendez-vous
            ttk.Label(self, text=nb_rdv, font=("Helvetica", 10), background="#CCE2F3").grid(row=row, column=1, padx=10,
                                                                                            pady=2, sticky="w")

            duree_totale = resultat[3]  # Index 3 pour durée totale
            ttk.Label(self, text=duree_totale, font=("Helvetica", 10), background="#CCE2F3").grid(row=row, column=2,
                                                                                                  padx=10, pady=2,
                                                                                                  sticky="w")

            row += 1

        # Ajout du bouton pour imprimer
        self.button_print = ttk.Button(self, text="Imprimer", command=self.imprimer_pdf)
        self.button_print.grid(row=row, column=0, columnspan=3, padx=10, pady=10)

    def imprimer_pdf(self):
        # Importation des modules de reportlab ici
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        # Création du fichier PDF
        nom_fichier = "etat_consultations.pdf"
        c = canvas.Canvas(nom_fichier, pagesize=letter)

        # Positionnement du texte dans le fichier PDF
        x, y = 100, 750
        for resultat in self.resultats:
            nom_medecin = resultat[0] + " " + resultat[1]
            nb_rdv = resultat[2]
            duree_totale = resultat[3]
            c.drawString(x, y, f"Nom du médecin: {nom_medecin}")
            c.drawString(x, y - 20, f"Nombre de rendez-vous: {nb_rdv}")
            c.drawString(x, y - 40, f"Durée totale des rendez-vous: {duree_totale}")
            y -= 60

        c.save()
        messagebox.showinfo("Impression réussie", "Le fichier PDF a été généré avec succès !")