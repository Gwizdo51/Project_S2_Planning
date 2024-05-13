import sys
from pathlib import Path
import mysql.connector as mysql
from datetime import date, time, datetime
# import locale

ROOT_DIR_PATH = str(Path(__file__).resolve().parents[1])
if ROOT_DIR_PATH not in sys.path:
    sys.path.insert(0, ROOT_DIR_PATH)


class BDDManager:

    config = {
        "user": "root",
        "password": "root",
        "host": "127.0.0.1",
        "database": "careplan",
        "port": 3306
    }

    def __init__(self):
        # self.connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
        self.connexion_mysql = mysql.connect(**self.config)
        self.curseur = self.connexion_mysql.cursor()
        # locale.setlocale()
        # pass

    def ajout_patient(self, nom, prenom, num_tel, civilite):
        # civilité :
        # 0 : Monsieur
        # 1 : Madame
        # 2 : Mademoiselle
        sql_query = "INSERT INTO patient (nom, prenom, num_tel, civilite) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, num_tel, civilite)
        self.curseur.execute(sql_query, values)
        self.connexion_mysql.commit()

    def get_all_patients(self):
        sql_query = "SELECT * FROM patient"
        self.curseur.execute(sql_query)
        patient_list = []
        for patient in self.curseur:
            patient_dict = {}
            patient_dict["ref_patient"] = patient[0]
            patient_dict["nom"] = patient[1]
            patient_dict["prenom"] = patient[2]
            patient_dict["num_tel"] = patient[3]
            patient_dict["civilite"] = patient[4]
            patient_list.append(patient_dict)
        # return self.curseur.fetchall()
        return patient_list

    def ajout_medecin(self, nom, prenom, num_tel, specialite, horaires_lundi="",
                      horaires_mardi="", horaires_mercredi="", horaires_jeudi="", horaires_vendredi="",
                      horaires_samedi="", horaires_dimanche=""):
        # horaires format : "08h00-12h00 14h00-18h00"
        sql_query = ("INSERT INTO medecin (nom, prenom, num_tel, specialite, "
                     "horaires_lundi, horaires_mardi, horaires_mercredi, horaires_jeudi, "
                     "horaires_vendredi, horaires_samedi, horaires_dimanche) "
                     "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (nom, prenom, num_tel, specialite, horaires_lundi,
                  horaires_mardi, horaires_mercredi, horaires_jeudi,
                  horaires_vendredi, horaires_samedi, horaires_dimanche)
        self.curseur.execute(sql_query, values)
        self.connexion_mysql.commit()

    def get_all_medecins(self):
        sql_query = "SELECT * FROM medecin"
        self.curseur.execute(sql_query)
        medecin_list = []
        for medecin in self.curseur:
            medecin_dict = {}
            medecin_dict["ref_medecin"] = medecin[0]
            medecin_dict["nom"] = medecin[1]
            medecin_dict["prenom"] = medecin[2]
            medecin_dict["num_tel"] = medecin[3]
            medecin_dict["specialite"] = medecin[4]
            medecin_dict["horaires_lundi"] = medecin[5]
            medecin_dict["horaires_mardi"] = medecin[6]
            medecin_dict["horaires_mercredi"] = medecin[7]
            medecin_dict["horaires_jeudi"] = medecin[8]
            medecin_dict["horaires_vendredi"] = medecin[9]
            medecin_dict["horaires_samedi"] = medecin[10]
            medecin_dict["horaires_dimanche"] = medecin[11]
            medecin_list.append(medecin_dict)
        return medecin_list

    def affichage_nom_medecins(self, ref_medecin):
        requete_sql = "SELECT nom FROM medecin WHERE ref_medecin = %s"
        self.curseur.execute(requete_sql, (ref_medecin,))
        nom_medecin = self.curseur.fetchall()
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

    def supprimer_medecin(self, ref_medecin):
        sql_query = "DELETE FROM medecin WHERE ref_medecin = %s"
        self.curseur.execute(sql_query, (ref_medecin,))
        self.connexion_mysql.commit()

    def supprimer_ref_hor_spe(self, ref_hor_spe):
        sql_query = "DELETE FROM horaires_speciaux WHERE ref_hor_spe = %s"
        self.curseur.execute(sql_query, (ref_hor_spe,))
        self.connexion_mysql.commit()

    def close(self):
        self.curseur.close()
        self.connexion_mysql.close()

    def modifier_medecin(self, nv_nom, nv_prenom, nv_num_tel, nv_specialite, nv_horaire_lundi, nv_horaire_mardi,
                         nv_horaire_mercredi, nv_horaire_jeudi, nv_horaire_vendredi, nv_horaire_samedi,
                         nv_horaire_dimanche, ref_medecin):
        sql_query = "UPDATE medecin SET nom = %s, prenom = %s, num_tel = %s, specialite = %s, horaires_lundi = %s, horaires_mardi = %s, horaires_mercredi = %s, horaires_jeudi = %s, horaires_vendredi = %s, horaires_samedi = %s, horaires_dimanche = %s WHERE ref_medecin = %s"
        self.curseur.execute(sql_query, (
            nv_nom, nv_prenom, nv_num_tel, nv_specialite, nv_horaire_lundi, nv_horaire_mardi, nv_horaire_mercredi,
            nv_horaire_jeudi, nv_horaire_vendredi, nv_horaire_samedi, nv_horaire_dimanche, ref_medecin))
        self.connexion_mysql.commit()


if __name__ == "__main__":
    # tests
    bdd_manager = BDDManager()

    # write tests
    # bdd_manager.ajout_patient("Dubois", "Henry", "0123456789", 0)
    # bdd_manager.ajout_patient("Dupond", "Marie", "0123456789", 1)
    # bdd_manager.supprimer_patient(2)
    # bdd_manager.ajout_medecin(
    #     nom="Doolittle",
    #     prenom="John",
    #     num_tel="0123456789",
    #     specialite="généraliste",
    #     horaires_mercredi="08h00-12h00 13h30-17h00",
    #     horaires_jeudi="08h00-12h00"
    # )
    # bdd_manager.ajout_medecin(
    #     nom="House",
    #     prenom="Gregory",
    #     num_tel="0123456789",
    #     specialite="cardiologue",
    #     horaires_vendredi="07h30-13h00"
    # )
    # bdd_manager.supprimer_medecin(1)
    # bdd_manager.ajout_rdv(
    #     date_heure_debut=datetime(
    #         year=2024,
    #         month=5,
    #         day=12,
    #         hour=12
    #     ),
    #     duree=time(hour=1, minute=30),
    #     ref_patient=4,
    #     ref_medecin=2
    # )

    # read tests
    patients_list = bdd_manager.get_all_patients()
    print(len(patients_list))
    for patient in patients_list:
        print(patient)
    medecins_list = bdd_manager.get_all_medecins()
    print(len(medecins_list))
    for medecin in medecins_list:
        print(medecin)
    bdd_manager.close()
