from .estilo_jogo import categoria

class Personagem:
    def __init__(self, nome, atributos, raca, classe):
        self.nome = nome
        self.atributos = atributos
        self.raca = raca
        self.classe = classe

    def to_dict(self):
        return {
            "nome": self.nome,
            "atributos": {k: (v, categoria(k, v)) for k, v in self.atributos.items()},
            "raca": {
                "nome": str(self.raca),
                "movimento": self.raca.movimento,
                "infravisao": self.raca.infravisao,
                "alinhamento": self.raca.alinhamento,
                "habilidades": self.raca.habilidades,
            },
            "classe": {
                "nome": str(self.classe),
                "habilidades": self.classe.habilidades,
            },
        }
