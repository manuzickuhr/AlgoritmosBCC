numeros = []
negativos = []
zeros = []
positivos = []

while True:
    numero = (input("Digite um número (enter para sair): "))
    if numero=="":
        break
    numeros.append(int(numero))


for numero in numeros:
    if numero < 0:
        negativos.append(numero)
    elif numero == 0:
        zeros.append(numero)
    else:
        positivos.append(numero)

for negativo in negativos:
    print(negativo)

for zero in zeros:
    print(zero)

for positivo in positivos:
    print(positivo)
