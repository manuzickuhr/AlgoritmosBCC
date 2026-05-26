def buscaReversa(dicionario, valorBuscado):

    chaves = []

    for chave, valor in dicionario.items():

        if valor == valorBuscado:
            chaves.append(chave)

    return chaves


def main():

    pessoas = {
        "Ana": 20,
        "Carlos": 25,
        "Maria": 20,
        "João": 30
    }

    print(buscaReversa(pessoas, 20))
    print(buscaReversa(pessoas, 25))
    print(buscaReversa(pessoas, 40))


main()