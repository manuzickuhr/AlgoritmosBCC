def formatar_lista(lista):

    string = ""

    for l in range(len(lista)):

        if l == 0:
            string += lista[l]

        elif l == len(lista) - 1:
            string += " e " + lista[l]

        else:
            string += ", " + lista[l]

    return string


def main():

    lista = []

    while True:

        item = input("Digite um item da lista (enter para sair): ")
        
        if item == "":
            break

        lista.append(item)

    print(formatar_lista(lista))


main()