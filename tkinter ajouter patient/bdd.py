import mysql.connector as mysql

def ajout_etudiant(nom, prenom, num_tel, civilite):
    connexion_mysql = mysql.connect(user='root', password='root', host='127.0.0.1', database='doctime', port=3306)
    curseur = connexion_mysql.cursor()
    sql_query = "INSERT INTO patient ( nom, prenom, num_tel, civilite) VALUES ( %s, %s, %s, %s)"
    values = (nom, prenom, num_tel, civilite)
    curseur.execute(sql_query, values)
    connexion_mysql.commit()
    connexion_mysql.close()
