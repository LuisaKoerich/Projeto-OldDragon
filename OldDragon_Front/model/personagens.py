from model.estilo_jogo import categoria

class Personagem:
    def __init__(self, nome, raca, classe, atributos):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.atributos = atributos
        # cria um dicionário já com categoria
        self.atributos_classificados = {
            attr: f"{valor} ({categoria(attr, valor)})"
            for attr, valor in atributos.items()
        }

    def ficha_dict(self):
        return {
            "nome": self.nome,
            "raca": str(self.raca),
            "classe": str(self.classe),
            "atributos": {attr: f"{valor} ({categoria(attr, valor)})" for attr, valor in self.atributos.items()},
            "habilidades_classe": self.classe.habilidades,
            "movimento": self.raca.movimento,
            "infravisao": self.raca.infravisao,
            "alinhamento": self.raca.alinhamento,
            "habilidades_raca": self.raca.habilidades,
        }
