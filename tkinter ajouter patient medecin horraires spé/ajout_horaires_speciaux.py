import tkinter as tk
from tkinter import *
from tkinter import ttk

from bdd import *

root = Tk()

root.title("Victoire")
root.minsize(width=600, height=500)

ref_medic = None  # Initialisation de ref_medic globalement

def option_selected(event):
    global ref_medic
    selected_option = dropdown.get()
    print("Option sélectionnée :", selected_option)
    if selected_option == "dead":
        ref_medic = 1
    elif selected_option == "dilan":
        ref_medic = 2
    elif selected_option == "defoi":
        ref_medic = 3

def recupere_contenu_ajout_horairesSpeciaux():
    date_debut = champ_date_debut.get()
    date_fin = champ_date_fin.get()
    hlundi = champ_horaires_lundi.get()
    hmardi = champ_horaires_mardi.get()
    hmercredi = champ_horaires_mercredi.get()
    hjeudi = champ_horaires_jeudi.get()
    hvendredi = champ_horaires_vendredi.get()
    hsamedi = champ_horaires_samedi.get()
    hdimanche = champ_horaires_dimanche.get()
    if ref_medic is not None:
        ajout_horaires_speciaux(date_debut, date_fin, hlundi, hmardi, hmercredi, hjeudi, hvendredi, hsamedi, hdimanche, ref_medic)
    else:
        print("Veuillez sélectionner une option de médecin.")

# Création de la liste des options
options = ["dead", "dilan", "defoi"]  # Exemple d'options, à remplacer par les noms réels des médecins

# Création du widget de menu déroulant
dropdown = ttk.Combobox(root, values=options)
dropdown.pack(pady=20)
dropdown.set("Sélectionnez une option")  # Texte par défaut affiché dans le menu déroulant

# Lier une fonction à l'événement de sélection d'option
dropdown.bind("<<ComboboxSelected>>", option_selected)

# champs de saisie
champ_date_debut = tk.Entry(root)
champ_date_debut.pack()
champ_date_fin = tk.Entry(root)
champ_date_fin.pack()
champ_horaires_lundi = tk.Entry(root)
champ_horaires_lundi.pack()
champ_horaires_mardi = tk.Entry(root)
champ_horaires_mardi.pack()
champ_horaires_mercredi = tk.Entry(root)
champ_horaires_mercredi.pack()
champ_horaires_jeudi = tk.Entry(root)
champ_horaires_jeudi.pack()
champ_horaires_vendredi = tk.Entry(root)
champ_horaires_vendredi.pack()
champ_horaires_samedi = tk.Entry(root)
champ_horaires_samedi.pack()
champ_horaires_dimanche = tk.Entry(root)
champ_horaires_dimanche.pack()

# Bouton pour récupérer le contenu
bouton_recuperer = tk.Button(root, text="Récupérer contenu", command=recupere_contenu_ajout_horairesSpeciaux)
bouton_recuperer.pack()

root.mainloop()
