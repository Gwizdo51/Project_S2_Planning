import tkinter as tk
from tkinter import *
from bdd import *

root = Tk()

root.title("victoire")
root.minsize(width=600, height=500)


####################################################################################################

#fonction pour recuperer le contenue des champs de saisie / les stock / les affiche
def recupere_contenu_ajout_medecin():
    nom = champ_nom.get()
    prenom = champ_prenom.get()
    tel = champ_telephone.get()
    specialite = champ_specialite.get()
    horaires_lundi = champ_horaires_lundi.get()
    horaires_mardi = champ_horaires_mardi.get()
    horaires_mercredi = champ_horaires_mercredi.get()
    horaires_jeudi = champ_horaires_jeudi.get()
    horaires_vendredi = champ_horaires_vendredi.get()
    horaires_samedi = champ_horaires_samedi.get()
    horaires_dimanche = champ_horaires_dimanche.get()
    ajout_medecin(nom, prenom, tel, specialite, horaires_lundi, horaires_mardi, horaires_mercredi ,horaires_jeudi ,horaires_vendredi ,horaires_samedi ,horaires_dimanche)




# champ de saisie
champ_nom = tk.Entry(root)
champ_nom.pack()
champ_prenom = tk.Entry(root)
champ_prenom.pack()
champ_telephone = tk.Entry(root)
champ_telephone.pack()
champ_specialite = tk.Entry(root)
champ_specialite.pack()
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

# envoyer
bouton_recuperer = tk.Button(root, text="Récupérer contenu", command=recupere_contenu_ajout_medecin)
bouton_recuperer.pack()



root.mainloop()

