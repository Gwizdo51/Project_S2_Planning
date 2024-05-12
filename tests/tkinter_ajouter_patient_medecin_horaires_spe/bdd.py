import mysql.connector as mysql


def ajout_patient(nom, prenom, num_tel, civilite):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "INSERT INTO patient ( nom, prenom, num_tel, civilite) VALUES ( %s, %s, %s, %s)"
    values = (nom, prenom, num_tel, civilite)
    curseur.execute(sql_query, values)
    connexion_mysql.commit()
    connexion_mysql.close()


def ajout_medecin(nom, prenom, num_tel, specialite,horaires_lundi,horaires_mardi,horaires_mercredi,horaires_jeudi,horaires_vendredi,horaires_samedi,horaires_dimanche):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "INSERT INTO medecin ( nom, prenom, num_tel, specialite, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nom, prenom, num_tel, specialite, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche)
    curseur.execute(sql_query, values)
    connexion_mysql.commit()
    connexion_mysql.close()

def affichage_nom_medecins(option):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    requete_sql = "SELECT nom FROM medecin WHERE ref_medecin = %s"
    curseur.execute(requete_sql, (option,))
    nom_medecin = curseur.fetchall()
    connexion_mysql.close()
    return nom_medecin


def ajout_horaires_speciaux(dt_debut,dt_fin,h_lundi,h_mardi,h_mercredi,h_jeudi,h_vendredi,h_samedi,h_dimanche,ref_med):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "INSERT INTO horaires_speciaux (date_debut, date_fin, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche, ref_medecin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (dt_debut, dt_fin, h_lundi, h_mardi, h_mercredi, h_jeudi, h_vendredi, h_samedi, h_dimanche,ref_med)
    curseur.execute(sql_query, values)
    connexion_mysql.commit()
    connexion_mysql.close()

def ajout_rdv(date_heure_debut, duree, ref_patient, ref_medecin):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "INSERT INTO rdv (date_heure_debut, duree, ref_patient, ref_medecin) VALUES (%s, %s, %s, %s)"
    values = (date_heure_debut, duree, ref_patient, ref_medecin)
    curseur.execute(sql_query, values)
    connexion_mysql.commit()
    connexion_mysql.close()

def supprimer_rdv(ref_patient):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "DELETE FROM rdv WHERE ref_patient = %s"
    curseur.execute(sql_query, (ref_patient,))
    connexion_mysql.commit()
    connexion_mysql.close()

def supprimer_patient(ref_patient):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "DELETE FROM patient WHERE ref_patient = %s"
    curseur.execute(sql_query, (ref_patient,))
    connexion_mysql.commit()
    connexion_mysql.close()

def supprimer_medic(ref_medecin):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "DELETE FROM medecin WHERE ref_medecin = %s"
    curseur.execute(sql_query, (ref_medecin,))
    connexion_mysql.commit()
    connexion_mysql.close()

def supprimer_ref_hor_spe(ref_hor_spe):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "DELETE FROM horaires_speciaux WHERE ref_hor_spe = %s"
    curseur.execute(sql_query, (ref_hor_spe,))
    connexion_mysql.commit()
    connexion_mysql.close()




def modifier_rdv(nouvelle_heure_debut, nouvelle_duree, ref_rdv):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "UPDATE rdv SET date_heure_debut = %s, duree = %s WHERE ref_patient = %s"
    curseur.execute(sql_query, (nouvelle_heure_debut, nouvelle_duree, ref_rdv))
    connexion_mysql.commit()
    connexion_mysql.close()

def modifier_patient(nouveau_nom, nouveau_prenom, nouveau_num_tel , nouvelle_civilite , ref_patient):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "UPDATE patient SET nom = %s, prenom = %s , num_tel %s , civilite = %s WHERE ref_patient = %s"
    curseur.execute(sql_query, (nouveau_nom, nouveau_prenom,nouveau_num_tel,nouvelle_civilite, ref_patient))
    connexion_mysql.commit()
    connexion_mysql.close()

def modifier_medecin(nv_nom, nv_prenom,nv_num_tel,nv_specialite,nv_horaire_lundi,nv_horaire_mardi,nv_horaire_mercredi,nv_horaire_jeudi,nv_horaire_vendredi,nv_horaire_samedi,nv_horaire_dimanche,ref_medecin):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "UPDATE medecin SET nom = %s,prenom = %s ,num_tel = %s ,specialite = %s ,horaires_lundi = %s ,horaires_mardi = %s ,horaires_mercredi = %s ,horaires_jeudi = %s ,horaires_vendredi = %s,horaires_samedi = %s,horaires_dimanche = %s WHERE ref_patient = %s"
    curseur.execute(sql_query, (nv_nom, nv_prenom,nv_num_tel,nv_specialite,nv_horaire_lundi,nv_horaire_mardi,nv_horaire_mercredi,nv_horaire_jeudi,nv_horaire_vendredi,nv_horaire_samedi,nv_horaire_dimanche,ref_medecin))
    connexion_mysql.commit()
    connexion_mysql.close()

def modifier_horaires_speciaux(nv_dt_db,nv_dt_fin,nv_h_lundi,nv_h_mardi,nv_h_mercredi,nv_h_jeudi,nv_h_vendredi,nv_h_samedi,nv_h_dimanche,ref_medecin,ref_hor_spe):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "UPDATE horaires_speciaux SET date_debut = %s,date_fin = %s, horaires_lundi = %s ,horaires_mardi = %s ,horaires_mercredi = %s ,horaires_jeudi = %s ,horaires_vendredi = %s,horaires_samedi = %s,horaires_dimanche = %s, ref_medecin = %s WHERE ref_hor_spe = %s"
    curseur.execute(sql_query, (nv_dt_db,nv_dt_fin,nv_h_lundi,nv_h_mardi,nv_h_mercredi,nv_h_jeudi,nv_h_vendredi,nv_h_samedi,nv_h_dimanche,ref_medecin,ref_hor_spe))
    connexion_mysql.commit()
    connexion_mysql.close()