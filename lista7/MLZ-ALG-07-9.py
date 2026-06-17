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
    print("--------------------------------")
    print("| B     I     N     G     O |")
    print("--------------------------------")

    for i in range(5):
        print(
            f"| {cartela['B'][i]:2} "
            f"  {cartela['I'][i]:3} "
            f"  {cartela['N'][i]:3} "
            f"  {cartela['G'][i]:3} "
            f"  {cartela['O'][i]:3} |"
        )

    print("--------------------------------")


def cartela_vencedora(cartela):
    letras = ["B", "I", "N", "G", "O"]

    for i in range(5):
        if sum(cartela[letra][i] for letra in letras) == 0:
            return True

    for letra in letras:
        if sum(cartela[letra]) == 0:
            return True

    if sum(cartela[letras[i]][i] for i in range(5)) == 0:
        return True

    if sum(cartela[letras[i]][4 - i] for i in range(5)) == 0:
        return True

    return False


def criar_chamadas():
    chamadas = []

    for numero in range(1, 76):
        if numero <= 15:
            chamadas.append(("B", numero))
        elif numero <= 30:
            chamadas.append(("I", numero))
        elif numero <= 45:
            chamadas.append(("N", numero))
        elif numero <= 60:
            chamadas.append(("G", numero))
        else:
            chamadas.append(("O", numero))

    random.shuffle(chamadas)
    return chamadas


def marcar_numero(cartela, letra, numero):
    for i in range(5):
        if cartela[letra][i] == numero:
            cartela[letra][i] = 0


def jogar_partida():
    cartela = criar_cartela()
    chamadas = criar_chamadas()

    quantidade_chamadas = 0

    for letra, numero in chamadas:
        marcar_numero(cartela, letra, numero)
        quantidade_chamadas += 1

        if cartela_vencedora(cartela):
            return quantidade_chamadas, cartela


def main():
    resultados = []
    ultima_cartela = None

    for i in range(1000):
        quantidade, cartela = jogar_partida()
        resultados.append(quantidade)
        ultima_cartela = cartela

    minimo = min(resultados)
    maximo = max(resultados)
    media = sum(resultados) / len(resultados)

    print(f"Minimo: {minimo}")
    print(f"Medio: {media:.2f}")
    print(f"Maximo: {maximo}")
    print()

    mostrar_cartela(ultima_cartela)


main()