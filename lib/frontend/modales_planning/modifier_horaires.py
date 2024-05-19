import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from typing import Optional

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)

from lib.bdd_manager import BDDManager


class ModaleModifierHoraires(tk.Toplevel):

    def __init__(self, bdd_manager: BDDManager, planning_selected: Optional[str], callback, **kwargs):
        super().__init__(**kwargs)
        self.planning_selected = planning_selected
        self.bdd_manager = bdd_manager
        self.callback = callback
        # taille de la fenêtre
        self.geometry("800x600")
        # taille fixe
        self.resizable(False, False)
        # titre
        self.title("Modifier horaires")
        # frame principale
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # self.mainframe = ttk.Frame(self, borderwidth=1, relief="solid")
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        # frame header
        # self.frame_header = ttk.Frame(self.mainframe, borderwidth=1, relief="solid")
        self.frame_header = ttk.Frame(self.mainframe)
        self.frame_header.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame_header.columnconfigure(0, weight=1)
        self.frame_header.columnconfigure(1, weight=1)
        self.frame_header.columnconfigure(2, weight=1)
        self.frame_header.rowconfigure(1, weight=1)
        # boutons radio de sélection du type d'horaire à modifier (défaut ou spéciaux)
        self.displayed_modify_mode = "default"
        self.selected_modify_mode = tk.StringVar(value=self.displayed_modify_mode)
        self.radio_button_modify_default = ttk.Radiobutton(
            self.frame_header,
            text="horaires hebdomadaire\npar défaut",
            variable=self.selected_modify_mode,
            value="default",
            command=self.update_modify_mode,
            style="Multiline.TRadiobutton"
        )
        # print(self.radio_button_modify_default.winfo_class())
        self.radio_button_modify_default.grid(column=0, row=0)
        self.radio_button_modify_special = ttk.Radiobutton(
            self.frame_header,
            text="horaires hebdomadaire\nspéciaux",
            variable=self.selected_modify_mode,
            value="special",
            command=self.update_modify_mode,
            style="Multiline.TRadiobutton"
        )
        self.radio_button_modify_special.grid(column=1, row=0)
        # bouton "Valider"
        self.button_apply = ttk.Button(
            self.frame_header,
            text="Valider",
            command=self.commit_schedual
        )
        self.button_apply.grid(column=2, row=0)
        # frame contenu
        # self.frame_content = ttk.Frame(self.mainframe, borderwidth=1, relief="solid")
        self.frame_content = ttk.Frame(self.mainframe)
        self.frame_content.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        # ajoute les noms des jours de la semaine
        weekdays_names = [
            "Lundi :",
            "Mardi :",
            "Mercredi :",
            "Jeudi :",
            "Vendredi :",
            "Samedi :"
        ]
        self.content_rows = []
        for weekday_number, weekday_name in enumerate(weekdays_names):
            content_row = {}
            content_row["label_row_title"] = ttk.Label(
                self.frame_content,
                text=weekday_name
            )
            content_row["label_row_title"].grid(column=0, row=weekday_number, sticky=tk.E)
            self.content_rows.append(content_row)
        for child in self.frame_content.winfo_children():
            child.grid_configure(padx=10, pady=10)
        self.focus()
        self.grab_set()

    def update_modify_mode(self):
        # print("updating modify mode")
        if self.displayed_modify_mode != self.selected_modify_mode.get():
            print("modifying mode")
            self.displayed_modify_mode = self.selected_modify_mode.get()

    def commit_schedual(self):
        print("committing schedual")
