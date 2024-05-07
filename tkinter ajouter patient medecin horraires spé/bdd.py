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

def ajout_horaires_speciaux(date_debut, date_fin, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "INSERT INTO horaires_speciaux ( date_debut, date_fin, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (date_debut, date_fin, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche)
    curseur.execute(sql_query, values)
    connexion_mysql.commit()
    connexion_mysql.close()