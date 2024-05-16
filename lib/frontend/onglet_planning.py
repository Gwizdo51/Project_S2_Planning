import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importer Pillow pour gérer les images
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

        # Initialisation de la liste des médecins
        self.list_medecins = self.bdd_manager.get_all_medecins()

        self.frame_toolbar = ttk.Frame(self)
        self.frame_toolbar.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Création des options de sélection de planning
        self.planning_selection_options = ["Cabinet"]
        self.medecin_ids = {}
        for medecin in self.list_medecins:
            nom_complet = f"Dr. {medecin['nom']}"
            self.planning_selection_options.append(nom_complet)
            self.medecin_ids[nom_complet] = medecin["ref_medecin"]

        self.planning_selected = tk.StringVar()
        self.planning_selected.set(self.planning_selection_options[0])

        # Menu déroulant de sélection de planning
        self.planning_selection_menu = ttk.OptionMenu(
            self.frame_toolbar,
            self.planning_selected,
            self.planning_selection_options[0],
            *self.planning_selection_options,
            command=self.update_planning_selected
        )
        self.planning_selection_menu.grid(column=0, row=0, sticky=(tk.W, tk.E))

        # Bouton "Nouveau RDV"
        self.button_nouveau_rdv = ttk.Button(self.frame_toolbar, text="Nouveau RDV", command=self.open_modale_nouveau_rdv)
        self.button_nouveau_rdv.grid(column=0, row=1, sticky=(tk.W, tk.E))

        # Autres boutons et configuration
        self.button_modifier_horaires = ttk.Button(
            self.frame_toolbar,
            text="Modifier\nouverture / disponibilités",
            style="Multiline.TButton",
            command=self.modale_modifier_horaires
        )
        self.button_modifier_horaires.grid(column=0, row=2, sticky=(tk.W, tk.E))

        self.button_etat_consultations = ttk.Button(
            self.frame_toolbar,
            text="Etat des\nconsultations",
            style="Multiline.TButton",
            command=self.modale_etat_consultation
        )
        self.button_etat_consultations.grid(column=0, row=3, sticky=(tk.W, tk.E))
        self.update_planning_selected()

        # Charger et afficher l'image de fond
        image_path = Path(__file__).resolve().parent / "planning.png"
        self.canvas = tk.Canvas(self, width=500, height=500)  # Ajuster les dimensions selon vos besoins
        self.canvas.grid(column=1, row=0, rowspan=4, sticky=(tk.N, tk.E, tk.S, tk.W))

        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((600, 450), Image.Resampling.LANCZOS)  # Ajuster la taille de l'image
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 50, image=self.bg_photo, anchor=tk.NW)  # Ajuster la coordonnée y pour descendre l'image

        # Ajuster les colonnes et les lignes pour une mise en page correcte
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

    def update_planning_selected(self, planning_selected=""):
        if self.planning_selected.get() == "Cabinet":
            self.button_nouveau_rdv["state"] = "disabled"
        else:
            self.button_nouveau_rdv["state"] = "normal"

    def open_modale_nouveau_rdv(self):
        selected_medecin = self.planning_selected.get()
        ref_medecin = self.medecin_ids.get(selected_medecin, None)
        if ref_medecin:
            ModaleNouveauRDV(self.bdd_manager, ref_medecin=ref_medecin)

    def modale_modifier_horaires(self):
        pass

    def modale_etat_consultation(self):
        ModaleEtatConsultations(self.bdd_manager)
