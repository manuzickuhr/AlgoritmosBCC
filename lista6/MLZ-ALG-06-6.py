def divisores_de_n(n):

    divisores = []

    for i in range(1, n):

        if n % i == 0:
            divisores.append(i)

    return divisores


def main():

    numero = int(input("Digite um número inteiro positivo: "))

    divisores = divisores_de_n(numero)

    print("Os divisores de", numero, "são:")

    for divisor in divisores:
        print(divisor)


main()