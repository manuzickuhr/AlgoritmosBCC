def diferencaSimetrica(a, b):

    resposta = list(a ^ b)

    resposta.sort()

    return resposta

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

resultado = diferencaSimetrica(conjunto1, conjunto2)

print(resultado)