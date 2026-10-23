
from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
