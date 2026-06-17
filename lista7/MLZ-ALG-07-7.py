import random


def criar_cartela():
    cartela = {
        "B": random.sample(range(1, 16), 5),
        "I": random.sample(range(16, 31), 5),
        "N": random.sample(range(31, 46), 5),
        "G": random.sample(range(46, 61), 5),
        "O": random.sample(range(61, 76), 5)
    }

    return cartela


def mostrar_cartela(cartela):
    print(" B   I   N   G   O")

    for i in range(5):
        print(
            f"{cartela['B'][i]:2} "
            f"{cartela['I'][i]:3} "
            f"{cartela['N'][i]:3} "
            f"{cartela['G'][i]:3} "
            f"{cartela['O'][i]:3}"
        )


def main():
    cartela = criar_cartela()
    mostrar_cartela(cartela)


main()