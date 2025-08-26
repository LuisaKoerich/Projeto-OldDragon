from dados import rolar_3d6, rolar_4d6_drop_menor

ATRIBUTOS = ["Força (FOR)", "Destreza (DES)", "Constituição (CON)",
             "Inteligência (INT)", "Sabedoria (SAB)", "Carisma (CAR)"]

def categoria(atributo, valor):
    if atributo == "Força (FOR)":
        return "Fraco" if valor <= 8 else "Mediano" if valor <= 12 else "Forte" if valor <= 16 else "Muito Forte"
    if atributo == "Destreza (DES)":
        return "Letárgico" if valor <= 8 else "Mediano" if valor <= 12 else "Ágil" if valor <= 16 else "Preciso"
    if atributo == "Constituição (CON)":
        return "Frágil" if valor <= 8 else "Mediano" if valor <= 12 else "Resistente" if valor <= 16 else "Vigoroso"
    if atributo == "Inteligência (INT)":
        return "Inepto" if valor <= 8 else "Mediano" if valor <= 12 else "Inteligente" if valor <= 16 else "Gênio"
    if atributo == "Sabedoria (SAB)":
        return "Tolo" if valor <= 8 else "Mediano" if valor <= 12 else "Intuitivo" if valor <= 16 else "Presciente"
    if atributo == "Carisma (CAR)":
        return "Descortês" if valor <= 8 else "Mediano" if valor <= 12 else "Influente" if valor <= 16 else "Ídolo"

def classico():
    valores = [rolar_3d6() for _ in range(6)]
    return dict(zip(ATRIBUTOS, valores))

def _distribuir_interativo(valores):
    atributos = {}
    for atributo in ATRIBUTOS:
        while True:
            print("\nValores disponíveis:", valores)
            try:
                escolha = int(input(f"Escolha um valor para {atributo}: "))
                if escolha in valores:
                    atributos[atributo] = escolha
                    valores.remove(escolha)
                    break
                else:
                    print("Valor inválido!")
            except ValueError:
                print("Digite um número válido!")
    return atributos

def aventureiro():
    valores = [rolar_3d6() for _ in range(6)]
    print("Valores rolados (3d6):", valores)
    return _distribuir_interativo(valores)

def heroico():
    valores = [rolar_4d6_drop_menor() for _ in range(6)]
    print("Valores rolados (4d6 drop menor):", valores)
    return _distribuir_interativo(valores)
