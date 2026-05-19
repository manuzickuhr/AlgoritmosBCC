def is_ordenado(lista):

    if not lista:
        return False
    if len(lista) == 1:
        return True
    lista_crescente = sorted(lista)

    if lista_crescente == lista:
        return True
    else:
        lista_decrescente = sorted(lista, reverse=True)
        if lista_decrescente == lista:
            return True
        
    return False


def main():

    lista = []

    while True:

        valor = input("Digite um número (enter para sair): ")

        if valor == "":
            break

        lista.append(int(valor))


    print("\nLista digitada:", lista)

    if is_ordenado(lista):
        print("A lista está ordenada.")
    else:
        print("A lista NÃO está ordenada.")


main()