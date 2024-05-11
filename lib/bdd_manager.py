import sys
from pathlib import Path
import mysql.connector as mysql

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[1])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class BDDManager:

    def __init__(self):
        self.connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
        self.curseur = self.connexion_mysql.cursor()

    def ajout_patient(self, nom, prenom, num_tel, civilite):
        sql_query = "INSERT INTO patient ( nom, prenom, num_tel, civilite) VALUES ( %s, %s, %s, %s)"
        values = (nom, prenom, num_tel, civilite)
        self.curseur.execute(sql_query, values)
        self.connexion_mysql.commit()


    def ajout_medecin(self, nom, prenom, num_tel, specialite,horaires_lundi,horaires_mardi,horaires_mercredi,horaires_jeudi,horaires_vendredi,horaires_samedi,horaires_dimanche):
        sql_query = "INSERT INTO medecin ( nom, prenom, num_tel, specialite, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, num_tel, specialite, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche)
        self.curseur.execute(sql_query, values)
        self.connexion_mysql.commit()

    def affichage_nom_medecins(self, option):
        connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
        curseur = connexion_mysql.cursor()
        requete_sql = "SELECT nom FROM medecin WHERE ref_medecin = %s"
        curseur.execute(requete_sql, (option,))
        nom_medecin = curseur.fetchall()
        # connexion_mysql.close()
        return nom_medecin


    def ajout_horaires_speciaux(self, dt_debut,dt_fin,h_lundi,h_mardi,h_mercredi,h_jeudi,h_vendredi,h_samedi,h_dimanche,ref_med):
        sql_query = "INSERT INTO horaires_speciaux (date_debut, date_fin, horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, horaires_vendredi, horaires_samedi, horaires_dimanche, ref_medecin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (dt_debut, dt_fin, h_lundi, h_mardi, h_mercredi, h_jeudi, h_vendredi, h_samedi, h_dimanche,ref_med)
        self.curseur.execute(sql_query, values)
        self.connexion_mysql.commit()

    def ajout_rdv(self, date_heure_debut, duree, ref_patient, ref_medecin):
        sql_query = "INSERT INTO rdv (date_heure_debut, duree, ref_patient, ref_medecin) VALUES (%s, %s, %s, %s)"
        values = (date_heure_debut, duree, ref_patient, ref_medecin)
        self.curseur.execute(sql_query, values)
        self.connexion_mysql.commit()

    def supprimer_rdv(self, ref_patient):
        sql_query = "DELETE FROM rdv WHERE ref_patient = %s"
        self.curseur.execute(sql_query, (ref_patient,))
        self.connexion_mysql.commit()

    def supprimer_patient(self, ref_patient):
        sql_query = "DELETE FROM patient WHERE ref_patient = %s"
        self.curseur.execute(sql_query, (ref_patient,))
        self.connexion_mysql.commit()

    def supprimer_medic(self, ref_medecin):
        sql_query = "DELETE FROM medecin WHERE ref_medecin = %s"
        self.curseur.execute(sql_query, (ref_medecin,))
        self.connexion_mysql.commit()

    def supprimer_ref_hor_spe(self, ref_hor_spe):
        sql_query = "DELETE FROM horaires_speciaux WHERE ref_hor_spe = %s"
        self.curseur.execute(sql_query, (ref_hor_spe,))
        self.connexion_mysql.commit()

    # def maj_bdd(self):
    #     self.connexion_mysql.commit()
    #     # self.connexion_mysql.close()


if __name__ == "__main__":
    bdd_manager = BDDManager()
    bdd_manager.ajout_medecin(...)
