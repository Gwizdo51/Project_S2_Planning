import tkinter as tk
from tkinter import ttk

def create_button(parent, text, command):
    button = ttk.Button(parent, text=text, command=command)
    return button

def nouveaux_rdv():
    print("Action: Nouveaux RDV")

def modifier_horaire():
    print("Action: Modifier Horaire")

def impression_historique():
    print("Action: Impression Historique")
    page_page_impression()

def page_principale():
    # Afficher la page principale
    frame_principal.pack()
    frame_page_1.pack_forget()
    frame_page_2.pack_forget()
    frame_page_impression.pack_forget()

def page_page_1():
    # Afficher la page 1
    frame_principal.pack_forget()
    frame_page_1.pack()
    frame_page_2.pack_forget()
    frame_page_impression.pack_forget()

def page_page_2():
    # Afficher la page 2
    frame_principal.pack_forget()
    frame_page_1.pack_forget()
    frame_page_2.pack()
    frame_page_impression.pack_forget()

def page_page_impression():
    # Afficher la page impression
    frame_principal.pack_forget()
    frame_page_1.pack_forget()
    frame_page_2.pack_forget()
    frame_page_impression.pack()

# Fonction pour désactiver les autres boutons radio lorsqu'un bouton est sélectionné
def desactiver_autres_boutons(bouton_actuel, boutons_a_desactiver):
    for bouton in boutons_a_desactiver:
        if bouton != bouton_actuel:
            bouton.deselect()

# Fonction pour configurer le texte par défaut et le griser pour les champs de saisie
def configurer_entree(entree, texte_par_defaut):
    entree.insert(0, texte_par_defaut)
    entree.bind("<FocusIn>", lambda event: entree.delete(0, tk.END))
    entree.bind("<FocusOut>", lambda event: entree.insert(0, texte_par_defaut) if not entree.get() else None)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion des RDV")

# Création des cadres pour chaque page
frame_principal = tk.Frame(root)
frame_page_1 = tk.Frame(root)
frame_page_2 = tk.Frame(root)
frame_page_impression = tk.Frame(root)

# Création des boutons sur la page principale
button_nouveaux_rdv = create_button(frame_principal, "Nouveaux RDV", page_page_1)
button_nouveaux_rdv.pack(pady=10)

button_modifier_horaire = create_button(frame_principal, "Modifier Horaire", modifier_horaire)
button_modifier_horaire.pack(pady=10)

button_impression_historique = create_button(frame_principal, "Impression Historique", impression_historique)
button_impression_historique.pack(pady=10)

# Création des boutons radio
var_option = tk.StringVar()
radio_1 = tk.Radiobutton(frame_principal, text="Option 1", variable=var_option, value="Option 1")
radio_1.pack(pady=5, anchor=tk.W)

radio_2 = tk.Radiobutton(frame_principal, text="Option 2", variable=var_option, value="Option 2")
radio_2.pack(pady=5, anchor=tk.W)

radio_3 = tk.Radiobutton(frame_principal, text="Option 3", variable=var_option, value="Option 3")
radio_3.pack(pady=5, anchor=tk.W)

# Associer la désactivation des autres boutons radio à la sélection d'un bouton radio
radio_1.config(command=lambda: desactiver_autres_boutons(radio_1, [radio_2, radio_3]))
radio_2.config(command=lambda: desactiver_autres_boutons(radio_2, [radio_1, radio_3]))
radio_3.config(command=lambda: desactiver_autres_boutons(radio_3, [radio_1, radio_2]))

# Création du champ de saisie avec le texte par défaut pour le prénom
entree_prenom = tk.Entry(frame_principal, width=30)
entree_prenom.pack(pady=10)
configurer_entree(entree_prenom, "Prénom")

# Création du champ de saisie avec le texte par défaut pour le nom
entree_nom = tk.Entry(frame_principal, width=30)
entree_nom.pack(pady=10)
configurer_entree(entree_nom, "Nom")

# Création du champ de saisie avec le texte par défaut pour le téléphone
entree_telephone = tk.Entry(frame_principal, width=30)
entree_telephone.pack(pady=10)
configurer_entree(entree_telephone, "Téléphone")

# Création du bouton de retour sur les autres pages
button_retour = create_button(frame_page_1, "Retour", page_principale)
button_retour.pack(pady=10)

button_retour = create_button(frame_page_2, "Retour", page_principale)
button_retour.pack(pady=10)

button_retour_impression = create_button(frame_page_impression, "Retour", page_principale)
button_retour_impression.pack(side=tk.LEFT, padx=5, pady=10)

# Création du bouton "Imprimer" sur la page d'impression historique
button_imprimer = create_button(frame_page_impression, "Imprimer", impression_historique)
button_imprimer.pack(side=tk.LEFT, padx=5, pady=10)

# Lancement de la boucle principale
page_principale()
root.mainloop()
