import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importer Pillow pour gérer les images
import sys
from pathlib import Path
from datetime import date
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[2])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.bdd_manager import BDDManager
from lib.frontend.modales_planning.resume_rdv import ModaleResumeRDV
from lib.frontend.modales_planning.modifier_rdv import ModaleModifierRDV
from lib.frontend.modales_planning.nouveau_rdv import ModaleNouveauRDV
# from lib.frontend.modales_planning.nouveau_patient import ModaleNouveauPatient
from lib.frontend.modales_planning.etat_consultations import ModaleEtatConsultations
from lib.frontend.modales_planning.modifier_horaires import ModaleModifierHoraires

class OngletPlanning(ttk.Frame):

    def __init__(self, master, bdd_manager: BDDManager):
        super().__init__(master)
        self.bdd_manager = bdd_manager

        # création de la frame "options"
        self.frame_options = ttk.Frame(self)
        self.frame_options.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.rowconfigure(1, weight=1)
        # initialisation de la liste des médecins
        self.list_medecins = self.bdd_manager.get_all_medecins()
        # création des options de sélection de planning
        self.planning_selection_options = ["Cabinet"]
        self.medecin_ids = {}
        for medecin in self.list_medecins:
            nom_complet = f"Dr. {medecin['nom']}"
            self.planning_selection_options.append(nom_complet)
            self.medecin_ids[nom_complet] = medecin["ref_medecin"]
        # menu déroulant de sélection de planning
        self.planning_selected = tk.StringVar()
        self.planning_selected.set(self.planning_selection_options[0])
        self.planning_selection_menu = ttk.OptionMenu(
            self.frame_options,
            self.planning_selected,
            self.planning_selection_options[0],
            *self.planning_selection_options,
            command=self.update_planning_selected
        )
        self.planning_selection_menu.grid(column=0, row=0, sticky=(tk.W, tk.E))
        # style de boutons multilignes
        style = ttk.Style()
        style.configure("Multiline.TButton", justify="center")
        # bouton "Nouveau RDV"
        self.button_nouveau_rdv = ttk.Button(self.frame_options, text="Nouveau RDV", command=self.open_modale_nouveau_rdv)
        self.button_nouveau_rdv.grid(column=0, row=1, sticky=(tk.W, tk.E))
        # bouton "modifier horaires"
        self.button_modifier_horaires = ttk.Button(
            self.frame_options,
            text="Modifier\nouverture / disponibilités",
            style="Multiline.TButton",
            command=self.modale_modifier_horaires
        )
        self.button_modifier_horaires.grid(column=0, row=2, sticky=(tk.W, tk.E))
        self.button_etat_consultations = ttk.Button(
            self.frame_options,
            text="Etat des\nconsultations",
            style="Multiline.TButton",
            command=self.modale_etat_consultation
        )
        self.button_etat_consultations.grid(column=0, row=3, sticky=(tk.W, tk.E, tk.N))
        self.frame_options.rowconfigure(3, weight=1)
        # self.icon_left_arrow_pil_img = Image.open(Path(ROOT_DIR_PATH) / "assets" / "icon_arrow_left.png").resize((20, 20))
        # self.icon_left_arrow = ImageTk.PhotoImage(self.icon_left_arrow_pil_img)
        # self.button_test = ttk.Button(
        #     self.frame_options,
        #     # text="test test",
        #     image=self.icon_left_arrow,
        #     command=""
        # )
        # self.button_test.grid(column=0, row=4, sticky=(tk.E, tk.W))

        # création de la frame "date"
        # self.frame_date = ttk.Frame(self, borderwidth=2, relief="solid")
        self.frame_date = ttk.Frame(self)
        self.frame_date.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(1, weight=1)
        # création de 3 frames pour les deux boutons "semaine suivante" et "semaine précédente" et le label
        self.frame_date_left = ttk.Frame(self.frame_date)
        self.frame_date_left.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame_date.columnconfigure(0, weight=1)
        self.frame_date.columnconfigure(1, weight=1)
        self.frame_date.columnconfigure(2, weight=1)
        # self.frame_date.columnconfigure(3, weight=1)
        self.frame_date_left.columnconfigure(0, weight=1)
        self.frame_date_left.columnconfigure(1, weight=1)
        # bouton "semaine précédente"
        # https://www.svgrepo.com/svg/533659/chevron-left
        self.icon_left_arrow_pil_img = Image.open(Path(ROOT_DIR_PATH) / "assets" / "icon_arrow_left.png").resize((20, 20))
        self.icon_left_arrow = ImageTk.PhotoImage(self.icon_left_arrow_pil_img)
        self.button_previous_week = ttk.Button(
            self.frame_date_left,
            image=self.icon_left_arrow,
            # text="lol haha",
            command=""
        )
        self.button_previous_week.grid(column=1, row=0, sticky=tk.E)
        # bouton "semaine suivante"
        # https://www.svgrepo.com/svg/533661/chevron-right
        self.icon_right_arrow_pil_img = Image.open(Path(ROOT_DIR_PATH) / "assets" / "icon_arrow_right.png").resize((20, 20))
        self.icon_right_arrow = ImageTk.PhotoImage(self.icon_right_arrow_pil_img)
        self.button_next_week = ttk.Button(
            self.frame_date,
            image=self.icon_right_arrow,
            command=""
        )
        self.button_next_week.grid(column=2, row=0, sticky=tk.W)
        # bouton sélection de date
        # https://www.svgrepo.com/svg/533381/calendar-alt
        self.icon_calendar_pil_img = Image.open(Path(ROOT_DIR_PATH) / "assets" / "icon_calendar.png").resize((20, 20))
        self.icon_calendar = ImageTk.PhotoImage(self.icon_calendar_pil_img)
        self.button_next_week = ttk.Button(
            self.frame_date_left,
            image=self.icon_calendar,
            command=""
        )
        self.button_next_week.grid(column=0, row=0, sticky=tk.W)
        # label d'affichage des dates de la semaine
        self.label_current_week = ttk.Label(
            self.frame_date,
            text="Semaine du XX/XX au XX/XX"
        )
        self.label_current_week.grid(column=1, row=0)

        # création de la frame "planning"
        self.frame_planning = ttk.Frame(self)
        self.frame_planning.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))

        # maj de l'affichage de la page
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
