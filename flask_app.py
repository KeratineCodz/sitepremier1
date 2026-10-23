
# ---------------------------------------------------------------
# Mon premier site Web avec Flask
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


@app.get("/")
def accueil():
    return "Bienvenue sur mon site !"


@app.get("/presentation")
def presentation():
    return """
    <h1>Rayan Moghrabi</h1>

    <p>Je suis étudiant en <strong>informatique</strong>.</p>

    <h2>Mes loisirs</h2>
    <ul>
        <li>La musique et le rap</li>
        <li>Les jeux vidéo</li>
        <li>Le sport</li>
    </ul>

    <h2>Un langage que j'apprends</h2>
    <p>Je découvre actuellement Python et HTML.</p>

    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100">
    """


@app.get("/loisirs")
def loisirs():
    return """
    <h1>Mes loisirs</h1>
    <p>J'aime la musique, le rap, les jeux vidéo et le sport.</p>
    """


# Ne pas modifier cette partie
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
