def divisores_de_n(n):

    divisores = []

    for i in range(1, n):

        if n % i == 0:
            divisores.append(i)

    return divisores

def numero_perfeito(n):
    divisores = divisores_de_n(n)
    resultado = 0

    for divisor in divisores:
        resultado += divisor
    
    if resultado==n:
        return True
    return False

def main():

    print("Números perfeitos de 1 a 10.000")
    for i in range(1, 10001):
        resultado = numero_perfeito(i)

        if resultado:
            print(i)
    
main()