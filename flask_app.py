
from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


# Page d'accueil
@app.get("/")
def accueil():
    return render_template("accueil.html")


# Page de présentation
@app.get("/presentation")
def presentation():
    return render_template(
        "presentation.html",
        prenom="Rayan",
        nom="Moghrabi",
        loisirs=["Musique et rap", "Jeux vidéo", "Sport"]
    )


# Page des loisirs
@app.get("/loisirs")
def loisirs():
    return render_template(
        "presentation.html",
        prenom="Rayan",
        nom="Moghrabi",
        loisirs=["Musique et rap", "Jeux vidéo", "Sport"]
    )


# Exercice 7 : prénom dans l'URL, avec template sécurisé
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


# Exercice 7 : calcul avec paramètres d'URL
@app.get("/calcul")
def calcul():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        return "Erreur : a et b doivent être des nombres entiers.", 400

    op = request.args.get("op", "plus")

    if op == "plus":
        resultat = a + b
        symbole = "+"
    elif op == "moins":
        resultat = a - b
        symbole = "-"
    elif op == "fois":
        resultat = a * b
        symbole = "×"
    elif op == "divise":
        if b == 0:
            return "Erreur : division par zéro impossible.", 400
        resultat = a / b
        symbole = "÷"
    else:
        return "Opération inconnue.", 400

    return f"{a} {symbole} {b} = {resultat}"


# Exercice 8 : afficher le formulaire
@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


# Exercice 8 : recevoir les données en GET ou POST
@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
        couleur = request.form.get("couleur", "royalblue")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
        couleur = request.args.get("couleur", "royalblue")

    # Autoriser uniquement les couleurs prévues dans le formulaire
    couleurs_autorisees = ["tomato", "teal", "royalblue"]
    if couleur not in couleurs_autorisees:
        couleur = "royalblue"

    return render_template(
        "salut.html",
        prenom=prenom,
        ville=ville,
        couleur=couleur,
        methode=request.method
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
