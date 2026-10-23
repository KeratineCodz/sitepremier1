
from flask import Flask, render_template, request

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


# Partie A : prénom dans le chemin de l'URL
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


# Partie B + défi : calcul avec des paramètres dans l'URL
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
        return "Opération inconnue. Utilisez plus, moins, fois ou divise.", 400

    return f"{a} {symbole} {b} = {resultat}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
