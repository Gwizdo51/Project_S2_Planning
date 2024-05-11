import tkinter as tk

def configurer_entree(entree, texte_par_defaut):
    entree.insert(0, texte_par_defaut)
    entree.bind("<FocusIn>", lambda event: entree.delete(0, tk.END))
    entree.bind("<FocusOut>", lambda event: entree.insert(0, texte_par_defaut) if not entree.get() else None)


fenetre = tk.Tk()
fenetre.title("Exemple de champ de saisie avec texte par défaut")
frame_principal = tk.Frame(fenetre)
frame_principal.pack()

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

fenetre.mainloop()
