import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
from tkcalendar import Calendar
from datetime import datetime

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class ModaleSelectionDate(tk.Toplevel):

    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.title("Sélection de date")
        # taille fixe
        self.resizable(False, False)
        # fonction callback pour update la date sélectionnée
        self.callback = callback
        # le widget Calendar
        self.calendar_widget = Calendar(self, locale="fr_FR")
        self.calendar_widget.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        # appelle une fonction quand une date est choisie
        self.calendar_widget.bind("<<CalendarSelected>>", lambda event: self.select_date())
        # prend le contrôle des intéractions utilisateur
        self.focus()
        self.grab_set()

    def select_date(self):
        date_selected = datetime.strptime(self.calendar_widget.get_date(), "%d/%m/%Y")
        self.callback(date_selected)
        self.destroy()
