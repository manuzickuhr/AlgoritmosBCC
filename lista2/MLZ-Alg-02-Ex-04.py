n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
medio = n1 + n2+ n3 - maior - menor

print(menor, medio, maior)