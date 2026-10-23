
# ---------------------------------------------------------------
# Mon premier site Web avec Flask
# ---------------------------------------------------------------
# Ce fichier reçoit les demandes des navigateurs et fabrique
# les réponses en utilisant des templates HTML.
# ---------------------------------------------------------------

from flask import Flask, render_template

app = Flask(__name__)


# Page d'accueil
@app.get("/")
def accueil():
    return "Bienvenue sur mon site !"


# Page de présentation utilisant un template HTML
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


# ---------------------------------------------------------------
# Ne pas modifier : utile seulement pour lancer le site
# sur votre propre ordinateur
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
