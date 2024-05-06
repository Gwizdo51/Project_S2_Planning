import tkinter as tk
from tkinter import *
from tkinter import ttk
from bdd import *

root = Tk()

root.title("victoire")
root.minsize(width=600, height=500)


####################################################################################################

#fonction pour recuperer le contenue des champs de saisie / les stock / les affiche
def recupere_contenu():
    nom = champ_nom.get()
    prenom = champ_prenom.get()
    tel = champ_telephone.get()
    civilite = champ_civilite.get()
    ajout_etudiant(nom, prenom, tel, civilite)




# champ de saisie
champ_nom = tk.Entry(root)
champ_nom.pack()
champ_prenom = tk.Entry(root)
champ_prenom.pack()
champ_telephone = tk.Entry(root)
champ_telephone.pack()
champ_civilite = tk.Entry(root)
champ_civilite.pack()

# envoyer
bouton_recuperer = tk.Button(root, text="Récupérer contenu", command=recupere_contenu)
bouton_recuperer.pack()



root.mainloop()

