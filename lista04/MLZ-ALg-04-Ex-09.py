soma = 0
quantidade = 0

maior = None
menor = None

while True:
    entrada = input("Digite um número (ou ENTER para sair): ")
    
    if entrada == "":
        break

    n = int(entrada)

    soma += n
    quantidade += 1

    if maior is None or n > maior:
        maior = n

    if menor is None or n < menor:
        menor = n

if quantidade > 0:
    media = soma / quantidade
    print("Média:", media)
    print("Maior:", maior)
    print("Menor:", menor)
else:
    print("Nenhum número foi digitado.")