import random


def criar_cartela():
    return {
        "B": random.sample(range(1, 16), 5),
        "I": random.sample(range(16, 31), 5),
        "N": random.sample(range(31, 46), 5),
        "G": random.sample(range(46, 61), 5),
        "O": random.sample(range(61, 76), 5)
    }


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


def cartela_vencedora(cartela):
    letras = ["B", "I", "N", "G", "O"]

    # Verifica linhas horizontais
    for i in range(5):
        soma_linha = 0

        for letra in letras:
            soma_linha += cartela[letra][i]

        if soma_linha == 0:
            return True

    # Verifica colunas verticais
    for letra in letras:
        if sum(cartela[letra]) == 0:
            return True

    # Verifica diagonal principal
    soma_diagonal1 = 0

    for i in range(5):
        soma_diagonal1 += cartela[letras[i]][i]

    if soma_diagonal1 == 0:
        return True

    # Verifica diagonal secundária
    soma_diagonal2 = 0

    for i in range(5):
        soma_diagonal2 += cartela[letras[i]][4 - i]

    if soma_diagonal2 == 0:
        return True

    return False


def main():
    # Cartela com linha horizontal vencedora
    cartela1 = criar_cartela()
    for letra in ["B", "I", "N", "G", "O"]:
        cartela1[letra][0] = 0

    print("Cartela com linha horizontal:")
    mostrar_cartela(cartela1)
    print("Vencedora?", cartela_vencedora(cartela1))
    print()

    # Cartela com coluna vertical vencedora
    cartela2 = criar_cartela()
    cartela2["B"] = [0, 0, 0, 0, 0]

    print("Cartela com coluna vertical:")
    mostrar_cartela(cartela2)
    print("Vencedora?", cartela_vencedora(cartela2))
    print()

    # Cartela com diagonal vencedora
    cartela3 = criar_cartela()
    letras = ["B", "I", "N", "G", "O"]

    for i in range(5):
        cartela3[letras[i]][i] = 0

    print("Cartela com diagonal:")
    mostrar_cartela(cartela3)
    print("Vencedora?", cartela_vencedora(cartela3))
    print()

    # Cartela com zeros, mas sem vencer
    cartela4 = criar_cartela()
    cartela4["B"][0] = 0
    cartela4["I"][2] = 0
    cartela4["N"][4] = 0
    cartela4["G"][1] = 0
    cartela4["O"][3] = 0

    print("Cartela com zeros, mas não vencedora:")
    mostrar_cartela(cartela4)
    print("Vencedora?", cartela_vencedora(cartela4))


main()