import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importer Pillow pour gérer les images
import sys
from pathlib import Path
from PIL import ImageTk, Image
from datetime import datetime, time, timedelta
# from babel.dates import format_date

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
from lib.frontend.modales_planning.selection_date import ModaleSelectionDate

class OngletPlanning(ttk.Frame):

    def __init__(self, master, bdd_manager: BDDManager):
        super().__init__(master)
        self.bdd_manager = bdd_manager

        # création de la frame "options"
        self.frame_options = ttk.Frame(self)
        # self.frame_options = ttk.Frame(self, borderwidth=5, relief="raised")
        self.frame_options.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.rowconfigure(1, weight=1)
        # initialisation de la liste des médecins
        self.list_medecins = self.bdd_manager.get_all_medecins()
        # création des options de sélection de planning
        self.planning_selection_options = ["Cabinet"]
        # pour chaque médecin ...
        for medecin in self.list_medecins:
            # crée et ajoute leur leur nom affiché
            name_displayed = f"Dr. {medecin["nom"]}"
            medecin["nom_affiche"] = name_displayed
            # ajoute le nom affiché du médecin à la liste de sélection des planning
            self.planning_selection_options.append(name_displayed)
        # crée un mapping nom_affiche -> ref_medecin
        self.medecin_name_displayed_to_ref = {medecin["nom_affiche"]: medecin["ref_medecin"] for medecin in self.list_medecins}
        # menu déroulant de sélection de planning
        self.planning_selected = tk.StringVar()
        self.planning_selected.set(self.planning_selection_options[0])
        self.planning_selection_menu = ttk.OptionMenu(
            self.frame_options,
            self.planning_selected,
            self.planning_selection_options[0],
            *self.planning_selection_options,
            # command=self.update_planning
            command=lambda event: self.update_planning()
        )
        self.planning_selection_menu.grid(column=0, row=0, sticky=(tk.W, tk.E))
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
        # récupère la date d'aujourd'hui
        date_today = datetime.today()
        # met l'heure à 00:00
        date_today = datetime(date_today.year, date_today.month, date_today.day)
        # récupère la date du lundi de la semaine actuelle
        self.date_monday_week_displayed = date_today - timedelta(days=date_today.weekday())
        # self.frame_date = ttk.Frame(self, borderwidth=5, relief="raised")
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
            command=self.select_previous_week
        )
        self.button_previous_week.grid(column=1, row=0, sticky=tk.E)
        # bouton "semaine suivante"
        # https://www.svgrepo.com/svg/533661/chevron-right
        self.icon_right_arrow_pil_img = Image.open(Path(ROOT_DIR_PATH) / "assets" / "icon_arrow_right.png").resize((20, 20))
        self.icon_right_arrow = ImageTk.PhotoImage(self.icon_right_arrow_pil_img)
        self.button_next_week = ttk.Button(
            self.frame_date,
            image=self.icon_right_arrow,
            command=self.select_next_week
        )
        self.button_next_week.grid(column=2, row=0, sticky=tk.W)
        # bouton sélection de date
        # https://www.svgrepo.com/svg/533381/calendar-alt
        self.icon_calendar_pil_img = Image.open(Path(ROOT_DIR_PATH) / "assets" / "icon_calendar.png").resize((20, 20))
        self.icon_calendar = ImageTk.PhotoImage(self.icon_calendar_pil_img)
        self.button_select_new_week = ttk.Button(
            self.frame_date_left,
            image=self.icon_calendar,
            # command=self.select_week
            command=lambda: ModaleSelectionDate(callback=self.select_week)
        )
        self.button_select_new_week.grid(column=0, row=0, sticky=tk.W)
        # label d'affichage des dates de la semaine
        self.label_current_week = ttk.Label(self.frame_date, anchor="center", width=41)
        self.label_current_week.grid(column=1, row=0)

        # création de la frame "planning"
        self.frame_planning = ttk.Frame(self, borderwidth=1, relief="sunken")
        # self.frame_planning = ttk.Frame(self)
        self.frame_planning.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        # 7 colonnes :
        # - titres des lignes (les heures)
        # - jours de la semaine (lundi, mardi ...)
        # 25 lignes :
        # - titres des colonnes (jours de la semaine)
        # - 1 ligne par demi heure, entre 8h00 et 20h00 (12 * 2)
        # titres des colonnes
        self.planning_column_titles: list[dict] = []
        weekdays_names = [
            "Lundi",
            "Mardi",
            "Mercredi",
            "Jeudi",
            "Vendredi",
            "Samedi"
        ]
        for weekday_number, weekday_name in enumerate(weekdays_names):
            # print(weekday_number, weekday_name)
            column_index = weekday_number + 1
            # partage l'espace disponible entre les colonnes
            self.frame_planning.columnconfigure(column_index, weight=1)
            planning_column_title = {}
            # ajoute une frame pour chaque titre de colonne
            planning_column_title["frame"] = ttk.Frame(self.frame_planning, borderwidth=1, relief="solid")
            planning_column_title["frame"].grid(column=column_index, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
            # remplis la largeur disponible avec la frame
            planning_column_title["frame"].columnconfigure(0, weight=1)
            # ajoute le label du jour de la semaine
            planning_column_title["day_name_label"] = ttk.Label(
                planning_column_title["frame"],
                text=weekday_name,
                width=8
            )
            planning_column_title["day_name_label"].grid(column=0, row=1, sticky=tk.W)
            # ajoute le label de la date de la journée
            planning_column_title["day_date_label"] = ttk.Label(
                planning_column_title["frame"],
                foreground="gray"
            )
            planning_column_title["day_date_label"].grid(column=0, row=0, sticky=tk.E)
            self.planning_column_titles.append(planning_column_title)
        # titres des lignes
        self.planning_row_titles = []
        self.planning_row_times = [datetime(
            year=self.date_monday_week_displayed.year,
            month=self.date_monday_week_displayed.month,
            day=self.date_monday_week_displayed.day,
            hour=8
        ) + row_number * timedelta(seconds=60*30) for row_number in range(24)]
        self.planning_row_names = [row_time.strftime("%Hh%M") for row_time in self.planning_row_times]
        for timestamp_number, timestamp_name in enumerate(self.planning_row_names):
            # print(timestamp_number, timestamp_name)
            row_index = timestamp_number + 1
            # partage l'espace disponible entre les lignes
            self.frame_planning.rowconfigure(row_index, weight=1)
            planning_row_title = {}
            # ajoute une frame toutes les 2 lignes (les heures entières)
            if timestamp_number % 2 == 0:
                planning_row_title["frame"] = ttk.Frame(self.frame_planning, borderwidth=1, relief="solid")
                planning_row_title["frame"].grid(column=0, row=row_index, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
                # remplis la hauteur disponible avec les deux lignes suivantes
                planning_row_title["frame"].rowconfigure(0, weight=1)
                # ajoute le label de l'heure entière associée
                planning_row_title["timestamp_label"] = ttk.Label(
                    planning_row_title["frame"],
                    text=timestamp_name,
                    foreground="gray"
                )
                planning_row_title["timestamp_label"].grid(column=0, row=0, sticky=tk.N)
            self.planning_row_titles.append(planning_row_title)
        # matrice des frames du planning
        # accès: self.planning_frames_matrix[weekday][timestamp_number]
        self.planning_frames_matrix = []
        for column_index in range(6):
            planning_frames_column = []
            for row_index in range(24):
                planning_content_frame = ttk.Frame(self.frame_planning, borderwidth=1, relief="solid")
                planning_content_frame.grid(column=column_index+1, row=row_index+1, sticky=(tk.N, tk.W, tk.E, tk.S))
                planning_frames_column.append(planning_content_frame)
            self.planning_frames_matrix.append(planning_frames_column)

        # maj de l'affichage de la page
        self.update_planning()

    def update_planning(self):
        # met à jour l'état du bouton "Nouveau RDV"
        if self.planning_selected.get() == "Cabinet":
            self.button_nouveau_rdv["state"] = "disabled"
        else:
            self.button_nouveau_rdv["state"] = "normal"
        # met à jour le label de la semaine affichée
        # self.label_current_week["text"] = "Semaine n°10, du XX/XX/XXXX au XX/XX/XXXX"
        # print(format_date(date=self.date_monday_week_displayed, format="short", locale="fr_FR"))
        # string_monday = format_date(date=self.date_monday_week_displayed, format="short", locale="fr_FR")
        string_monday = self.date_monday_week_displayed.strftime("%d/%m/%Y")
        date_sunday = self.date_monday_week_displayed + timedelta(days=6)
        # string_sunday = format_date(date=date_sunday, format="short", locale="fr_FR")
        string_sunday = date_sunday.strftime("%d/%m/%Y")
        week_number = self.date_monday_week_displayed.isocalendar().week
        self.label_current_week["text"] = f"Semaine n°{week_number}, du {string_monday} au {string_sunday}"
        # met à jour la date de chacuns des jours affichés
        for weekday_number, planning_column_title in enumerate(self.planning_column_titles):
            planning_column_title["day_date"] = self.date_monday_week_displayed + timedelta(days=weekday_number)
            planning_column_title["day_date_label"]["text"] = planning_column_title["day_date"].strftime("%d/%m")

    def select_previous_week(self):
        # print("select previous week")
        self.date_monday_week_displayed -= timedelta(days=7)
        self.update_planning()

    def select_next_week(self):
        # print("select next week")
        self.date_monday_week_displayed += timedelta(days=7)
        self.update_planning()

    def select_week(self, date_selected: datetime):
        # print("select new week")
        # ModaleSelectionDate()
        # print("date sélectionnée:", date_selected)
        self.date_monday_week_displayed = date_selected - timedelta(days=date_selected.weekday())
        self.update_planning()

    def open_modale_nouveau_rdv(self):
        selected_medecin = self.planning_selected.get()
        ref_medecin = self.medecin_name_displayed_to_ref[selected_medecin]
        ModaleNouveauRDV(self.bdd_manager, ref_medecin)
        # print("modale fermée")

    def modale_modifier_horaires(self):
        planning_selected = self.planning_selected.get()
        ref_medecin = self.medecin_name_displayed_to_ref.get(planning_selected)
        ModaleModifierHoraires(self.bdd_manager, ref_medecin, self.update_planning)

    def modale_etat_consultation(self):
        ModaleEtatConsultations(self.bdd_manager)
