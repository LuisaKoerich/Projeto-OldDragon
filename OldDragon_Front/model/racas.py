class Humano:
    def __init__(self):
        self.movimento = "9m"
        self.infravisao = "Nenhuma"
        self.alinhamento = "Qualquer"
        self.habilidades = ["Aprendizado", "Adaptabilidade"]
    def __repr__(self):
        return "Humano"

class Elfo:
    def __init__(self):
        self.movimento = "9m"
        self.infravisao = "18m"
        self.alinhamento = "Tendem à Neutralidade"
        self.habilidades = ["Percepção Natural", "Graciosos", "Arma Racial", "Imunidades"]
    def __repr__(self):
        return "Elfo"
    
class Anao:
    def __init__(self):
        self.movimento = "6m"
        self.infravisao = "18m"
        self.alinhamento = "Tendem à Ordem"
        self.habilidades = ["Mineradores", "Vigoroso", "Armas grandes", "Inimigos"]
    def __repr__(self):
        return "Anão"

class Halfling:
    def __init__(self):
        self.movimento = "6m"
        self.infravisao = "Nenhuma"
        self.alinhamento = "Tendem à Neutralidade"
        self.habilidades = ["Furtivos", "Destemidos", "Bons de Mira", "Pequenos", "Restrições"]
    def __repr__(self):
        return "Halfling"
