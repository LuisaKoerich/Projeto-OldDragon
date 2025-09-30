from model.estilo_jogo import categoria

class Personagem:
    def __init__(self, nome, raca, classe_base, atributos, especializacao="Nenhuma"):
        self.nome = nome
        self.raca = raca
        self.classe_base = classe_base 
        self.especializacao = especializacao  
        self.atributos = atributos
        self.atributos_classificados = {
            attr: f"{valor} ({categoria(attr, valor)})"
            for attr, valor in atributos.items()
        }

    def ficha_dict(self):
        return {
            "nome": self.nome,
            "raca": str(self.raca),
            "classe_base": str(self.classe_base),
            "especializacao": self.especializacao,
            "atributos": {attr: f"{valor} ({categoria(attr, valor)})" for attr, valor in self.atributos.items()},
            "habilidades_classe": self.classe_base.habilidades,
            "movimento": self.raca.movimento,
            "infravisao": self.raca.infravisao,
            "alinhamento": self.raca.alinhamento,
            "habilidades_raca": self.raca.habilidades,
        }
