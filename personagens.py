from estilo_jogo import classico, aventureiro, heroico, categoria
from racas import escolher_raca
from classes import escolher_classe

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.raca = None
        self.classe = None
        self.atributos = {}

        from main import menu_estilo
        estilo = menu_estilo()
        if estilo == "1":
            self.atributos = classico()
        elif estilo == "2":
            self.atributos = aventureiro()
        elif estilo == "3":
            self.atributos = heroico()
        else:
            print("Opção inválida, usando estilo clássico por padrão.")
            self.atributos = classico()

        self.raca = escolher_raca()
        self.classe = escolher_classe()

    def mostrar_ficha(self):
        print("\n=== FICHA DO PERSONAGEM ===")
        print()
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Classe: {self.classe}")
        print("\nAtributos:")
        for attr, valor in self.atributos.items():
            print(f"  {attr}: {valor} ({categoria(attr, valor)})")
        print("\nHabilidades da classe:")
        for h in self.classe.habilidades:
            print(f"  - {h}")
        print("\nCaracterísticas raciais:")
        print(f"  Movimento: {self.raca.movimento}")
        print(f"  Infravisão: {self.raca.infravisao}")
        print(f"  Alinhamento: {self.raca.alinhamento}")
        print("  Habilidades:", ", ".join(self.raca.habilidades))
