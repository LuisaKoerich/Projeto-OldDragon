from flask import Flask, render_template, request, session
from model.personagens import Personagem
from model.racas import Humano, Elfo, Anao, Halfling
from model.classes import *
from model.estilo_jogo import classico, aventureiro, heroico, ATRIBUTOS
import random

app = Flask(__name__)
app.secret_key = "segredo123"  # necessário para usar session

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        nome = request.form["nome"]
        raca_escolhida = request.form["raca"]
        classe_base = request.form["classe_base"]
        especializacao = request.form.get("especializacao", "Nenhuma")
        estilo = request.form["estilo"]

        # Salva no session os dados já escolhidos
        session["nome"] = nome
        session["raca"] = raca_escolhida
        session["classe_base"] = classe_base
        session["especializacao"] = especializacao

        if estilo == "1":  # Clássico
            atributos = classico()
            return finalizar_personagem(atributos)
        elif estilo in ["2", "3"]:  # Aventureiro ou Heróico
            if estilo == "2":
                valores = [random.randint(3, 18) for _ in range(6)]  # rolar 3d6
            else:
                valores = [sum(sorted([random.randint(1, 6) for _ in range(4)])[1:]) for _ in range(6)]  # 4d6 drop menor

            session["valores_rolados"] = valores
            return render_template("atributos.html", valores=valores, atributos=ATRIBUTOS)
        else:
            atributos = classico()
            return finalizar_personagem(atributos)

    return render_template("criar.html")

@app.route("/atributos", methods=["POST"])
def distribuir_atributos():
    valores = session.get("valores_rolados", [])
    atributos = {}
    usados = []
    for attr in ATRIBUTOS:
        valor = int(request.form[attr])
        if valor in valores and valores.count(valor) > usados.count(valor):
            atributos[attr] = valor
            usados.append(valor)
        else:
            return "Erro: valor inválido ou repetido além do permitido."
    return finalizar_personagem(atributos)

def finalizar_personagem(atributos):
    nome = session["nome"]
    raca_escolhida = session["raca"]
    classe_base = session["classe_base"]
    especializacao = session["especializacao"]

    racas_dict = {"Humano": Humano(), "Elfo": Elfo(), "Anao": Anao(), "Halfling": Halfling()}
    raca = racas_dict[raca_escolhida]

    if especializacao != "Nenhuma":
        class_key = especializacao
    else:
        base_map = {"Guerreiro": "Guerreiro", "Clerigo": "Clerigo", "Ladrao": "Ladrao", "Mago": "Mago"}
        class_key = base_map.get(classe_base, classe_base)

    classes_dict = {
        "Guerreiro": Guerreiro(), "Barbaro": Barbaro(), "Paladino": Paladino(),
        "Clerigo": Clerigo(), "Druida": Druida(), "Academico": Academico(),
        "Mago": Mago(), "Ilusionista": Ilusionista(), "Necromante": Necromante(),
        "Ladrao": Ladrao(), "Ranger": Ranger(), "Bardo": Bardo()
    }
    classe = classes_dict[class_key]

    personagem = Personagem(nome, raca, classe, atributos)
    return render_template("ficha.html", personagem=personagem)

    return render_template("criar.html")


if __name__ == "__main__":
    app.run(debug=True)
