def removendo_extremos(lista: list, n: int):
    nova_lista = lista.copy()

    for i in range(n):
        nova_lista.remove(max(nova_lista))
        nova_lista.remove(min(nova_lista))

    return nova_lista


# Programa principal
numeros = []

while True:
    valor = input("Digite um número (ENTER para parar): ")

    if valor == "":
        break

    numeros.append(float(valor))

if len(numeros) < 4:
    print("Erro: é necessário informar pelo menos 4 valores.")
else:
    resultado = removendo_extremos(numeros, 2)

    print("Lista sem extremos:", resultado)
    print("Lista original:", numeros)