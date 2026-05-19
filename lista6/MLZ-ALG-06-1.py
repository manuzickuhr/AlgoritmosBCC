numeros = []

while True:
    num = int(input("Digite um número inteiro (0 para sair): "))
    if num==0:
        break 
    numeros.append(num)


for i in range(len(numeros)):
    for j in range(0, (len(numeros)) -1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

for numero in numeros:
    print(numero)