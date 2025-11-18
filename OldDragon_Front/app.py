from flask import Flask, render_template, request, session
from model.personagens import Personagem
from model.racas import Humano, Elfo, Anao, Halfling
from model.classes import *
from model.estilo_jogo import classico, aventureiro, heroico, ATRIBUTOS
import json
import random

app = Flask(__name__)
app.secret_key = "segredo123"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        nome = request.form["nome"]
        raca_escolhida = request.form["raca"]
        classe_base = request.form["classe_base"]
        especializacao = request.form["especializacao"]
        estilo = request.form["estilo"]

        session["nome"] = nome
        session["raca"] = raca_escolhida
        session["classe_base"] = classe_base
        session["especializacao"] = especializacao

        # Estilo Clássico
        if estilo == "1":
            atributos = classico()
            return finalizar_personagem(atributos)

        # Estilo Aventureiro ou Heróico
        if estilo == "2":
            valores = [random.randint(3, 18) for _ in range(6)]
        else:
            valores = [sum(sorted([random.randint(1, 6) for _ in range(4)])[1:]) for _ in range(6)]

        session["valores_rolados"] = valores

        return render_template(
            "atributos.html",
            valores=valores,
            atributos=ATRIBUTOS
        )

    return render_template("criar.html")

@app.route("/atributos", methods=["POST"])
def distribuir_atributos():
    valores = session.get("valores_rolados", [])
    atributos = {}

    for attr in ATRIBUTOS:
        valor = int(request.form[attr])

        if valor in valores:
            atributos[attr] = valor
        else:
            return f"Erro: valor {valor} inválido."

    return finalizar_personagem(atributos)

def finalizar_personagem(atributos):
    nome = session["nome"]
    raca_escolhida = session["raca"]
    classe_base = session["classe_base"]
    especializacao = session["especializacao"]

    racas_dict = {
        "Humano": Humano(),
        "Elfo": Elfo(),
        "Anao": Anao(),
        "Halfling": Halfling()
    }
    raca = racas_dict[raca_escolhida]

    classes_base_dict = {
        "Guerreiro": Guerreiro(),
        "Clerigo": Clerigo(),
        "Ladrao": Ladrao(),
        "Mago": Mago()
    }
    classe_base_obj = classes_base_dict[classe_base]

    personagem = Personagem(
        nome,
        raca,
        classe_base_obj,
        atributos,
        especializacao
    )

    # ajuste json 'salvar personagem'
    personagem_dict = {
        "nome": personagem.nome,
        "raca": str(personagem.raca),
        "classe_base": str(personagem.classe_base),
        "especializacao": personagem.especializacao,
        "atributos": personagem.atributos,
        "atributos_classificados": personagem.atributos_classificados,
        "habilidades_classe": personagem.classe_base.habilidades,
        "movimento": personagem.raca.movimento,
        "infravisao": personagem.raca.infravisao,
        "alinhamento": personagem.raca.alinhamento,
        "habilidades_raca": personagem.raca.habilidades
    }

    with open("personagem.json", "w", encoding="utf-8") as f:
        json.dump(personagem_dict, f, indent=4, ensure_ascii=False)

    print(">>> Personagem salvo em personagem.json")

    return render_template("ficha.html", personagem=personagem)

if __name__ == "__main__":
    app.run(debug=True)
