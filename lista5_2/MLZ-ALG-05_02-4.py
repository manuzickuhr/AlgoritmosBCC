def calcular_mediana(a, b, c):
    soma = a + b + c
    return soma - min(a, b, c) - max(a, b, c)

def main():
    print("Digite três números:")
    n1 = float(input("1º número: "))
    n2 = float(input("2º número: "))
    n3 = float(input("3º número: "))

    resultado = calcular_mediana(n1, n2, n3)
    
    print(f"A mediana é: {resultado}")

main()