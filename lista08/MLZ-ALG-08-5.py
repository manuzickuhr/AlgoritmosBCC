def soma_valores():
    valor = input("Digite um número (ENTER para parar): ")

    if valor == "":
        return 0.0

    return float(valor) + soma_valores()

print("Soma =", soma_valores())