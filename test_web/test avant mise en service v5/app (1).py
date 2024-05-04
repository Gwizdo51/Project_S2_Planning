from flask import Flask, render_template, request
from bdd import recuperer_des_etudiants_par, sql_tb

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Définit une valeur par défaut pour option_selectionnee si ce n'est pas déjà défini
    global test
    if 'option_selectionnee' not in globals():
        option_selectionnee = 0  # Mettez ici la valeur par défaut désirée
    else:
        option_selectionnee = globals()['option_selectionnee']
    if request.method == 'POST':
        option_selectionnee = int(request.form['menu_deroulant'])

    ############################################################

    # Exécute la requête SQL en fonction de la valeur de option_selectionnee

    print(option_selectionnee)
    return render_template("index.html", dt=sql_tb(option_selectionnee))


@app.route('/recherche', methods=['GET', 'POST'])
def recherche_etudiant():
    if request.method == 'POST':
        donnees = request.form
        nom = donnees.get('nom')
        list_etudiant = recuperer_des_etudiants_par(nom)
        print(list_etudiant)
    else:
        list_etudiant = None

    return render_template("recherche.html", etudiant=list_etudiant)


if __name__ == '__main__':
    app.run(debug=True)
