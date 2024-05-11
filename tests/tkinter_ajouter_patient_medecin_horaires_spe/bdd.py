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