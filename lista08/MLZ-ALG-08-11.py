def codificar(texto):
    if len(texto) == 0:
        return []

    caractere = texto[0]
    contador = 1

    while contador < len(texto) and texto[contador] == caractere:
        contador += 1

    return [caractere, contador] + codificar(texto[contador:])

texto = input("Digite uma string: ")

print(codificar(texto))