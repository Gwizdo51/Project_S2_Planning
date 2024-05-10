import mysql.connector as mysql
from flask import Flask, render_template, request
def recuperer_des_etudiants_par(nom):
    mysql_connection = mysql.connect(user='root', password='root', host='127.0.0.1', database='derniere', port=3306)
    cursor = mysql_connection.cursor()
    cursor.execute("SELECT Nom,Prenom,Adresse,Ville,Email FROM etudiant WHERE nom = %s;", (nom,))
    etudiants = cursor.fetchall()
    mysql_connection.close()
    return etudiants

def sql_tb(option):

    mysql_connection = mysql.connect(user='root', password='root', host='127.0.0.1', database='derniere', port=3306)
    cursor = mysql_connection.cursor()

    if option == 0:
        cursor.execute("SELECT Intitule FROM seance;")
    elif option == 1:
        cursor.execute("SELECT Debut FROM seance WHERE Code_C = 1;")
    elif option == 2:
        cursor.execute("SELECT Debut FROM seance WHERE Code_C = 2;")
    elif option == 3:
        cursor.execute("SELECT Intitule FROM seance WHERE Code_C = 3;")

    date_retour = cursor.fetchall()
    mysql_connection.close()
    return date_retour









def sql_tb1():
    mysql_connection = mysql.connect(user='root', password='root', host='127.0.0.1', database='derniere', port=3306)
    cursor = mysql_connection.cursor()
    cursor.execute("SELECT Debut FROM seance WHERE Code_C = 1;")
    date_retour = cursor.fetchall()
    mysql_connection.close()
    return date_retour