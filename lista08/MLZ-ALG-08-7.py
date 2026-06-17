def decimal_para_binario(q):
    resultado = ""

    while True:
        resto = q % 2
        resultado = str(resto) + resultado
        q = q // 2

        if q == 0:
            break

    return resultado

n = int(input("Digite um número decimal: "))
print(decimal_para_binario(n))