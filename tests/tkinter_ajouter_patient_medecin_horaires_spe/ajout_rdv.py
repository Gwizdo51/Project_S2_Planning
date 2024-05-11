import tkinter as tk
from tkinter import ttk
from bdd import *

root = tk.Tk()

root.title("Victoire")
root.minsize(width=600, height=500)

ref_medic = None  # Initialisation de ref_medic globalement
ref_patient = None

def option_selected(event):
    global ref_medic
    select_option = dropdown_medecin.get()
    print("Option sélectionnée (médecin) :", select_option)
    if select_option == "dead":
        ref_medic = 1
    elif select_option == "dilan":
        ref_medic = 2
    elif select_option == "defoi":
        ref_medic = 3

def option_select_patient(event):
    global ref_patient
    select_option_patient = dropdown_patient.get()
    print("Option sélectionnée (patient) :", select_option_patient)
    if select_option_patient == "ladebrouille":
        ref_patient = 1
    elif select_option_patient == "rousseau":
        ref_patient = 2
    elif select_option_patient == "lelouche":
        ref_patient = 3
    elif select_option_patient == "vibreure":
        ref_patient = 4
    elif select_option_patient == "fontaine":
        ref_patient = 5
    elif select_option_patient == "stagiaire":
        ref_patient = 6

def recupere_contenu_ajout_rdv():
    date_heure_debut = champ_date_heure_debut.get()
    duree = champ_duree.get()
    if ref_medic is not None and ref_patient is not None:
        ajout_rdv(date_heure_debut, duree, ref_patient, ref_medic)
    else:
        print("Veuillez sélectionner une option de médecin et un patient.")

# Création de la liste des options médecin
options_medecin = ["dead", "dilan", "defoi"]  # Exemple d'options, à remplacer par les noms réels des médecins

# Création du widget de menu déroulant pour les médecins
dropdown_medecin = ttk.Combobox(root, values=options_medecin)
dropdown_medecin.pack(pady=10)
dropdown_medecin.set("Sélectionnez un médecin")  # Texte par défaut affiché dans le menu déroulant

# Création de la liste des options patient
options_patient = ["ladebrouille", "rousseau", "lelouche", "vibreure", "fontaine", "stagiaire"]  # Exemple d'options, à remplacer par les noms réels des patients

# Création du widget de menu déroulant pour les patients
dropdown_patient = ttk.Combobox(root, values=options_patient)
dropdown_patient.pack(pady=10)
dropdown_patient.set("Sélectionnez un patient")  # Texte par défaut affiché dans le menu déroulant

# Lier une fonction à l'événement de sélection d'option pour les médecins
dropdown_medecin.bind("<<ComboboxSelected>>", option_selected)

# Lier une fonction à l'événement de sélection d'option pour les patients
dropdown_patient.bind("<<ComboboxSelected>>", option_select_patient)

# champs de saisie
champ_date_heure_debut = tk.Entry(root)
champ_date_heure_debut.pack()
champ_duree = tk.Entry(root)
champ_duree.pack()

# Bouton pour récupérer le contenu
bouton_recuperer = tk.Button(root, text="Récupérer contenu", command=recupere_contenu_ajout_rdv)
bouton_recuperer.pack()

root.mainloop()
