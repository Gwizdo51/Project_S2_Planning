import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.bdd_manager import BDDManager
from lib.frontend.modales_planning.resume_rdv import ModaleResumeRDV
from lib.frontend.modales_planning.modifier_rdv import ModaleModifierRDV
from lib.frontend.modales_planning.nouveau_rdv import ModaleNouveauRDV
from lib.frontend.modales_planning.nouveau_patient import ModaleNouveauPatient
from lib.frontend.modales_planning.etat_consultations import ModaleEtatConsultations
from lib.frontend.modales_planning.modifier_horaires import ModaleModifierHoraires


class OngletPlanning(ttk.Frame):

    def __init__(self, master, bdd_manager: BDDManager):
        super().__init__(master)
        self.bdd_manager = bdd_manager
        # self.content = ttk.Label(self, text="Contenu de l'onglet Planning")
        # self.content.grid(column=0, row=0)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.button_open = tk.Button(
        #     self,
        #     text="état de consultation",
        #     command=self.open_etat_consultation,
        #     font=("Arial", 12), background="#305F82", bd=0, relief="flat", width=16, height=2
        # )
        # self.button_open.place(x=30, y=250)
        # self.button_nouveau_rdv = tk.Button(
        #     self,
        #     text="Nouveaux RDV",
        #     command=self.open_nouveau_rdv,
        #     font=("Arial", 12), background="#305F82", bd=0, relief="flat", width=16, height=2
        # )
        # self.button_nouveau_rdv.place(x=30, y=150)

        # frame zone de sélection de semaine
        self.frame_week_selection = ttk.Frame(self)
        self.frame_week_selection.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        # frame barre d'outils
        self.frame_toolbar = ttk.Frame(self)
        self.frame_toolbar.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        # frame calendrier
        self.frame_calendar = ttk.Frame(self)
        self.frame_calendar.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        # remplissage de l'espace
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        ### zone de sélection de semaine
        # liste déroulante de sélection de planning
        self.list_medecins = self.bdd_manager.get_all_medecins()
        # print(self.list_medecins)
        self.planning_selection_options = ["Cabinet"]
        self.planning_selection_options += [f"Dr. {medecin["nom"]}" for medecin in self.list_medecins]
        self.planning_selected = tk.StringVar()
        self.planning_selection_menu = ttk.OptionMenu(
            self.frame_toolbar,
            self.planning_selected,
            self.planning_selection_options[0],
            *self.planning_selection_options,
            command=self.update_planning_selected
        )
        self.planning_selection_menu.grid(column=0, row=0, sticky=(tk.W, tk.E))
        # bouton "Nouveau RDV"
        self.button_nouveau_rdv = ttk.Button(self.frame_toolbar, text="Nouveau RDV", command=self.modale_nouveau_rdv)
        self.button_nouveau_rdv.grid(column=0, row=1, sticky=(tk.W, tk.E))
        # bouton "Modifier ouverture / disponibilités"
        style = ttk.Style()
        # print(style.element_options("TButton.label"))
        # style.configure("Multiline.TButton", foreground="red")
        style.configure("Multiline.TButton", justify="center")
        self.button_modifier_horaires = ttk.Button(
            self.frame_toolbar,
            text="Modifier\nouverture / disponibilités",
            style="Multiline.TButton",
            command=self.modale_modifier_horaires
        )
        # print(self.button_modifier_horaires.winfo_class())
        self.button_modifier_horaires.grid(column=0, row=2, sticky=(tk.W, tk.E))
        # bouton "Etat des consultations"
        self.button_etat_consultations = ttk.Button(
            self.frame_toolbar,
            text="Etat des\nconsultations",
            style="Multiline.TButton",
            command=self.modale_etat_consultation
        )
        self.button_etat_consultations.grid(column=0, row=3, sticky=(tk.W, tk.E))
        self.update_planning_selected()

    def update_planning_selected(self, planning_selected=""):
        # désactiver le bouton "Nouveau RDV" si le planning du cabinet est sélectionné
        if self.planning_selected.get() == "Cabinet":
            self.button_nouveau_rdv["state"] = "disabled"
        else:
            self.button_nouveau_rdv["state"] = "normal"

    def modale_nouveau_rdv(self):
        # ModaleNouveauRDV(self.bdd_manager)
        pass

    def modale_modifier_horaires(self):
        # ModaleModifierHoraires(self.bdd_manager)
        pass

    def modale_etat_consultation(self):
        ModaleEtatConsultations(self.bdd_manager)
