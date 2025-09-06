from personagens import Personagem

def menu_estilo():
    print("\nEscolha o estilo de rolagem:")
    print("1) Clássico — 3d6 em ordem")
    print("2) Aventureiro — 3d6 seis vezes; distribuir")
    print("3) Heróico — 4d6 descarta menor; distribuir")
    return input("Opção (1/2/3): ").strip()

def main():
    print("=== CRIAÇÃO DE PERSONAGEM — OLD DRAGON ===")
    nome = input("Nome do personagem: ").strip()
    personagem = Personagem(nome)
    personagem.mostrar_ficha()

if __name__ == "__main__":
    main()
