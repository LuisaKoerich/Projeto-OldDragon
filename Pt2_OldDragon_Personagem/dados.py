import random

def rolar_d6():
    return random.randint(1, 6)

def rolar_3d6():
    return sum(rolar_d6() for _ in range(3))

def rolar_4d6_drop_menor():
    rolagens = [rolar_d6() for _ in range(4)]
    return sum(rolagens) - min(rolagens)
