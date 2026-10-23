
from flask import Flask, render_template, request, redirect, abort
from markupsafe import escape

app = Flask(__name__)


# Pages principales
@app.get("/")
def accueil():
    return render_template("accueil.html")


@app.get("/presentation")
def presentation():
    return render_template(
        "presentation.html",
        prenom="Rayan",
        nom="Moghrabi",
        loisirs=["Musique et rap", "Jeux vidéo", "Sport"]
    )


@app.get("/loisirs")
def loisirs():
    return render_template(
        "presentation.html",
        prenom="Rayan",
        nom="Moghrabi",
        loisirs=["Musique et rap", "Jeux vidéo", "Sport"]
    )


# Exercice 7 : prénom dans l'URL
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


# Exercice 7 : calcul
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


# Exercice 8 : formulaire
@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


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


# Exercice 9 : redirection
@app.get("/home")
def home():
    return redirect("/")


# Exercice 9 : erreurs personnalisées
@app.get("/secret")
def secret():
    abort(403)


@app.errorhandler(403)
def acces_interdit(erreur):
    return render_template("403.html"), 403


@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


# Exercice 10 : informations reçues par le serveur
@app.get("/moi")
def moi():
    return render_template(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent", "Non renseigné"),
        langues=request.headers.get("Accept-Language", "Non renseigné"),
        entetes=request.headers
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
