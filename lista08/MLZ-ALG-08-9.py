def raiz_quadrada(n, estimativa=1.0):
    if abs(estimativa ** 2 - n) <= 1e-12:
        return estimativa

    nova_estimativa = (estimativa + n / estimativa) / 2

    return raiz_quadrada(n, nova_estimativa)

print(raiz_quadrada(2))
print(raiz_quadrada(9))
print(raiz_quadrada(25))
print(raiz_quadrada(100))