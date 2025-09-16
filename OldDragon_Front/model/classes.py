class Guerreiro:
    def __init__(self):
        self.hp_base = 10
        self.habilidades = ["Aparar", "Maestria em Arma", "Ataque Extra"]
    def __repr__(self):
        return "Guerreiro"
                
class Barbaro(Guerreiro):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Vigor Bárbaro", "Talentos Selvagens", "Supresa Selvagem", "Força do Totem"])
    def __repr__(self):
        return "Bárbaro"

class Paladino(Guerreiro):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Imunidade a Doenças", "Cura pelas Mãos", "Aura de Proteção", "Espada Sagrada"])
    def __repr__(self):
        return "Paladino"  
                                                  
class Clerigo:
    def __init__(self):
        self.hp_base = 8
        self.habilidades = ["Magia Divina", "Afastar Mortos Vivos", "Cura Milagrosa"]
    def __repr__(self):
        return "Clérigo"
            
class Druida(Clerigo):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Herbalismo", "Previdência", "Transformação"])
    def __repr__(self):
        return "Druida"
            
class Academico(Clerigo):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Conhecimento Acadêmico", "Decifrar Linguagens", "Lendas e Tradições"])
    def __repr__(self):
        return "Acadêmico"
        
class Mago:
    def __init__(self):
        self.hp_base = 4
        self.habilidades = ["Magias Arcanas", "Ler Magias", "Detectar Magias"]
        self.magias_exclusivas = []
    def __repr__(self):
        return "Mago"
            
class Ilusionista(Mago):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Miragem", "Ilusão Melhorada", "Ilusão Permanente"])    
    def __repr__(self):
        return "Ilusionista"
            
class Necromante(Mago):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Criar Mortos Vivos", "Drenar Vida", "Magia da Morte"])
    def __repr__(self):
        return "Necromante"       
    
class Ladrao:
    def __init__(self):
        self.hp_base = 6
        self.habilidades = ["Ataque Furtivo", "Ouvir Ruídos", "Talentos de Ladrão"]
    def __repr__(self):
        return "Ladrão"
            
class Ranger(Ladrao):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Inimigo Mortal", "Combativo", "Previdência", "Companheiro Animal"])
    def __repr__(self):
        return "Ranger"
    
class Bardo(Ladrao):
    def __init__(self):
        super().__init__()
        self.habilidades.extend(["Influenciar", "Inspirar", "Fascinar", "Usar Pergaminhos"])
    def __repr__(self):
        return "Bardo"
    