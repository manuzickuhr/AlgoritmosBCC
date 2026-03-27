x = 1
soma = 0

maior = None
menor = None

while x <= 10:
    n1 = int(input("Digite um número inteiro: "))
    
    soma += n1

    if maior is None or n1 > maior:
        maior = n1

    if menor is None or n1 < menor:
        menor = n1

    x += 1

media = soma / 10

print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)