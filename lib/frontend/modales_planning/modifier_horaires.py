import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[3])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class ModaleModifierHoraires(tk.Toplevel):
    pass
