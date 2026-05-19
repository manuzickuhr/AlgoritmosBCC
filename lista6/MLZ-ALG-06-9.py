numeros = []
media = 0
abaixo_media = []
valores_media = []
acima_media = []

while True:
    num = input("Digite um número: (enter para sair)")
    if num == "":
        break
    numeros.append(int(num))
    media += int(num)

media = media / len(numeros)

for numero in numeros:
    if numero == media:
        valores_media.append(numero)
    elif numero < media:
        abaixo_media.append(numero)
    else:
        acima_media.append(numero)

print()

print("Média:", media)

print("\nValores abaixo da média:")

if len(abaixo_media) == 0:
    print("Não há valores abaixo da média.")
else:
    for numero in abaixo_media:
        print(numero)


print("\nValores iguais à média:")

if len(valores_media) == 0:
    print("Não há valores iguais à média.")
else:
    for numero in valores_media:
        print(numero)


print("\nValores acima da média:")

if len(acima_media) == 0:
    print("Não há valores acima da média.")
else:
    for numero in acima_media:
        print(numero)