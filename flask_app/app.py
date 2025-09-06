from flask import Flask, render_template, request, redirect, url_for, session

from .estilo_jogo import classico, aventureiro, heroico
from .racas import Humano, Elfo, Anao, Halfling
from .classes import (
    Guerreiro, Barbaro, Paladino, Clerigo, Druida, Academico,
    Ladrao, Ranger, Bardo, Mago, Ilusionista, Necromante
)
from .personagens import Personagem

app = Flask(__name__)
app.secret_key = "segredo123"  # Necessário para session


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        estilo = request.form["estilo"]
        raca = request.form["raca"]
        classe = request.form["classe"]

        # Definir atributos
        if estilo == "1":
            atributos = classico()
        elif estilo == "2":
            atributos = aventureiro()
        elif estilo == "3":
            atributos = heroico()
        else:
            atributos = classico()

        # Definir raça
        racas_dict = {
            "humano": Humano,
            "elfo": Elfo,
            "anao": Anao,
            "halfling": Halfling,
        }
        raca_obj = racas_dict.get(raca, Humano)()

        # Definir classe
        classes_dict = {
            "guerreiro": Guerreiro,
            "barbaro": Barbaro,
            "paladino": Paladino,
            "clerigo": Clerigo,
            "druida": Druida,
            "academico": Academico,
            "ladrao": Ladrao,
            "ranger": Ranger,
            "bardo": Bardo,
            "mago": Mago,
            "ilusionista": Ilusionista,
            "necromante": Necromante,
        }
        classe_obj = classes_dict.get(classe, Guerreiro)()

        # Criar personagem
        personagem = Personagem(nome, atributos, raca_obj, classe_obj)

        # Guardar na sessão
        session["personagem"] = personagem.to_dict()

        return redirect(url_for("ficha"))

    return render_template("index.html")


@app.route("/ficha")
def ficha():
    personagem = session.get("personagem")
    if not personagem:
        return redirect(url_for("index"))
    return render_template("ficha.html", personagem=personagem)


if __name__ == "__main__":
    app.run(debug=True)
